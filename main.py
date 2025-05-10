# main.py
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from utils.video_utils import extract_frames
from utils.feature_utils import compute_feature_vector
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance
import os
import uuid

app = FastAPI()
FRAMES_DIR = "frames"
COLLECTION_NAME = "video_frames"
client = QdrantClient(":memory:")  # Use Qdrant Cloud or local URL if needed

# Initialize vector collection
client.recreate_collection(
    collection_name=COLLECTION_NAME,
    vectors_config=VectorParams(size=512, distance=Distance.COSINE)
)

@app.post("/upload/")
async def upload_video(file: UploadFile = File(...)):
    contents = await file.read()
    filename = f"temp_{uuid.uuid4().hex}.mp4"
    with open(filename, "wb") as f:
        f.write(contents)

    extracted_paths = extract_frames(filename, FRAMES_DIR, interval=1)
    os.remove(filename)

    points = []
    for path in extracted_paths:
        vector = compute_feature_vector(path)
        point_id = uuid.uuid4().int >> 64
        points.append(PointStruct(id=point_id, vector=vector, payload={"path": path}))

    client.upsert(collection_name=COLLECTION_NAME, points=points)
    return {"message": f"{len(points)} frames processed and stored."}

@app.post("/query/")
async def query_similar(vector: list[float]):
    results = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=vector,
        limit=5
    )
    output = []
    for res in results:
        output.append({
            "score": res.score,
            "vector": res.vector,
            "image_path": res.payload["path"]
        })
    return JSONResponse(content=output)
