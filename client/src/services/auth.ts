import Env from "@definitions/env";
import type { UserRegistration } from "@types";
import axios from "axios";
import BaseService from "./base";
import ERROR_CODES from "@constants/error_code";

export default class AuthService extends BaseService {
  constructor() {
    super({
      baseUrl: "/auth",
    });
  }

  static async isAuthenticated(): Promise<boolean> {
    const accessToken = localStorage.getItem("access_token");
    if (!accessToken) return false;

    try {
      const response = await axios.get(Env.getApiUrl("auth/users/me"), {
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
      });
      return response.status === 200;
    } catch (error) {
      console.error("Authentication check failed:", error);
      return false;
    }
  }

  async refreshToken(): Promise<void> {
    const accessToken = localStorage.getItem("access_token");
    if (!accessToken) throw new Error(ERROR_CODES.E_ACCESS_TOKEN_NOT_FOUND);
  }

  async register(body: UserRegistration): Promise<void> {
    return await this._axios.post("/users", body).then(() => {});
  }

  async login(email: string, password: string): Promise<void> {
    const response = await this._axios.post("/jwt/create", { email, password });
    localStorage.setItem("access_token", response.data.access_token);
  }
  async logout(): Promise<void> {
    localStorage.removeItem("access_token");
  }
}

const authService = new AuthService();
export { authService };
