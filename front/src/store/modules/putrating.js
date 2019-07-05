import axios from 'axios'
const ST = 'cons-mov'
const STORE = 'cons-store'

export default {
    state: {
        moviesList: ''
    },
    getters: {
        movies: state => state.moviesList
    },
    mutations: {
        SET_MOVIE(state, movie){
            state.moviesList = movie
        },

    },
    actions:{
        loadMovie({commit},index1){
            var curM  = JSON.parse(localStorage.getItem(ST)|| '[]')
            axios.get(`http://localhost:8000/api/genre/${index1}/movies/${curM}/`).then((response) => {
                commit('SET_MOVIE', response.data)
            });
        },
        updateMovie({ commit }, newRate){
            var curG  = JSON.parse(localStorage.getItem(ST)|| '[]')
            var curM  = JSON.parse(localStorage.getItem(STORE)|| '[]')
            var m = newRate
            axios.put(`http://localhost:8000/api/genre/${curG}/movies/${curM}/rating/`,{
                rating: m
            }).then(res=>{});
            console.log(newRate)
            axios.get(`http://localhost:8000/api/genre/${curG}/movies/${curM}/`).then((response) => {
                commit('SET_MOVIE', response.data)
            });
        },
    }
}
