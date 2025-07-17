export default class Env {
  static BACKEND_ENDPOINT =
    import.meta.env.VITE_BACK_ENDPOINT || "http://localhost:8000";
  static API_VERSION = "v1";
  static API_BASE_URL = `${Env.BACKEND_ENDPOINT}${Env.API_VERSION}/`;
  static getApiUrl(endpoint: string = ""): string {
    return `${Env.API_BASE_URL}${endpoint}`;
  }
}
