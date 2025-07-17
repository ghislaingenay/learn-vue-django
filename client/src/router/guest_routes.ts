import routing from "@constants/router_names";
import type { RouteRecordRaw } from "vue-router";

const guestRoutes: RouteRecordRaw[] = [
  {
    path: "/login",
    name: routing.LOGIN,
    meta: { requiresAuth: false },
    component: async () => await import("@pages/auth/login.vue"),
  },
  {
    path: "/register",
    name: routing.REGISTER,
    meta: { requiresAuth: false },
    component: async () => await import("@pages/auth/register.vue"),
  },
];

export default guestRoutes;
