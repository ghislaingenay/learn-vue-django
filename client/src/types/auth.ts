import type {
  loginValidator,
  registerValidator,
  resetPasswordValidator,
} from "@validators/auth";
import type { Infer } from "@vinejs/vine/types";

export type UserRegistration = Infer<typeof registerValidator>;
export type UserLogin = Infer<typeof loginValidator>;
export type ResetPassword = Infer<typeof resetPasswordValidator>;
