import React, { useState } from "react";
import axios from "axios";
import ImageUpload from "./components/ImageUpload";
import Result from "./components/Result";
import Navbar from "./components/Navbar";
import "./App.css";

const App = () => {
  const [currentStep, setCurrentStep] = useState("upload"); // Track current view
  const [selectedFile, setSelectedFile] = useState(null);   // Store uploaded file
  const [result, setResult] = useState(null);               // Store API result
  const [loading, setLoading] = useState(false);            // Track loading state

  const handleFileChange = (file) => {
    console.log("File selected:", file);
    setSelectedFile(file);
    setResult(null); // Clear previous result
  };

  const handleSubmit = async () => {
    if (!selectedFile) {
      alert("Please select a file before submitting.");
      return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);
    setLoading(true); // Show loading spinner

    try {
      const response = await axios.post('http://localhost:8000/predict', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      
      
      console.log("API Response:", response.data);
      setResult(response.data); // Store API result
      setCurrentStep("result"); // Navigate to result page
    } catch (error) {
      console.error("Error uploading the file:", error);
      alert("Failed to get prediction. Please try again.");
    } finally {
      setLoading(false); // Hide loading spinner
    }
  };

  const handleReset = () => {
    setCurrentStep("upload");
    setSelectedFile(null);
    setResult(null);
  };

  return (
    <div className="App">
      <Navbar onReset={handleReset} />
      {currentStep === "upload" && (
        <ImageUpload
          onFileChange={handleFileChange}
          onSubmit={handleSubmit}
          loading={loading}
        />
      )}
      {currentStep === "result" && (
        <Result
          data={result}
          imageFile={selectedFile}
          onReset={handleReset}
        />
      )}
    </div>
  );
};

export default App;
