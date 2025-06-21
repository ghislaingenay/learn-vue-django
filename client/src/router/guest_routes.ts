import routing from "@constants/router_names";
import type { RouteRecordRaw } from "vue-router";

const guestRoutes: RouteRecordRaw[] = [
  {
    path: "/login",
    name: routing.LOGIN,
    meta: { requiresAuth: false },
    component: () => import("@modules/auth/index.vue"),
  },
  {
    path: "/register",
    name: routing.REGISTER,
    meta: { requiresAuth: false },
    component: () => import("@modules/auth/index.vue"),
  },
];

export default guestRoutes;
