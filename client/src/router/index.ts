import {
  createRouter,
  createWebHistory,
  type RouteRecordRaw,
} from "vue-router";
import guestRoutes from "./guest_routes";
import appRoutes from "./app_routes";
import routing from "@constants/router_names";

const routes: RouteRecordRaw[] = [
  ...guestRoutes,
  ...appRoutes,
  {
    path: "/:pathMatch(.*)*",
    name: routing.NOTFOUND,
    component: import("@components/NotFound.vue"),
    meta: { requiresAuth: false },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

const isAuthenticated = () => {
  // check GET auth/me later
  return true;
};

router.beforeEach((to, _, next) => {
  if (to.meta.requiresAuth && !isAuthenticated()) {
    next({ name: routing.LOGIN });
  } else {
    next();
  }
});

export default router;
