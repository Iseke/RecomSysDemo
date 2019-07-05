import axios from 'axios'

export default {
    state: {
        ListOfMovie: [],
    },
    getters: {
        ListOfMovie: state=>state.ListOfMovie,
    },
    mutations:{
        SET_MOVIES(state, movies){
            state.ListOfMovie = movies
        },
        ADD_MOVIE(state, movie){
            state.ListOfMovie.push(movie)
        },
        DELETE_MOVIE(state,movie){
            var newList = state.ListOfMovie
            newList.splice(newList.indexOf(movie),1)
            state.ListOfMovie = newList
        },
        UPDATE_MOVIE(state,movie){
            var newList = state.ListOfMovie
            for(var l in newList){
                if(l.id == movie.id){
                    l = movie
                }
            }
            state.ListOfMovie = newList
        }

    },
    actions: {
        loadMovies({commit},index){
            axios.get(`http://localhost:8000/api/genre/${index}/movies/`).then((response) => {
                commit('SET_MOVIES', response.data)
            });
        },
    },

}
