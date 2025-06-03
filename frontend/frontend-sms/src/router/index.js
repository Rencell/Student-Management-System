import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '@/views/Dashboard.vue'
import Student from '@/views/Student.vue'
import StudentDetail from '@/views/StudentDetail/StudentDetail.vue'
import StudentSubjectDetail from '@/views/StudentDetail/StudentSubjectDetail.vue'
import Classes from '@/views/Classes.vue'
import Subject from '@/views/Subject.vue'
import login from '@/views/Authentication/login.vue'
import { useAuthStore } from '@/stores/auth'



const requireAuthenticated = (to, from, next) => {
  const authStore = useAuthStore();
  if (!authStore.isAuthenticated) {
    next({
      path: '/login',
      query: { redirect: to.fullPath }  
    });
  } else {
    next();
  }
};

const redirectLogout = (to, from, next) => {
  const authStore = useAuthStore();
  authStore.logout().then(() => next('/login'));
};

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Dashboard,
      beforeEnter : requireAuthenticated
      
    },
    {
      path: '/login',
      name: 'login',
      component: login,
    },
    {
      path: '/class',
      name: 'class',
      component: Classes,
      beforeEnter : requireAuthenticated
    },
    {
      path: '/subjects',
      name: 'subject',
      component: Subject,
      beforeEnter : requireAuthenticated
    },
    {
      path: '/students',
      name: 'student',
      component: Student,
      beforeEnter : requireAuthenticated
    },
    {
      path: '/students/:id',
      name: 'studentdetail',
      component: StudentDetail,
      beforeEnter : requireAuthenticated
    },
    {
      path: '/students/:stud_id/subjects/:subj_id/enr/:enroll_id',
      name: 'Studentsubjectdetail',
      component: StudentSubjectDetail,
      beforeEnter : requireAuthenticated
    },
    {
      path: '/logout',
      name: 'logout',
      beforeEnter: redirectLogout
    }
  ],
})

export default router
