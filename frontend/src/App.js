import './App.css';
import axios from 'axios';
import { useState } from 'react';

import { CircularProgressbar } from 'react-circular-progressbar';
import 'react-circular-progressbar/dist/styles.css';

function App() {

  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const uploadFile = async () => {

    if (!file) {
      alert("Please select a file");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {

      setLoading(true);

      const response = await axios.post(
        "https://veriproof-ai.onrender.com/analyze",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      setResult(response.data);

    } catch (error) {

      console.log(error);
      alert("Upload failed");

    } finally {

      setLoading(false);

    }
  };

  return (

    <div className="app">

      <nav className="navbar">

        <div className="logo">
          VeriProof AI
        </div>

        <div className="nav-links">
          <span>Dashboard</span>
          <span>AI Engine</span>
          <span>Reports</span>
        </div>

      </nav>

      <div className="hero">

        <h1>VeriProof AI</h1>

        <p>
          Advanced Academic Authenticity Validation System
        </p>

      </div>

      <div className="upload-box">

        <div className="scan-line"></div>

        <h2>Upload Academic Document</h2>

        <input
          type="file"
          className="file-input"
          onChange={(e) => setFile(e.target.files[0])}
        />

        <br />

        <button
          className="analyze-btn"
          onClick={uploadFile}
        >
          {loading ? "Analyzing with AI..." : "Analyze Document"}
        </button>

      </div>

      {

        result && (

          <div className="results">

            <div className="score-card">

              <h2>Authenticity Score</h2>

              <div className="circle-wrapper">

                <CircularProgressbar
                  value={result.originality_score}
                  text={`${result.originality_score}%`}
                />

              </div>

              <p>
                AI Semantic Analysis Completed
              </p>

            </div>

            <div className="score-card">

              <h2>Detected Similarities</h2>

              {

                result.plagiarism_details.map((item, index) => (

                  <div className="match-card" key={index}>

                    <p>
                      <strong>Uploaded:</strong>
                      {" "}
                      {item.uploaded_sentence}
                    </p>

                    <p>
                      <strong>Matched:</strong>
                      {" "}
                      {item.matched_sentence}
                    </p>

                    <p>
                      <strong>Similarity:</strong>
                      {" "}
                      {item.similarity_score}%
                    </p>

                  </div>

                ))

              }

            </div>

          </div>

        )

      }

      <div className="features">

        <div className="feature-card">
          <h3>98.7%</h3>
          <p>Detection Accuracy</p>
        </div>

        <div className="feature-card">
          <h3>3+</h3>
          <p>Supported File Formats</p>
        </div>

        <div className="feature-card">
          <h3>AI NLP</h3>
          <p>Semantic Similarity Engine</p>
        </div>

        <div className="feature-card">
          <h3>Real-Time</h3>
          <p>Academic Validation</p>
        </div>

      </div>

    </div>

  );
}

export default App;
