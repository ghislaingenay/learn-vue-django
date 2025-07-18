<script lang="ts" setup>
import { authService } from "@services/auth";
import type { UserLogin, VineErrorResponse } from "@types";
import { loginValidatorObject } from "@validators/auth";
import vine from "@vinejs/vine";
import { reactive, ref } from "vue";

const isLoading = ref(false);

const loginDetails = reactive({
  email: "",
  password: "",
});

const validateLoginDetails = async () => {
  return await vine
    .validate({ schema: loginValidatorObject, data: loginDetails })
    .catch((err: VineErrorResponse<UserLogin>) => {
      if (err.messages) {
        err.messages.forEach((error) => {
          if (error.field === "email") {
            errors.email = error.message;
          } else if (error.field === "password") {
            errors.password = error.message;
          }
        });
      }
      return null;
    });
};

const validateField = async (field: keyof UserLogin) => {
  return await vine
    .validate({
      schema: loginValidatorObject,
      data: { [field]: loginDetails[field] },
    })
    .then(() => {
      errors[field] = "";
      return true;
    })
    .catch((err: VineErrorResponse<UserLogin>) => {
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

const errors = reactive({
  email: "",
  password: "",
});
const handleLogin = async () => {
  errors.email = "";
  errors.password = "";

  const validatedData = await validateLoginDetails();
  if (!validatedData) return;
  isLoading.value = true;

  try {
    // Simulate an API call
    isLoading.value = true;
    await authService.login(loginDetails.email, loginDetails.password);
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
      to="/auth/register"
    >
      Don't have an account? Register
    </router-link>
    <form novalidate @submit.prevent="handleLogin()">
      <div class="grid gap-8">
        <v-text-field
          label="Email"
          variant="underlined"
          :error="!!errors.email"
          :error-messages="errors.email"
          v-model="loginDetails.email"
          @blur="async () => await validateField('email')"
        ></v-text-field>
        <v-text-field
          label="Password"
          variant="underlined"
          :error="!!errors.password"
          :error-messages="errors.password"
          v-model="loginDetails.password"
          @blur="async () => await validateField('password')"
        ></v-text-field>

        <v-btn :loading="isLoading" type="submit"> Login </v-btn>
      </div>
    </form>
  </div>
</template>
<style scoped></style>
