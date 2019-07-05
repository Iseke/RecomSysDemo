<template>
  <div class="hello">
    <h1>{{$route.params.movieId}}</h1>
    <button @click="back">Back</button>
    <table class="tableCl">
      <tr>
        <th>Title</th>
        <th></th>
        <th>Rating</th>
        <th>rating_count</th>
      </tr>
      <tr>
        <td>{{movie.title}}<td>
        <td>{{roundR(movie.rating)}}</td>
        <td>{{movie.rating_count}}</td>
      </tr>
    </table>
    <span>Put Rating - <input type="number" v-model="newRate"> - {1-10}</span>
    <button @click="updT">Rate</button>
  </div>
</template>

<script>
  const STORE = 'cons-store'
  const ST = 'cons-mov'


  export default {
        data(){
            return{
                curGenre: '',
                newRate:''
            }
        },
        created(){
          localStorage.setItem(ST,JSON.stringify(this.$route.params.movieId));
          this.curGenre = JSON.parse(localStorage.getItem(STORE)|| '[]')
          this.$store.dispatch('loadMovie', this.curGenre)
        },
        computed:{
          movie(){
            return this.$store.getters.movies
          }
        },
        methods:{
            back(){
              this.$router.go(-1);
            },
            roundR(index){
              var rounded = parseFloat(index.toFixed(1));
              return rounded
            },
            updT(word){
              this.$store.dispatch('updateMovie', this.newRate)
            }

        }

    }
</script>

<style>
  .tableCl{
    font-family: "Lucida Sans Unicode", "Lucida Grande", Sans-Serif;
    font-size: 16px;
    background: white;
    width: 50%;
    text-align: left;
  }
</style>
