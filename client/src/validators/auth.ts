import vine from "@vinejs/vine";

export const registerValidator = vine.compile(
  vine.object({
    email: vine.string().email(),
    password: vine.string().minLength(6),
    first_name: vine.string().minLength(2).maxLength(50),
    lastName: vine.string().minLength(2).maxLength(50),
  })
);
export const loginValidator = vine.compile(
  vine.object({
    email: vine.string().email(),
    password: vine.string().minLength(6),
  })
);
export const resetPasswordValidator = vine.compile(
  vine.object({
    email: vine.string().email(),
  })
);
export const changePasswordValidator = vine.compile(
  vine.object({
    oldPassword: vine.string().minLength(6),
    newPassword: vine.string().minLength(6),
  })
);
