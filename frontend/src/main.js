import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'

import './style.css'
import App from './App.vue'
const router = createRouter({
    history: createWebHistory(),
    routes: []
  })
  
  app.use(router)

createApp(App).mount('#app')
