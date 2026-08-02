import "../styles/layout.css";

function Layout({ children }) {
  return (
    <div className="page">
      <div className="container">
        {children}

        <footer className="footer">
          Built with React • FastAPI • Gemini • ChromaDB • SQLite
        </footer>
      </div>
    </div>
  );
}

export default Layout;