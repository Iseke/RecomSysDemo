<template>
    <div>
        <h1>Registration</h1>
        <span>Username<input type="text" v-model="username" ></span><br>
        <span>Password<input type="password" v-model="passwd" ></span><br>
        <span>Repeat Password<input type="password" v-model="repeatPas" ></span><br>
        <button @click="reg">Register</button><br>

    </div>
</template>

<script>
    export default {
        data(){
            return{
                username: '',
                passwd: '',
                repeatPas: ''
            }
        },
        methods:{
            reg(){
                if(this.username!=='' && this.passwd!=='' && this.repeatPas!==''){
                    if(this.passwd===this.repeatPas){
                        this.$router.push('/genre/')
                    }else{
                        alert('Your password and repeat password should be equal')
                    }
                }else {
                    alert('Please fill all fields!!!')
                }
            }
        }
    }
</script>

<style scoped>

</style>
