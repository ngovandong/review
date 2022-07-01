import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store'
import ContainerView from '../views/ContainerView.vue'
import HomeView from '../views/HomeView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    component: ContainerView,

    children: [
      {
        path: "",
        component: HomeView,
        name: "home",
        meta: {
          requireLogin: true
        },
      }
    ]

  },
  {
    path: "/login",
    name: "login",
    component: () => import("../views/LoginView.vue"),
  },
  {
    path: "/signup",
    component: () => import("../views/SignupView.vue"),
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})


router.beforeEach((to, from, next) =>
{
  console.log(store.state.isAuthenticated)
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'login', query: { to: to.path } });
  } else {
    next()
  }
})


export default router
