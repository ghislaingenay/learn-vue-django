<script lang="ts" setup>
import { authService } from "@services/auth";
import { type UserRegistration, type VineErrorResponse } from "@types";
import {
  loginValidatorObject,
  registerValidatorObject,
} from "@validators/auth";
import vine from "@vinejs/vine";
import { reactive, ref } from "vue";

const isLoading = ref(false);

const registerDetails = reactive<UserRegistration>({
  email: "",
  password: "",
  first_name: "",
  last_name: "",
});

const errors = reactive<UserRegistration>({
  email: "",
  password: "",
  first_name: "",
  last_name: "",
});
const resetErrors = () => {
  for (const key of Object.keys(errors))
    errors[key as keyof typeof errors] = "";
};

const registerInputList = [
  { label: "Email", model: "email", type: "email" },
  { label: "Password", model: "password", type: "password" },
  { label: "First Name", model: "first_name", type: "text" },
  { label: "Last Name", model: "last_name", type: "text" },
];

const validateRegisterDetails = async () => {
  return await vine
    .validate({ schema: registerValidatorObject, data: registerDetails })
    .catch((err: VineErrorResponse<UserRegistration>) => {
      if (err.messages) {
        err.messages.forEach((error) => {
          errors[error.field] = error.message;
        });
      }
      return null;
    });
};

const validateField = async (field: keyof UserRegistration) => {
  return await vine
    .validate({
      schema: loginValidatorObject,
      data: { [field]: registerDetails[field] },
    })
    .catch((err: VineErrorResponse<UserRegistration>) => {
      errors[field] = "";
      if (err.messages) {
        err.messages.forEach((error) => {
          if (error.field === field) {
            errors[field] = error.message;
          }
        });
      }
      return false;
    });
};

const handleRegister = async () => {
  resetErrors();

  const validatedData = await validateRegisterDetails();
  if (validatedData === null) return;
  isLoading.value = true;

  try {
    const res = await authService.register({
      data: {
        type: "User",
        attributes: registerDetails,
      },
    });
  } catch (error) {
    console.error("Login failed:", error);
  } finally {
    isLoading.value = false;
  }
};
</script>
<template>
  <div class="grid gap-8">
    <h1 class="text-center pt-4">Google Form</h1>
    <router-link
      class="text-center underline text-blue-500 font-[0.5rem]"
      to="/login"
    >
      Have an account? Login
    </router-link>
    <form novalidate @submit.prevent="handleRegister()">
      <div class="grid gap-8 mb-4" v-for="input of registerInputList">
        <v-text-field
          :label="input.label"
          variant="underlined"
          :type="input.type"
          :error="!!errors[input.model as keyof typeof errors]"
          :error-messages="errors[input.model as keyof typeof errors]"
          v-model="registerDetails[input.model as keyof UserRegistration]"
          @blur="
            async () =>
              await validateField(input.model as keyof UserRegistration)
          "
        ></v-text-field>
      </div>
      <v-btn :loading="isLoading" type="submit">Register</v-btn>
    </form>
  </div>
</template>
<style scoped></style>
