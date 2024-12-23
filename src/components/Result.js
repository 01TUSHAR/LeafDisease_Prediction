import React, { useEffect, useState } from "react";
import "./Result.css";

const Result = ({ data, imageFile, onReset }) => {
  const [diseaseDetected, setDiseaseDetected] = useState(null);

  // Update diseaseDetected when API response data is available
  useEffect(() => {
    if (data) {
      console.log("Data Received in Result.js:", data);
      setDiseaseDetected(data.predicted_class);
    }
  }, [data]);

  // Return if no data is available yet
  if (!data) return <p>No data available</p>;

  // Display an error if the API response contains an error
  if (data.error) return <p>Error: {data.error}</p>;

  return (
    <div className="image-disease-analyzer">
      {/* Main Content */}
      <main className="ida-content">
        {/* Prediction, Image Preview, and Insights Section */}
        <div className="ida-prediction-insights-container">
          {/* Predicted Disease Section */}
          <section className="ida-prediction">
            <h2>Predicted Disease: {diseaseDetected || "Processing..."}</h2>
            {imageFile && (
              <img
                src={URL.createObjectURL(imageFile)}
                alt={data.predicted_class}
                className="ida-image"
              />
            )}
          </section>

          {/* Disease Insights Section */}
          <section className="ida-disease-insights">
            <h3>Disease Insights</h3>
            <p>
              <strong>Name:</strong> {diseaseDetected || "Unknown"}
            </p>
            <p>
              <strong>Description:</strong>{" "}
              {data.description || "No description available."}
            </p>
            <p>
              <strong>Causes:</strong> {data.cause || "Not provided."}
            </p>
            <p>
              <strong>Symptoms:</strong> {data.symptoms || "Not provided."}
            </p>
          </section>
        </div>

        {/* Prevention and Cure Section */}
        <section className="ida-prevention">
          <h3>Prevention and Cure</h3>
          <table className="ida-table">
            <thead>
              <tr>
                <th>Aspect</th>
                <th>Details</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Prevention</td>
                <td>{data.pre_management || "N/A"}</td>
              </tr>
              <tr>
                <td>Treatment</td>
                <td>{data.mid_management || "N/A"}</td>
              </tr>
              <tr>
                <td>Future Management</td>
                <td>{data.future_management || "N/A"}</td>
              </tr>
              <tr>
                <td>Precautions</td>
                <td>{data.precautions || "N/A"}</td>
              </tr>
            </tbody>
          </table>
        </section>
      </main>

      {/* Footer */}
      <footer className="ida-footer">
        <p>© 2023 Sugarcane Disease Prediction System. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default Result;
