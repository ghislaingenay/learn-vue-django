<script lang="ts" setup>
import { defineProps } from "vue";
import LoginForm from "./components/LoginForm.vue";
import RegisterForm from "./components/RegisterForm.vue";
const { mode } = defineProps<{
  mode: "login" | "register";
}>();
</script>
<template>
  <div>
    <h1>layout logic</h1>
    <div v-if="mode === 'login'">
      <LoginForm />
    </div>
    <div v-else>
      <RegisterForm />
    </div>
  </div>
</template>
<style scoped></style>
