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
      baseUrl: "auth",
    });
  }
  private getAccessToken() {
    const accessToken = localStorage.getItem("access_token");
    if (!accessToken) return null;
    return accessToken;
  }

  async isAuthenticated(): Promise<boolean> {
    await this.requestNewAccessToken();
    const accessToken = this.getAccessToken();
    if (accessToken === null) return false;

    try {
      const response = await this._axios.get("/users/me/", {
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

  private getAccessTokenExpirationDate(): Date | null {
    const isValidToken = this.isValidToken();
    if (!isValidToken) return null;
    const accessToken = localStorage.getItem("access_token");
    if (!accessToken) return null;
    const decodedToken = jwtDecode<{ exp: number }>(accessToken);
    return decodedToken.exp ? new Date(decodedToken.exp * 1000) : null;
  }

  async requestNewAccessToken(
    timeMinBeforeExpiration: number = 5
  ): Promise<boolean> {
    const expirationDate = this.getAccessTokenExpirationDate();
    if (!expirationDate) {
      localStorage.removeItem("access_token");
      return false;
    }

    const currentTime = Date.now();
    const timeToExpiration = expirationDate.getTime() - currentTime;

    const needsRefresh =
      timeToExpiration < timeMinBeforeExpiration * 60 * 1000 ||
      timeToExpiration <= 0;
    if (needsRefresh) {
      await this.refreshToken();
      return true;
    }

    return false;
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
    const response = await this._axios.post("/jwt/refresh/", {
      refresh: localStorage.getItem("refresh_token"),
    });
    localStorage.setItem("access_token", response.data.access);
    return response.data;
  }

  async register(body: {
    data: { type: "User"; attributes: UserRegistration };
  }): Promise<void> {
    const res = await this._axios.post("/users/", body).catch(() => null);
    return res?.data ?? null;
  }

  async login(email: string, password: string): Promise<void> {
    const response = await this._axios.post("/jwt/create/", {
      email,
      password,
    });
    localStorage.setItem("access_token", response.data.access);
    localStorage.setItem("refresh_token", response.data.refresh);
  }
  async logout(): Promise<void> {
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
  }
}

const authService = new AuthService();
export { authService };
