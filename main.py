from fastapi import FastAPI, Depends, File, UploadFile, HTTPException
from sqlalchemy.orm import Session
from PIL import Image
import io
import numpy as np
import tensorflow as tf
import uvicorn
from models import DiseaseInfo, SessionLocal
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Add frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Load model and handle exceptions
try:
    model = tf.keras.models.load_model(r"E:/SEM3/MajorProject/models/inceptionv3_model_v2.keras")
    print("Model loaded successfully.")
except Exception as e:
    print(f"Failed to load model: {e}")
    raise e  # Raise error to stop the app if model loading fails

# Class names corresponding to the model's output
class_names = ['Healthy', 'Mosaic', 'RedRot', 'Rust', 'Yellow']

# Database session generator
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Prediction endpoint
@app.post("/predict")
async def predict(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        print(f"File Received: {file.filename}")  # Debugging log
        
        # Check for valid file types
        if file.content_type not in ["image/jpeg", "image/png"]:
            raise HTTPException(status_code=400, detail="Invalid file type. Only JPEG and PNG are allowed.")

        # Read and process image
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        image = image.resize((224, 224))  # Resize to InceptionV3 model input size (299x299)

        image_array = np.array(image) / 255.0  # Normalize pixel values
        image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension

        # Predict the class
        prediction = model.predict(image_array)
        predicted_class_index = np.argmax(prediction, axis=1)[0]
        predicted_class_name = class_names[predicted_class_index]

        print(f"Prediction: {predicted_class_name}")  # Debugging log

        # Query the database for additional disease information
        disease_info = db.query(DiseaseInfo).filter_by(disease_name=predicted_class_name).first()
        print(f"Query Result: {disease_info}")  # Debugging log

        # Return response with predictions and additional info
        if disease_info:
            return {
                "filename": file.filename,
                "predicted_class": predicted_class_name,
                "predicted_class_index": int(predicted_class_index),
                "description":disease_info.description,
                "cause": disease_info.cause,
                "symptoms": disease_info.symptoms,
                "pre_management": disease_info.pre_management,
                "mid_management": disease_info.mid_management,
                "future_management": disease_info.future_management,
                "precautions": disease_info.precautions,
            }
        else:
            return {
                "filename": file.filename,
                "predicted_class": predicted_class_name,
                "predicted_class_index": int(predicted_class_index),
                "message": "No additional information found for this disease.",
            }

    except Exception as e:
        print(f"Error during prediction: {e}")
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

# Run the app with Uvicorn
if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
