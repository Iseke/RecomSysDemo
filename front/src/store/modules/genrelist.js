import axios from 'axios'

export default {
    state: {
        genreList: [],
        favoriteList: []
    },
    getters: {
        genreList: state => state.genreList,
        favorite: state => state.favoriteList
    },
    mutations: {
        SET_GENRE (state, genres) {
            state.genreList = genres
        },
        SET_FAVORITE(state,movies){
          state.favoriteList = movies
        },
        ADD_GENRE (state, genreObject) {
            var max = 0;
            for(var l in state.genreList){
                if(l.id > max){
                    max = l.id;
                }
            }
            state.genreList.push({max,genreObject});
        },
        DELETE_GENRE (state, genre) {
            var genreList = state.genreList
            genreList.splice(genreList.indexOf(genre), 1);
            state.genreList = genreList
        },
        UPDATE_GENRE (state, genre) {
            var genreList = state.genreList
            for(var list in genreList){
                if(list.id == genre.id){
                    list = genre;
                }
            }
            state.genreList = genreList;
        },
    },
    actions: {
        loadGenre ({ commit }) {
            axios
                .get('http://localhost:8000/api/genre/')
                .then(response => {
                    commit('SET_GENRE', response.data)
                })

        },
        loadList({commit}){
          axios.get('http://localhost:8000/api/movies/getBest/').then(res=>{
              commit('SET_FAVORITE', res.data)
          });
        },
        addGenre ({ commit}, genreItem ) {
            if (!genreItem) {
                return
            }

            axios.post('http://localhost:8000/api/genre/',{
                name: genreItem
            }).then(response => {commit('ADD_GENRE', genreItem)});
        },
        deleteGenre ({ commit }, genre) {
            axios.delete(`http://localhost:8000/api/genre/${genre.id}/`).then(response => {
                commit('DELETE_GENRE', genre);
            })
        },
        updateGenre({ commit }, genre){
            axios.put(`http://localhost:8000/api/genre/${genre.id}/`,{
                name: genre.name
            }).then(res=>{commit('UPDATE_GENRE',genre)})
        },
    },

}
