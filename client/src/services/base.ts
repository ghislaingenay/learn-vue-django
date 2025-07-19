import Env from "@definitions/env";
import axios from "axios";

type APIServiceName = "gateway";

type APIBaseContructor = {
  service?: APIServiceName;
  baseUrl?: string;
};
export default class BaseService {
  protected _axios;

  constructor({ service = "gateway", baseUrl = "" }: APIBaseContructor = {}) {
    if (service !== "gateway") {
      throw new Error("Invalid service name. Only 'gateway' is supported.");
    }

    if (baseUrl.startsWith("/")) baseUrl = baseUrl.substring(1);

    this._axios = axios.create({
      baseURL: Env.getApiUrl(baseUrl),
      headers: {
        "Content-Type": "application/json",
        Authorization: "Bearer " + localStorage.getItem("access_token"),
      },
    });
  }
}
