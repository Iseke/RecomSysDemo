<template>
    <div>
        <div>
            <input type="text" placeholder="Title" v-model="newGenre" class="initF">
            <button @click="addG" class="createB">Create Genre</button>
        </div>

        <table border="1" class="tableCl">
            <tr>
                <th>id</th>
                <th>Genre</th>
            </tr>
            <tr v-for="genre in genres">
                <td>{{genre.id}}</td>
                <td><input type="text" v-model="genre.name" class="initF"></td>
                <td><button @click="updateG(genre)" class="createB">Change</button></td>
                <td><button @click="deleteG(genre)" class="createB">Delete</button></td>
                <td><button @click="show(genre.id)" class="createB">Show</button></td>
            </tr>
        </table>
        <div>
            <h2>Movies for You</h2>
            <div v-for="mov in fave">
                <ul v-if="mov.rating >3 ">
                    <li>'{{mov.title}}'     Rating - '{{roundd(mov.rating)}}'</li>
                </ul>
            </div>
        </div>

    </div>
</template>

<script>
    export default {
        data(){
            return{
                newGenre: '',
            }
        },
        created() {
            this.$store.dispatch('loadGenre');
            this.$store.dispatch('loadList');
        },
        computed: {
            genres(){
                return this.$store.getters.genreList;
            },
            fave(){
                return this.$store.getters.favorite
            }
        },
        methods: {
            addG () {
                this.$store.dispatch('addGenre', this.newGenre);
                this.newGenre = '';
            },
            deleteG (CurGener) {
                this.$store.dispatch('deleteGenre', CurGener)
            },
            updateG( genre) {
                this.$store.dispatch('updateGenre', genre);
            },
            show(index){
                this.$router.push('/genre/'+index)
            },
            roundd(index){
                var rounded = parseFloat(index.toFixed(1));
                return rounded
            }
        }
    }
</script>

<style>
    .tbl{
        font-family: "Lucida Sans Unicode", "Lucida Grande", Sans-Serif;
        font-size: 16px;
        background: white;
        width: 10%;
        text-align: left;
    }
    .tableCl{
        font-family: "Lucida Sans Unicode", "Lucida Grande", Sans-Serif;
        font-size: 16px;
        background: white;
        width: 40%;
        text-align: left;
    }
    .initF{
        font-family: "Lucida Sans Unicode", "Lucida Grande", Sans-Serif;
        font-size: 16px;
    }
    .createB{
        font-size: 12px;
        text-align: center;
        display: inline-block;
        color: darkmagenta;
        padding: 7px 12px;
        margin-left: 5px;
    }
</style>
