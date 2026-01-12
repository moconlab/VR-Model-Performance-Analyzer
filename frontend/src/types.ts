export interface Mesh {
  name: string;
  triangle_count: number;
  instanced: boolean;
}

export interface MaterialInfo {
  name: string;
  transparent: boolean;
  texture_resolution: number;
}

export interface SceneDetails {
  meshes: Mesh[];
  materials: MaterialInfo[];
  object_count: number;
  lod_count: number;
  warnings?: string[];
}

export interface AnalysisResult {
  file: string;
  fps_estimate: number;
  overall_score: number;
  status: string;
  details: SceneDetails;
}
