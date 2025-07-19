<script setup lang="ts">
import { FormTemplateStatus, type FormTemplate } from "@types";
import { h, inject } from "vue";
const forms = inject<FormTemplate[]>("form-list", []);

const headers = [
  {
    label: "ID",
    key: "id",
  },
  { label: "Name", key: "name" },
  {
    label: "Status",
    key: "status",
    render: (status: FormTemplateStatus) => {
      if (status === FormTemplateStatus.ACTIVE)
        return h("v-chip", { color: "green" }, "Active");

      if (status === FormTemplateStatus.INACTIVE)
        return h("v-chip", { color: "red" }, "Inactive");
      return h("v-chip", { color: "yellow" }, "Deleted");
    },
  },
];
</script>

<template>
  <div class="form-list">
    <v-table striped="even">
      <thead>
        <tr>
          <th v-for="header in headers" :key="header.key" class="text-left">
            {{ header.label }}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(form, index) in forms" :key="form.id">
          <td v-if="headers[index].render">
            <component
              :is="headers[index].render(form[headers[index].key as keyof typeof form] as any)"
            />
          </td>
          <td v-else>
            {{ form[headers[index].key as keyof typeof form] }}
          </td>
        </tr>
      </tbody>
    </v-table>
    <section v-for="form of forms"></section>
    <!-- Add your form list logic here -->
  </div>
</template>
