import React from "react";
import "./App.css";

function App() {
  return (
    <div className="container">
      <h1>📡 WiFi Scanner</h1>
      <p className="version">Version 2.0</p>

      <div className="card">
        <p>
          This is a simple UI for the WiFi Scanner project.
        </p>
        <p>
          Click the button below to scan WiFi networks using the Python backend.
        </p>

        <button onClick={() => alert("Run scanner.py from backend folder")}>
          Scan WiFi
        </button>
      </div>
    </div>
  );
}

export default App;
