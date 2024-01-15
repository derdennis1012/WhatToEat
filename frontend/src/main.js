import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'

import WhatToEatAPI from './api/WhatToEat.js'

import './style.css'
import App from './App.vue'
const router = createRouter({
    history: createWebHistory(),
    routes: [

      {
        path:'/login',
        component: () => import('./pages/Login.vue'),
        meta: {
          title: 'Login',
          requiresAuth: false
        }
      },
      {
        path:'/restaurants/search',
        component: () => import('./pages/SearchRestaurant.vue'),
        meta: {
          title: 'Search',
          requiresAuth: false
        }
      }
    ]
  })
  
const app = createApp(App)

app.config.globalProperties.$api = new WhatToEatAPI();

app.use(router)
app.mount('#app')
