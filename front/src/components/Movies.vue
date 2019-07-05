<template>
    <div>
        <app-input :msg="genre"></app-input>
        <h2>{{genre}}</h2><br>
        <button @click="back" class="createB">Back</button>

        <table border="1" class="tableCl">
            <tr>
                <th>id</th>
                <th>title</th>
                <th>rating(out of 10)</th>
            </tr>
            <tr v-for="movie in movss">
                <td>{{movie.id}}</td>
                <td>{{movie.title}}</td>
                <td>{{roundRate(movie.rating)}}</td>
                <td><button @click="watch(movie.id)">Watch</button></td>
            </tr>
        </table>
    </div>
</template>

<script>
    const STORE = 'cons-store'

    export default {

        data(){
            return {
                genre: this.$route.params.gId
            }
        },
        created() {
            this.$store.dispatch('loadMovies', this.$route.params.gId);
        },
        computed: {
            movss(){
                return this.$store.getters.ListOfMovie
            }
        },
        methods:{
            back(){
                this.$router.push('/genre');
            },
            watch(index){
                this.$router.push('/movie/'+index);
                localStorage.setItem(STORE,JSON.stringify(this.genre));
            },
            roundRate(index){
                var rounded = parseFloat(index.toFixed(1));
                return rounded
            }

        },



    }
</script>

<style >
    .createB{
        font-size: 12px;
        text-align: center;
        display: inline-block;
        color: darkmagenta;
        margin-left: 5px;
    }
    .tableCl{
        font-family: "Lucida Sans Unicode", "Lucida Grande", Sans-Serif;
        font-size: 16px;
        background: white;
        width: 50%;
        text-align: left;
    }
</style>
