import type { FormTemplate } from "@types";
import BaseService from "./base";

export default class FormTemplateService extends BaseService {
  constructor() {
    super({
      baseUrl: "forms/templates",
    });
  }

  async findAll() {
    const res = await this._axios.get("/");
    return res.data as FormTemplate[];
  }
}
