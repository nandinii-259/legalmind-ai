import Layout from "../components/Layout";
import UploadCard from "../components/UploadCard";
import ChatBox from "../components/ChatBox";
import Sidebar from "../components/Sidebar";

function Home() {
  return (
    <Layout>
      <div className="header">
        <h1 className="title">🧠 LegalMind AI</h1>

        <p className="subtitle">
          AI-powered Legal Document Assistant
        </p>

        <p className="description">
          Upload legal documents, ask questions in natural language,
          and receive AI-powered answers with source citations.
        </p>
      </div>

      <div className="home-layout">
        <div className="left-panel">
          <Sidebar />
        </div>

        <div className="right-panel">
          <UploadCard />

          <ChatBox />
        </div>
      </div>
    </Layout>
  );
}

export default Home;