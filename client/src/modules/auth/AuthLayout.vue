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
  <main class="bg-slate-50 w-screen h-screen overflow-hidden auth-background">
    <div class="flex items-center justify-center w-full h-full">
      <section class="auth-card border-2">
        <div v-if="mode === 'login'">
          <LoginForm />
        </div>
        <div v-else>
          <RegisterForm />
        </div>
      </section>
    </div>
  </main>
</template>
<style scoped>
.auth-card {
  width: 400px;
  min-height: 300px;
  padding: 20px;
  margin: auto;
  background-color: aliceblue;
  border-radius: 8px;
  opacity: 0.9;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.auth-background {
  background: linear-gradient(
    135deg,
    #003f5b,
    #2b4b7d,
    #5f5195,
    #98509d,
    #cc4c91,
    #f25375,
    #ff6f4e,
    #ff9913
  );
}
</style>
