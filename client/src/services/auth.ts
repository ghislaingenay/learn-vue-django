import Env from "@definitions/env";
import type { UserRegistration } from "@types";
import axios from "axios";
import BaseService from "./base";
import ERROR_CODES from "@constants/error_code";
import { JWT_REGEX } from "@constants/regex";
import { jwtDecode } from "jwt-decode";

export default class AuthService extends BaseService {
  constructor() {
    super({
      baseUrl: "/auth",
    });
  }

  async isAuthenticated(): Promise<boolean> {
    await this.requestNewAccessToken(); // Ensure token is refreshed if needed
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

  private getExpirationDate(): Date | null {
    const isValidToken = this.isValidToken();
    if (!isValidToken) return null;
    const accessToken = localStorage.getItem("access_token");
    if (!accessToken) return null;
    const decodedToken = jwtDecode<{ exp: number }>(accessToken);
    return decodedToken.exp ? new Date(decodedToken.exp * 1000) : null;
  }

  async requestNewAccessToken(
    timeMinBeforeExpiration: number = 5
  ): Promise<void> {
    const expirationDate = this.getExpirationDate();
    if (!expirationDate) {
      localStorage.removeItem("access_token");
      return; // Token is invalid or not found
    }

    const currentTime = Date.now();
    const timeToExpiration = expirationDate.getTime() - currentTime;

    const needsRefresh =
      timeToExpiration < timeMinBeforeExpiration * 60 * 1000 ||
      timeToExpiration <= 0;
    if (needsRefresh) {
      await this.refreshToken();
      return;
    }

    return; // Token is still valid
  }

  private isValidToken(): boolean {
    const accessToken = localStorage.getItem("access_token");
    if (!accessToken) return false;
    if (!JWT_REGEX.test(accessToken)) return false;
    return jwtDecode<{ exp: number }>(accessToken).exp > Date.now() / 1000;
  }

  async refreshToken(): Promise<void> {
    const accessToken = localStorage.getItem("access_token");
    if (!accessToken) throw new Error(ERROR_CODES.E_ACCESS_TOKEN_NOT_FOUND);
    const response = await this._axios.post("/jwt/refresh", {
      access: accessToken,
    });
    localStorage.setItem("access_token", response.data.access_token);
    return response.data;
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
