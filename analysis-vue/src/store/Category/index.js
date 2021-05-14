import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '../../router/index.js'

Vue.use(Vuex);

const AuthStore = {
    state: {
        categoryList: [],
    },
    getters: {
        getCategoryList(state){
            let token = localStorage.getItem('Token');
            let authorization = { 
                headers: {
                    Authorization: `Token ${token}`
                }
            };
            axios.get('categories/', authorization)
            .then(response => state.categoryList = response.data)
            .catch(error => console.log(error.message));
            return state.categoryList;
        }
    },
    mutations: {
 
    },
    actions: {

    },
};

export default AuthStore;