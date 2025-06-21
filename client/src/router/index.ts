import type { RouteRecordRaw } from "vue-router";
import guestRoutes from "./guest_routes";
import appRoutes from "./app_routes";
import NotFound from "@components/NotFound.vue";

const routes: RouteRecordRaw[] = [
  ...guestRoutes,
  ...appRoutes,
  {
    path: "/:pathMatch(.*)*",
    name: "NotFound",
    component: import("@components/NotFound.vue"),
  },
];
