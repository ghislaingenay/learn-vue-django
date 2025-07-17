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
    .catch((err: VineErrorResponse) => {
      if (err.errors) {
        err.errors.forEach((error) => {
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

const validateField = (field: keyof UserLogin) => {
  return vine
    .validate({
      schema: loginValidatorObject,
      data: { [field]: loginDetails[field] },
    })
    .then(() => {
      errors[field] = "";
      return true;
    })
    .catch((err: VineErrorResponse) => {
      if (err.errors) {
        err.errors.forEach((error) => {
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
  isLoading.value = true;
  if (!validatedData) return;

  try {
    // Simulate an API call
    await authService.login(loginDetails.email, loginDetails.password);
  } catch (error) {
    console.error("Login failed:", error);
  } finally {
    isLoading.value = false;
  }
};
</script>
<template>
  <section class="">
    <div class="auth-card">
      <h1>Login form</h1>
      <form novalidate @submit.prevent="handleLogin()">
        <v-text-field
          label="Email"
          variant="underlined"
          v-model="loginDetails.email"
          @blur="validateField('email')"
        ></v-text-field>

        <!-- <input
          type="email"
          name="email"
          v-model="loginDetails.email"
          placeholder="Email"
          required
          @blur="validateField('email')"
        /> -->
        <input
          type="password"
          name="password"
          v-model.trim="loginDetails.password"
          placeholder="Password"
          required
          @blur="validateField('password')"
        />
      </form>
    </div>
  </section>
</template>
<style scoped>
.h1 {
  color: #333;
  font-size: 24px;
  text-align: center;
}

.auth-card {
  width: 400px;
  height: 300px;
  padding: 20px;
  background-color: aliceblue;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

section {
  display: grid;
  place-self: center;
  background-color: #4311cb;
}
</style>
