import Vue from 'vue';
import VueRouter from 'vue-router';

import WatchMovie from '../components/WatchMovie.vue';
import Movies from '../components/Movies.vue'
import Main from '../components/Main.vue'
import Auth from '../components/Auth.vue'
import Reg from '../components/Register.vue'

Vue.use(VueRouter);

export default new VueRouter({
    routes:[
        {path: '/movie/:movieId', component: WatchMovie},
        {path: '/genre/:gId', component: Movies},
        {path: '/genre', component: Main},
        {path: '/login', component: Auth},
        {path: '/register', component: Reg},


    ],
    mode: 'history',
})
