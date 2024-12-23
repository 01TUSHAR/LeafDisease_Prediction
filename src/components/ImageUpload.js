// import React, { useState } from "react";
// import "./ImageUpload.css";

// function ImageUpload({ onFileChange, onSubmit, loading, onReset }) {
//   const [image, setImage] = useState(null);

//   const handleImageChange = (event) => {
//     const file = event.target.files[0];
//     if (file) {
//       const imageUrl = URL.createObjectURL(file);
//       setImage(imageUrl);
//       onFileChange(file);
//       console.log("Image Selected in ImageUpload:", file); // Debugging log
//     }
//   };

//   const handleReset = () => {
//     // Reset the image preview and trigger the onReset function
//     setImage(null);
//     onReset();
//   };

//   return (
//     <div>
//       {/* Header with Navbar */}
//       <header className="header">
//         <h1>Sugarcane Disease Prediction and Management</h1>
//         <nav>
//           {/* Home button as a reset button */}
//           <a href="#home" onClick={handleReset}>
//             Reset
//           </a>
//           <a href="#results">Results</a>
//           <a href="#about">About Us</a>
//         </nav>
//       </header>

//       {/* Main Content */}
//       <div className="image-upload-container">
//         <div className="upload-box">
//           <h2>Upload your Image</h2>

//           {/* Image Preview */}
//           <div className="image-preview">
//             {image ? (
//               <img src={image} alt="Preview" className="preview-image" />
//             ) : (
//               <p className="placeholder-text">No image uploaded</p>
//             )}
//           </div>

//           {/* File Input */}
//           <input
//             type="file"
//             accept="image/*"
//             onChange={handleImageChange}
//             className="file-input"
//             disabled={loading}
//           />

//           {/* Submit Button */}
//           <button
//             className="upload-button"
//             onClick={onSubmit}
//             disabled={!image || loading}
//           >
//             {loading ? "Processing..." : "Process Image for Disease Prediction"}
//           </button>
//         </div>
//       </div>
//     </div>
//   );
// }

// export default ImageUpload;

import React, { useState } from "react";
import "./ImageUpload.css";

function ImageUpload({ onFileChange, onSubmit, loading, error }) {
  const [image, setImage] = useState(null);

  const handleImageChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      if (file.size > 5 * 1024 * 1024) { // 5MB limit
        alert("File is too large. Max size is 5MB.");
        return;
      }
      setImage(URL.createObjectURL(file));
      onFileChange(file);
    }
  };

  return (
    <div className="image-upload-container">
      <div className="upload-box">
        <h2>Upload your Image</h2>
        <div className="image-preview">
          {image ? (
            <img src={image} alt="Preview" className="preview-image" />
          ) : (
            <p className="placeholder-text">No image uploaded</p>
          )}
        </div>

        <input
          type="file"
          accept="image/*"
          onChange={handleImageChange}
          className="file-input"
          disabled={loading}
        />

        <button
          className="upload-button"
          onClick={onSubmit}
          disabled={!image || loading}
        >
          {loading ? "Processing..." : "Process Image for Disease Prediction"}
        </button>
        {error && <p className="error-message">{error}</p>}
      </div>
    </div>
  );
}

export default ImageUpload;
