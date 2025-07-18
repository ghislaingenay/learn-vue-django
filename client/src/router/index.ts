import {
  createRouter,
  createWebHistory,
  type RouteRecordRaw,
} from "vue-router";
import guestRoutes from "./guest_routes";
import appRoutes from "./app_routes";
import routing from "@constants/router_names";
import { authService } from "@services/auth";

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
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

router.beforeEach(async (to, _, next) => {
  const isAuth = await authService.isAuthenticated();
  if (to.meta.requiresAuth && !isAuth) {
    next({ name: routing.LOGIN, replace: true });
  } else {
    next();
  }
});

// router.beforeResolve(async (to) => {
//   if (to.meta.requiresCamera) {
//     try {
//       await askForCameraPermission();
//     } catch (error) {
//       if (error instanceof NotAllowedError) {
//         // ... handle the error and then cancel the navigation
//         return false;
//       } else {
//         // unexpected error, cancel the navigation and pass the error to the global handler
//         throw error;
//       }
//     }
//   }
// });

// router.afterEach((to, from) => {
//   sendToAnalytics(to.fullPath)
// })

export default router;
