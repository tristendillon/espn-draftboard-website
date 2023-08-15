import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import DraftsView from '../views/DraftsView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/drafts',
      name: 'drafts',
      component: DraftsView
    },
    {
      path: '/draft-board',
      name: 'draft-board',
      // Code-splitting to increase the load time of the Home View
      component: () => import('../views/DraftBoardView.vue')
    }
  ]
})

export default router
