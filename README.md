# FastAPI Project
This project demonstrates the development of a FastAPI application, which is designed to handle various backend functionalities such as feature extraction, video processing, and data handling. The project aims to showcase how FastAPI can be used to build efficient and modern web applications with Python.

## ⚙️ Features
***Feature Extraction:*** This module processes video data and extracts relevant features using utils/feature_utils.py.

***Video Processing:*** Handles video data and performs video-related operations using utils/video_utils.py.

***API Endpoints:*** Exposes RESTful APIs for interacting with the backend, developed using FastAPI.

***Testing:*** Includes test scripts (e.g., test_vector.py) for unit tests and ensuring the functionality of the application.

## 📦 Installation

**Clone the repository:**
git clone https://github.com/bit-milind42/FastAPI-Project.git
cd FastAPI-Project


**Set up a virtual environment:**
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows

**Install the required dependencies:**
pip install -r requirements.txt

**🚀 Running the Application**
*To start the FastAPI server:*
uvicorn main:app --reload
**or**
python -m uvicorn main:app --reload
