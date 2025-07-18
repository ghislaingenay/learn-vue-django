import routing from "@constants/router_names";
import type { RouteRecordRaw } from "vue-router";

const appRoutes: RouteRecordRaw[] = [
  {
    path: "/",
    // redirect: "/forms",
    // // OR
    redirect: {
      name: routing.FORM_DASHBOARD,
    },
  },
  {
    path: "/forms",
    name: routing.FORM_DASHBOARD,
    component: import("@modules/forms/FormList.vue"),
    meta: { requiresAuth: true },
    children: [],
  },
];

export default appRoutes;

// Forms Dashboard

// / - Homepage with all forms

// /forms - Alternative dashboard route

// /forms/new - Create a new blank form

// /forms/templates - Browse form templates

// /forms/trash - Deleted forms

// Form Builder

// /forms/:id/edit - Edit form questions and settings

// /forms/:id/design - Customize form appearance

// /forms/:id/settings - Configure form settings

// /forms/:id/share - Manage collaborators and sharing

// Responses

// /forms/:id/responses - View form responses

// /forms/:id/responses/summary - Response analytics

// /forms/:id/responses/individual - View individual responses

// /forms/:id/responses/export - Export response data

// Form Filling

// /forms/:id/view - Preview the form

// /forms/:id/submit - Public URL for form submission

// /forms/:id/thanks - Custom thank-you page after submission
