<script lang="ts" setup>
import type { FormTemplate, FormTemplateValues } from "@types";
import { computed, reactive, ref, watch } from "vue";
import { useRoute } from "vue-router";

import { defineProps } from "vue";


const emit = defineEmits<{
  (e: "on-created", formData: FormTemplate): void;
  (e: "on-updated", id: number,formData: FormTemplate): void;
}>();

const formItems = [{
  name: "name",
  label: "Name",
  model: "name",
  children: {
    type: 'text'
  }
}, {
  name: "description",
  label: "Description",
  model: "description",
  children: {
    type: 'textarea'
  }
}, {
  name: "status",
  label: "Status",
  model: "status",
  children: {
    type: 'select',
    options: [
      { value: 'active', text: 'Active' },
      { value: 'inactive', text: 'Inactive' }
    ]
  }
}]

const { form } = defineProps<{
  form?: FormTemplateValues;
}>();

let formData = reactive<FormTemplateValues>({
  name: "",
  description: "",
  status: "active",
});

const route = useRoute();
const formTemplateId = route.params.id as string;

const isEdit = computed(() => {
  return formTemplateId && form !== undefined;
});

const handleForm = async() => {}

watch(
  () => form,
  (newForm) => {
    if (!newForm) return;
    formData = { ...newForm };
  },
  { immediate: true }
);
</script>

<template>
  <h2>{{ isEdit ? "Edit Form Template" : "Create Form Template" }}</h2>
  <form @submit.prevent="submitForm">
    <div>
      <label for="name">Name:</label>
</template>

<style scoped></style>
