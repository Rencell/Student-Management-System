import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '@/views/Dashboard.vue'
import Student from '@/views/Student.vue'
import StudentDetail from '@/views/StudentDetail/StudentDetail.vue'
import StudentSubjectDetail from '@/views/StudentDetail/StudentSubjectDetail.vue'
import Classes from '@/views/Classes.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Dashboard,
    },
    {
      path: '/class',
      name: 'class',
      component: Classes,
    },
    {
      path: '/students',
      name: 'student',
      component: Student,
    },
    {
      path: '/students/1',
      name: 'studentdetail',
      component: StudentDetail,
    },
    {
      path: '/students/1/subjects/subject1',
      name: 'Studentsubjectdetail',
      component: StudentSubjectDetail,
    },
  ],
})

export default router
