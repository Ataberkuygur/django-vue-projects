<template>
    <div id="loginFormApp">
        <form @submit.prevent="login" method="POST">
            <div class="field form-title">
                <h3>Giriş Formu</h3>
            </div>
            <div class="field username">
                <input v-model="username" class="form-control" placeholder="Username" type="text">
            </div>
            <div class="field password">
                <input v-model="password" class="form-control" placeholder="Password" type="password">
            </div>         
            <button 
                @click="login"
                type="submit" 
                class="button form-button button-ocean-blue"
            >
                Giriş Yap
            </button>   
        </form>
    </div>
</template>

<script>
export default {
    name: 'loginFormApp',
    data(){
        return{
            username: '',
            password: '',
        }
    },
    methods: {
        login(){
            let credentials = {
                username: this.username,
                password: this.password,
            };
            this.$store.dispatch('loginAsync', credentials);
        }
    }
}
</script>

<style scoped>
#loginFormApp{
    max-width: 500px;
    width: 40%;
    height: 300px;
    box-shadow: 0px 0px 5px 5px gray;
    border-radius: 10px;
    padding: 10px;
}

.form-title{
    margin-top: 20px;
}

.field input{
    height: 50px;
    border-radius: 0px;
    margin-bottom: 20px;
    outline: 0px;
}

.form-button{
    margin-top: 10px;
    margin-left: 10px;
    width: 110px;
    height: 45px;
}

@media only screen and (max-width: 768px){
    #loginFormApp{
        width: 90%;
    }
}
</style>