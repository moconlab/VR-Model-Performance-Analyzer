import axios from "axios";
import { AnalysisResult } from "../types";

const BASE_URL = "http://localhost:8000";

export const analyzeModel = async (file: File, device: string): Promise<AnalysisResult> => {
  const formData = new FormData();
  formData.append("file", file);
  const response = await axios.post(`${BASE_URL}/analyze/${device}`, formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });
  return response.data;
};

export const uploadGPUProfile = async (profile: any) => {
  await axios.post(`${BASE_URL}/upload_gpu_profile`, profile);
};
