from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
from PIL import Image
import io
import numpy as np
import tensorflow as tf
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from models import disease_collection, DiseaseInfo

# Initialize FastAPI app
app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Load ML model
try:
    model = tf.keras.models.load_model(r"../models/inceptionv3_model_v2.keras")
    print("✅ Model loaded successfully.")
except Exception as e:
    print(f"❌ Failed to load model: {e}")
    raise e

# Class names
class_names = ['Healthy', 'Mosaic', 'RedRot', 'Rust', 'Yellow']


# ------------------- Prediction Endpoint -------------------
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        print(f"File Received: {file.filename}")

        if file.content_type not in ["image/jpeg", "image/png"]:
            raise HTTPException(status_code=400, detail="Invalid file type. Only JPEG and PNG are allowed.")

        # Preprocess
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        image = image.resize((224, 224))

        image_array = np.array(image) / 255.0
        image_array = np.expand_dims(image_array, axis=0)

        # Predict
        prediction = model.predict(image_array)
        predicted_class_index = np.argmax(prediction, axis=1)[0]
        predicted_class_name = class_names[predicted_class_index]

        print(f"Prediction: {predicted_class_name}")

        # Query MongoDB
        disease_info = await disease_collection.find_one({"disease_name": predicted_class_name})

        if disease_info:
            return {
                "filename": file.filename,
                "predicted_class": predicted_class_name,
                "predicted_class_index": int(predicted_class_index),
                "description": disease_info.get("description"),
                "cause": disease_info.get("cause"),
                "symptoms": disease_info.get("symptoms"),
                "pre_management": disease_info.get("pre_management"),
                "mid_management": disease_info.get("mid_management"),
                "future_management": disease_info.get("future_management"),
                "precautions": disease_info.get("precautions"),
            }
        else:
            return {
                "filename": file.filename,
                "predicted_class": predicted_class_name,
                "predicted_class_index": int(predicted_class_index),
                "message": "No additional information found.",
            }

    except Exception as e:
        print(f"Error during prediction: {e}")
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


# ------------------- Extra Endpoint to Insert Diseases -------------------
@app.post("/add-disease")
async def add_disease(disease: DiseaseInfo):
    try:
        # Check if disease already exists
        existing = await disease_collection.find_one({"disease_name": disease.disease_name})
        if existing:
            raise HTTPException(status_code=400, detail="Disease already exists.")

        result = await disease_collection.insert_one(disease.dict())
        return {"message": "Disease added successfully", "id": str(result.inserted_id)}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error inserting disease: {str(e)}")


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)


# from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
# from PIL import Image
# import io
# import numpy as np
# import tensorflow as tf
# import uvicorn
# from fastapi.middleware.cors import CORSMiddleware
# from models import disease_collection  # Mongo collection
# from bson import ObjectId

# # Initialize FastAPI app
# app = FastAPI()

# # CORS Middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000"],  # frontend URL
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"]
# )

# # Load ML model
# try:
#     model = tf.keras.models.load_model(r"../models/inceptionv3_model_v2.keras")
#     print("✅ Model loaded successfully.")
# except Exception as e:
#     print(f"❌ Failed to load model: {e}")
#     raise e

# # Class names
# class_names = ['Healthy', 'Mosaic', 'RedRot', 'Rust', 'Yellow']


# @app.post("/predict")
# async def predict(file: UploadFile = File(...)):
#     try:
#         print(f"File Received: {file.filename}")

#         if file.content_type not in ["image/jpeg", "image/png"]:
#             raise HTTPException(status_code=400, detail="Invalid file type. Only JPEG and PNG are allowed.")

#         # Preprocess
#         image_bytes = await file.read()
#         image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
#         image = image.resize((224, 224))

#         image_array = np.array(image) / 255.0
#         image_array = np.expand_dims(image_array, axis=0)

#         # Predict
#         prediction = model.predict(image_array)
#         predicted_class_index = np.argmax(prediction, axis=1)[0]
#         predicted_class_name = class_names[predicted_class_index]

#         print(f"Prediction: {predicted_class_name}")

#         # Query MongoDB
#         disease_info = await disease_collection.find_one({"disease_name": predicted_class_name})

#         if disease_info:
#             return {
#                 "filename": file.filename,
#                 "predicted_class": predicted_class_name,
#                 "predicted_class_index": int(predicted_class_index),
#                 "description": disease_info.get("description"),
#                 "cause": disease_info.get("cause"),
#                 "symptoms": disease_info.get("symptoms"),
#                 "pre_management": disease_info.get("pre_management"),
#                 "mid_management": disease_info.get("mid_management"),
#                 "future_management": disease_info.get("future_management"),
#                 "precautions": disease_info.get("precautions"),
#             }
#         else:
#             return {
#                 "filename": file.filename,
#                 "predicted_class": predicted_class_name,
#                 "predicted_class_index": int(predicted_class_index),
#                 "message": "No additional information found.",
#             }

#     except Exception as e:
#         print(f"Error during prediction: {e}")
#         raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


# if __name__ == "__main__":
#     uvicorn.run("main:app", host="localhost", port=8000, reload=True)
