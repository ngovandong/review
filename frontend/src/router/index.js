import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store'
import ContainerView from '../views/ContainerView.vue'
import HomeView from '../views/HomeView.vue'
import MyView from '../views/MyView.vue'
import AdminView from '../views/AdminView.vue'
import AddPowerUser from '../views/AddPowerUser.vue'
import UserDetail from '../views/UserDetail.vue'
import WorkspaceUser from '../views/WorkspaceUser.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    component: ContainerView,
    meta: {
      requireLogin: true
    },
    children: [
      {
        path: "/",
        component: HomeView,
        name: "home",
      },
      {
        path: "/my",
        component: MyView,
        name: "my",

      },
      {
        path: "/project/:id",
        component: () => import("../views/ProjectView.vue"),
        props: true,
      },
      {
        path: "/admin",
        component: AdminView,
        name: "admin",
        children: [

        ]
      },
      {
        path: "/add_power_user",
        component: AddPowerUser,
        name: "add_power_user",
      },
      {
        path: "/user_detail/:id",
        component: UserDetail,
        name: "user_detail",
        props: true,
      },
      {
        path: "/space_user/:id",
        component: WorkspaceUser,
        name: "space_user",
        props: true,
      },
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
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'login', query: { to: to.path } });
  } else {
    next()
  }
})


export default router
