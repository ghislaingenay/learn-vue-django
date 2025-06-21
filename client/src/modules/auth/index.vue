<script lang="ts" setup>
import { computed } from "vue";
import AuthLayout from "./AuthLayout.vue";
import LoginForm from "./components/LoginForm.vue";
import RegisterForm from "./components/RegisterForm.vue";
import { useRoute, useRouter } from "vue-router";

const route = useRoute();
const router = useRouter();

const mode = computed(() => {
  const path = route.path.replace("/", "");
  return path || "login"; // default to login if empty
});

// defensive programming to ensure mode is always valid
const isValidRoute = computed(() => ["login", "register"].includes(mode.value));
if (!isValidRoute.value) {
  router.replace("/login");
}
</script>
<template>
  <!-- <div v-if="!isValidRoute">
    <h1>Invalid Route</h1>
    <p>The route "{{ route.path }}" is not valid.</p>
  </div> -->
  <AuthLayout>
    <LoginForm v-if="mode === 'login'" />
    <RegisterForm v-else />
    <!-- Include your login form component here -->
  </AuthLayout>
</template>
<style scoped></style>
