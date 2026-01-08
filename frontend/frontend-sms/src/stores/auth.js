import { defineStore } from 'pinia'
import authentication from '@/services/auth/auth'
import { computed, reactive, ref } from 'vue'
export const useAuthStore = defineStore('auth', () => {

  const TOKEN_STORAGE = 'AUTH_TOKEN'
  const actionStates = reactive({
    authenticating: false,
    error: false,
    token: null,
  })

  const errors = ref({})

  const token = ref(localStorage.getItem(TOKEN_STORAGE));
  const isAuthenticated = ref(!!token.value);

  const login = async (form, route,router) => {
    mutations.LOGIN_BEGIN()
    try {
      const response = await authentication.login(form.username, form.password)
      actionStates.loginresponse = response.data
      mutations.SET_TOKEN(response.data['key'])

      const redirectPath = route.query.redirect || '/';
      await router.push(redirectPath);

      mutations.LOGIN_SUCCESS()
    } catch (e) {
      console.error(e)
      
      const data = e.response.data;
      Object.keys(data).forEach(key => {
        errors.value[key] = data[key][0]; 
      });
      mutations.LOGIN_FAILED()
    }
  }

  const logout = async () => {
    try {
      await authentication.logout()
      mutations.REMOVE_TOKEN()
    } catch (e) {
      console.log(e)
    } finally {
      mutations.LOGOUT()
    }
  }

  const mutations = {
    LOGIN_BEGIN: () => {
      actionStates.authenticating = true
      actionStates.error = false
    },
    LOGIN_SUCCESS: () => {
      actionStates.authenticating = false
      actionStates.error = false
    },
    LOGIN_FAILED: () => {
      actionStates.authenticating = false
      actionStates.error = true
    },
    LOGOUT: () => {
      actionStates.authenticating = false
      actionStates.error = false
      mutations.REMOVE_TOKEN()
    },
    SET_TOKEN: (token) => {
      localStorage.setItem(TOKEN_STORAGE, token)
      authentication.setToken(token)
      actionStates.token = token
      isAuthenticated.value = true;
    },
    REMOVE_TOKEN: () => {
      localStorage.removeItem(TOKEN_STORAGE)
      authentication.removeToken()
      actionStates.token = null
      isAuthenticated.value = false;
    },
  }

  return { login, logout, actionStates, errors, isAuthenticated}
})
