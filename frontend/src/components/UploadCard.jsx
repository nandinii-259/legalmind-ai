import { useRef, useState } from "react";
import { uploadPDF } from "../services/api";
import "../styles/upload.css";

function UploadCard() {
  const fileInputRef = useRef(null);

  const [message, setMessage] = useState("");
  const [selectedFile, setSelectedFile] = useState("No file selected");

  const handleButtonClick = () => {
    fileInputRef.current.click();
  };

  const handleFileChange = async (event) => {
    const file = event.target.files[0];

    if (!file) return;

    setSelectedFile(file.name);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await uploadPDF(formData);
      setMessage(response.data.message);
    } catch (error) {
      console.error(error);
      setMessage("Upload failed.");
    }
  };

  return (
    <div className="upload-card">
      <h2 className="upload-title">📄 Upload PDF</h2>

      <p className="upload-description">
        Upload a legal document to build your AI knowledge base.
      </p>

      <div className="upload-area">
        <div className="file-name">
          📁 {selectedFile}
        </div>

        <input
          type="file"
          accept=".pdf"
          ref={fileInputRef}
          style={{ display: "none" }}
          onChange={handleFileChange}
        />

        <button
          className="upload-button"
          onClick={handleButtonClick}
        >
          Choose PDF
        </button>
      </div>

{message && (
  <div className="upload-success">
    <strong>✅ Upload Successful</strong>

    <br />

    {selectedFile}

    <br />

    Your document is now ready for AI-powered questions.
  </div>
)}

      <div className="upload-footer">
        Supported format: PDF (.pdf)
      </div>
    </div>
  );
}

export default UploadCard;