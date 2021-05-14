<template>
    <div id="loginApp">
        <LoginForm class="loginForm" />
    </div>
</template>

<script>
import LoginForm from '../components/Auth/LoginForm.vue'
export default {
    name: 'loginApp',
    components: {
        LoginForm,
    }
}
</script>

<style scoped>
#loginApp{
    display: flex;
    justify-content: center;
    margin-top: 8%;
}
</style>