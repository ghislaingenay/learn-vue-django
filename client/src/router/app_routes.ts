import routing from "@constants/router_names";
import type { RouteRecordRaw } from "vue-router";

const appRoutes: RouteRecordRaw[] = [];

const routes = [
  {
    path: "/forms",
    name: routing.FORM_DASHBOARD,
    component: import("@modules/forms/index.vue").then((m) => m.FormList),
    meta: { requiresAuth: true },
    children: [],
  },
];

export default appRoutes;
