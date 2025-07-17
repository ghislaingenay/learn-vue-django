<script lang="ts" setup>
import { defineProps } from "vue";
import LoginForm from "./components/LoginForm.vue";
import RegisterForm from "./components/RegisterForm.vue";
import type { AuthMode } from "@types";
const { mode } = defineProps<{
  mode: AuthMode;
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
