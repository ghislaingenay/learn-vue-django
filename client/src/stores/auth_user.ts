import type { User } from "@types";
import { defineStore } from "pinia";

type AuthUserStore = {
  user: User | null;
  refreshToken: string | null;
};

type AuthUserGetters = {
  isAuthenticated: (state: AuthUserStore) => boolean;
  getUser: (state: AuthUserStore) => User | null;
  getRefreshToken: (state: AuthUserStore) => string | null;
};

type AuthUserActions = {
  setUser: (user: User | null) => void;
  setRefreshToken: (token: string | null) => void;
  clearUser: () => void;
};

export const useAuthUserStore = defineStore<
  string,
  AuthUserStore,
  AuthUserGetters,
  AuthUserActions
>("auth_user", {
  state: () => ({
    user: null,
    refreshToken: null,
  }),
  getters: {
    isAuthenticated: (state): boolean => !!state.user,
    getUser: (state): User | null => state.user,
    getRefreshToken: (state): string | null => state.refreshToken,
  },
  actions: {
    setUser(user: User | null) {
      this.user = user;
    },
    setRefreshToken(token: string | null) {
      this.refreshToken = token;
    },
    clearUser() {
      this.user = null;
      this.refreshToken = null;
    },
  },
});
