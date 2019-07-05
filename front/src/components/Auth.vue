<template>
    <div>
        <h1>Authentication</h1>
        <span>Username<input type="text" v-model="username" ></span><br>
        <span>Password<input type="password" v-model="passwd" ></span><br>
        <button @click="log">Log In</button>
        <button @click="reg">Register</button>

    </div>
</template>

<script>
    export default {
        data(){
            return{
                username: '',
                passwd: '',
            }
        },
        methods:{
            log(){
                this.$router.push('/genre')
            },
            reg(){
                this.$router.push('/register/')
            }
        }
    }
</script>

<style scoped>

</style>
