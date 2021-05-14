import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '../../router/index.js'

Vue.use(Vuex);

const AuthStore = {
    state: {
        isAuthenticated: false,
    },
    getters: {
        getIsAuthenticated(state){
            if (localStorage.getItem('Token')){
                state.isAuthenticated = true;
            }
            else{
                state.isAuthenticated = false;
            }
            return state.isAuthenticated;
        },
    },
    mutations: {
        login(state, credentials){
            axios.post('auth-token/', credentials)
            .then(response => {
                state.isAuthenticated = true;
                let token = response.data.token;
                localStorage.setItem('Token', token);
                localStorage.setItem('Username', credentials.username)
                router.push({ name: 'home' });
            })
            .catch(error => {
                console.log(error.message);
            });
        },
        logout(state){
            state.isAuthenticated = false;
            localStorage.removeItem('Token');
            localStorage.removeItem('Username');
        },
        register(state, credentials){
            axios.post('users/', credentials)
            .then(response => {
                router.push({ name: 'login' });
            })
            .catch(error => {
                console.log(error.message);
            });            
        }
    },
    actions: {
        loginAsync({commit}, credentials){
            commit('login', credentials);
        },
        logoutAsync({commit}){
            commit('logout');
        },
        registerAsync({commit}, credentials){
            commit('register', credentials);
        }
    },
};

export default AuthStore;