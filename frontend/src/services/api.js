import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});

export const uploadPDF = (formData) => {
  return api.post("/upload/", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });
};

export const askQuestion = (question) => {
  return api.post("/chat/", {
    question,
  });
};

export const getHistory = () => {
  return api.get("/history/");
};

export const clearHistory = () => {
  return api.delete("/history/");
};

export default api;