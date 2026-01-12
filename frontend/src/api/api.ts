import axios from "axios";

export const analyzeModel = async (file: File, device: string) => {
  const formData = new FormData();
  formData.append("file", file);

  const response = await axios.post(
    `http://localhost:8000/analyze/${device}`,
    formData,
    { headers: { "Content-Type": "multipart/form-data" } }
  );
  return response.data;
};
