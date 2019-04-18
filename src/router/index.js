import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Rank from '@/components/rankPage'
import Login from '@/components/loginPage'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/Rank',
      name: 'Rank',
      component: Rank
    },
    {
      path: '/Login',
      name: 'Login',
      component: Login
    }

  ]
})
