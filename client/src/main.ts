import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import Vue3Toastify, { type ToastContainerOptions } from "vue3-toastify";
import router from "./router";

const app = createApp(App);
app.use(Vue3Toastify, {
  autoClose: 3000,
} as ToastContainerOptions);
app.use(router);
app.mount("#app");
