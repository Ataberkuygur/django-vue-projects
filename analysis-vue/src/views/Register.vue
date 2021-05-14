<template>
    <div id="registerApp">
        <RegisterForm />
    </div>
</template>

<script>
import RegisterForm from '../components/Auth/RegisterForm.vue'
export default {
    name: 'registerFormApp',
    components: {
        RegisterForm,
    }
}
</script>

<style scoped>
#registerApp{
    display: flex;
    justify-content: center;
    margin-top: 5%;
}
</style>