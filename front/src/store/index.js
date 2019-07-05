import Vue from 'vue';
import Vuex from 'vuex';
import genreList from './modules/genrelist'
import movieList from './modules/movieList'
import getRate from './modules/putrating'

Vue.use(Vuex)


export default new Vuex.Store({
    modules:{
        genreList,
        movieList,
        getRate,
    }
})
