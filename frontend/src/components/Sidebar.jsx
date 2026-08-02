import { useEffect, useState } from "react";
import { getHistory, clearHistory } from "../services/api";
import "../styles/sidebar.css";

function Sidebar() {
  const [history, setHistory] = useState([]);

  const loadHistory = async () => {
    try {
      const response = await getHistory();
      setHistory(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  const handleClearHistory = async () => {
    try {
      await clearHistory();
      setHistory([]);
    } catch (error) {
      console.error(error);
    }
  };

  useEffect(() => {
    loadHistory();
  }, []);

  return (
    <div className="sidebar">
      <h2 className="sidebar-title">📚 Chat History</h2>

      <p className="sidebar-subtitle">
        Your previous questions
      </p>

      <div className="history-list">
        {history.length === 0 ? (
          <div className="empty-history">
            <div className="empty-history-icon">💬</div>

            <p>No conversations yet.</p>

            <small>
              Upload a PDF and ask your first question.
            </small>
          </div>
        ) : (
          history.map((item) => (
            <div
              key={item.id}
              className="history-item"
            >
              <div className="history-question">
                {item.question}
              </div>
            </div>
          ))
        )}
      </div>

      <button
        className="clear-button"
        onClick={handleClearHistory}
      >
        🗑 Clear History
      </button>
    </div>
  );
}

export default Sidebar;