import { defineStore } from 'pinia'
import authentication from '@/services/auth/auth'
import { computed, reactive, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router';
export const useAuthStore = defineStore('auth', () => {

  const route = useRoute();
  const router = useRouter();

  const TOKEN_STORAGE = 'AUTH_TOKEN'
  const actionStates = reactive({
    authenticating: false,
    error: false,
    token: null,
  })

  const errors = ref({})

  const isAuthenticated = computed(() => !!localStorage.getItem(TOKEN_STORAGE));

  const login = async (form) => {
    mutations.LOGIN_BEGIN()
    try {
      const response = await authentication.login(form.username, form.password)
      actionStates.loginresponse = response.data
      mutations.SET_TOKEN(response.data['key'])
      mutations.LOGIN_SUCCESS()
    } catch (e) {
      console.error(e)
      
      const data = e.response.data;
      console.log(data)
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
      const redirectPath = route.query.redirect || '/';
      router.push(redirectPath);
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
    },
    REMOVE_TOKEN: () => {
      localStorage.removeItem(TOKEN_STORAGE)
      authentication.removeToken()
      actionStates.token = null
    },
  }

  return { login, logout, actionStates, errors, isAuthenticated}
})
