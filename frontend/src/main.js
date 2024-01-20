import {
  createApp
} from 'vue'
import {
  createRouter,
  createWebHistory
} from 'vue-router'

import WhatToEatAPI from './api/WhatToEat.js'

import './style.css'
import App from './App.vue'
const router = createRouter({
  history: createWebHistory(),
  routes: [

    {
      path: '/restaurants/search',
      component: () => import('./pages/SearchRestaurant.vue'),
      meta: {
        title: 'Search',
        requiresAuth: false
      }
    },
    {
      path: '/restaurants/list/:postcode',
      component: () => import('./pages/RestaurantList.vue'),
      name: 'RestaurantList',
      meta: {
        title: 'Restaurant List',
        requiresAuth: false
      }
    },
    {
      path: '/restaurants/:primarySlug',
      component: () => import('./pages/RestaurantDetail.vue'),
      name: 'RestaurantDetail',
      meta: {
        title: 'Restaurant Detail',
        requiresAuth: false
      }
    },
    {
      path: '/',
      redirect: '/restaurants/search'
    }
  ]
})

const app = createApp(App)

app.config.globalProperties.$api = new WhatToEatAPI();

app.use(router)
app.mount('#app')