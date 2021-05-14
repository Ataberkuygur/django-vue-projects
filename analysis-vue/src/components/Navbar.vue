<template>
    <div id="navbarApp">
        <nav class="navbar navbar-expand-md navbar-dark">
            <router-link
                tag="a"
                :to="{ name: 'home' }"
                class="navbar-brand"
            >
                Analiz
            </router-link>
            <button
                class="navbar-toggler"
                data-toggle="collapse"
                data-target="#navbarCollapse"
            >
                <span class="navbar-toggler-icon"></span>
            </button>

            <div 
                class="collapse navbar-collapse" 
                id="navbarCollapse"
            >
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item">
                        <router-link
                            tag="a"
                            :to="{ name: 'home' }"
                            class="nav-link"
                        >
                            Ana Sayfa
                        </router-link>
                    </li>
                    <li class="nav-item" v-if="checkAuthentication">
                        <router-link
                            tag="a"
                            :to="{ name: 'habits' }"
                            class="nav-link"
                        >
                            Rutinler
                        </router-link>
                    </li> 
                    <li class="nav-item" v-if="!checkAuthentication">
                        <router-link
                            tag="a"
                            :to="{ name: 'login' }"
                            class="nav-link"
                        >
                            Giriş Yap
                        </router-link>
                    </li>     
                    <li class="nav-item" v-if="!checkAuthentication">
                        <router-link
                            tag="a"
                            :to="{ name: 'register' }"
                            class="nav-link"
                        >
                            Kayıt Ol
                        </router-link>
                    </li>  
                    <li class="nav-item" v-if="checkAuthentication">
                        <a class="logout nav-link" @click="logout">Çıkış Yap</a>
                    </li>  
                </ul>
            </div>
        </nav>
    </div>
</template>

<script>
export default {
    name: 'navbarApp',
    methods: {
        logout(){
            this.$store.dispatch('logoutAsync');
        },
    },
    computed: {
        checkAuthentication(){
            return this.$store.getters.getIsAuthenticated;
        }, 
    },
}
</script>

<style scoped>
.navbar{
    background-color: black;
    color: white !important;
}

.navbar-brand{
    text-decoration: none;
    color: white !important;
    margin-left: 5%;
}

.nav-link{
    color: white !important;
    margin-right: 1.5em;
}

.logout{
    cursor: pointer;
}
</style>