<script setup lang="ts">
import { RouterLink } from "vue-router";
</script>

<template>
  <div class="not-found">
    <h1>404 - Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
    <RouterLink to="/">Go back to Home</RouterLink>
  </div>
</template>

<style scoped>
.not-found {
  text-align: center;
  margin-top: 50px;
}
.not-found h1 {
  font-size: 2em;
  color: #ff0000;
}
.not-found p {
  font-size: 1.2em;
  color: #333;
}
</style>
<script setup lang="ts"></script>
