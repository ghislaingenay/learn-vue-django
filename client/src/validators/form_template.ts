import vine from "@vinejs/vine";

export const createEditFormTemplateValidatorObject = vine.object({
  name: vine.string().minLength(3).maxLength(80),
  description: vine.string(),
  status: vine.enum(["active", "inactive", "deleted"]),
});

export const createEditFormTemplateValidator = vine.compile(
  createEditFormTemplateValidatorObject
);
