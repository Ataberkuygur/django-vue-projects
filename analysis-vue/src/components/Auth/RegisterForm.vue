<template>
    <div id="registerFormApp">
        <form @submit.prevent="register" method="POST">
            <div class="field form-title">
                <h3>Kayıt Formu</h3>
            </div>
            <div class="field username">
                <input v-model="username" class="form-control" placeholder="Username" type="text">
            </div>
            <div class="field password">
                <input v-model="password" class="form-control" placeholder="Password" type="password">
            </div>   
            <div class="field password-confirm">
                <input v-model="passwordConfirm" class="form-control" placeholder="Password Confirm" type="password">
            </div>       
            <p class="error-message">{{errorMessage}}</p>            
            <button 
                type="submit" 
                class="button form-button button-ocean-blue"
            >
                Kayıt Ol
            </button>   
        </form>
    </div>
</template>

<script>
export default {
    name: 'registerFormApp',
    data(){
        return{
            username: '',
            password: '',
            passwordConfirm: '',
            errorMessage: '',
        }
    },
    methods: {
        register(){
            if (this.password == this.passwordConfirm){
                let credentials = {
                    username: this.username,
                    password: this.password,
                };
                this.$store.dispatch('registerAsync', credentials);
                this.errorMessage = ''
            }
            else{
                this.errorMessage = 'Passwords must be same.'
            }
        }
    }
}
</script>

<style scoped>
#registerFormApp{
    max-width: 500px;
    width: 40%;
    height: 390px;
    box-shadow: 0px 0px 5px 5px gray;
    border-radius: 10px;
    margin: auto;
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
    letter-spacing: 2px;
    width: 100px;
    height: 45px;
}

.error-message{
    color: brown;
}

@media only screen and (max-width: 768px){
    #registerFormApp{
        width: 90%;
    }
}
</style>