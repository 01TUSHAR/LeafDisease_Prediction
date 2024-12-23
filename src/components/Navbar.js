import React from "react";
import "./Navbar.css";

function Navbar({ onReset }) {
  const handleResetClick = (event) => {
    event.preventDefault(); // Prevent default link behavior
    onReset();
  };

  return (
    <header className="header">
      <h1>Sugarcane Disease Prediction</h1>
      <nav>
        <a href="#home" onClick={handleResetClick}>
          Home
        </a>
        <a href="#results">Results</a>
        <a href="#about">About Us</a>
      </nav>
    </header>
  );
}

export default Navbar;
