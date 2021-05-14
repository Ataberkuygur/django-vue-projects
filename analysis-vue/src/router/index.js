import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import Habits from '../views/Habits.vue'

Vue.use(VueRouter);

const routes = [
    { path: '/', component: Home, name: 'home' },
    { path: '/login', component: Login, name: 'login' },
    { path: '/register', component: Register, name: 'register' },
    { path: '/habits', component: Habits, name: 'habits' },
];

export default new VueRouter({
    routes: routes,
    mode: 'history',
});