import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import "vuetify/styles/main.css";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import { createVuetify } from "vuetify";
import Vue3Toastify, { type ToastContainerOptions } from "vue3-toastify";
import router from "./router";

const vuetify = createVuetify({ components, directives });

const app = createApp(App);
app.use(Vue3Toastify, {
  autoClose: 3000,
} as ToastContainerOptions);
app.use(router);
app.use(vuetify);
app.mount("#app");
