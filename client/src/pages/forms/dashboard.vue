<script lang="ts" setup>
import FormList from "@modules/forms/FormList.vue";
import type { FormTemplate } from "@types";
import { reactive, ref, provide, watch } from "vue";

const isLoading = ref(false);
const forms = reactive<FormTemplate[]>([]);

const loadForms = async () => {
  isLoading.value = true;
  try {
    // Logic to load forms can be added here
  } catch (error) {
    console.error("Error loading forms:", error);
  } finally {
    isLoading.value = false;
  }
};

watch(forms, (newVal) => {
  provide("form-list", newVal);
});
</script>
<template>
  <h2>Form List</h2>
  <div v-if="isLoading" class="loading">
    <p>Loading forms...</p>
  </div>
  <div v-else-if="forms.length === 0" class="no-forms">
    <p>No forms available.</p>
  </div>
  <div v-else class="form-list">
    <FormList :forms="forms" />
  </div>
</template>

<style scoped></style>
