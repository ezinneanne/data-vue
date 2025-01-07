import { createRouter, createWebHistory } from 'vue-router'
// import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/predict',
      name: 'predict',
      component: () => import('../views/PredictView.vue'),
    },
  ],
})

export default router
