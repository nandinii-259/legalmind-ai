import { useState } from "react";
import ReactMarkdown from "react-markdown";
import { askQuestion } from "../services/api";
import "../styles/chat.css";

function ChatBox() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [sources, setSources] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleAskQuestion = async () => {
    if (!question.trim()) return;

    setLoading(true);
    setAnswer("");
    setSources([]);

    try {
      const response = await askQuestion(question);

      setAnswer(response.data.answer);
      setSources(response.data.sources || []);
    } catch (error) {
      console.error(error);

      setAnswer(
        "Sorry, I couldn't generate an answer because the AI service is currently unavailable or its quota has been exceeded."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="chat-card">
      <h2 className="chat-title">💬 Ask AI</h2>

      <p className="chat-subtitle">
        Ask questions about your uploaded document.
      </p>

      <textarea
        className="chat-textarea"
        placeholder="Example: What projects has the candidate completed?"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />

    <button
      className="ask-button"
      onClick={handleAskQuestion}
      disabled={loading}
    >
    {loading ? (
      <div className="loading-content">
        <div className="spinner"></div>
      Thinking...
    </div>
  ) : (
    "Ask AI"
  )}
</button>

      {answer && (
        <div className="answer-card">
          <h3 className="answer-title">🤖 AI Answer</h3>

          <div className="answer-content">
            <ReactMarkdown>{answer}</ReactMarkdown>
          </div>

          {sources.length > 0 && (
            <div className="sources-section">
              <h4 className="sources-title">
                📄 Sources
              </h4>

              {sources.map((source, index) => (
                <div
                  key={index}
                  className="source-card"
                >
                  <div className="source-document">
                    {source.document}
                  </div>

                  <div className="source-chunk">
                    Chunk #{source.chunk}
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default ChatBox;