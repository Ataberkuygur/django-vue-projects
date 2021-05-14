import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '../../router/index.js'

Vue.use(Vuex);

const HabitStore = {
    state: {
        habitList: [],
        theHabit: {},
        habitSlug: '',
    },
    getters: {
        getHabitList(state){
            let token = localStorage.getItem('Token');
            let authorization = { 
                headers: {
                    Authorization: `Token ${token}`
                }
            };            
            axios.get('habits/', authorization)
            .then(response => state.habitList = response.data)
            .catch(error => console.log(error.message));
            return state.habitList;
        },
        getTheHabit(state){
            let token = localStorage.getItem('Token');
            let authorization = {
                headers: {
                    Authorization: `Token ${token}`
                }
            };
            axios.get(`habits/${state.habitSlug}`, authorization)
            .then(response => state.theHabit = response.data[0])
            .catch(error => console.log(error.message));
            return state.theHabit;
        }
    },
    mutations: {
        createHabit(state, habit){
            let token = localStorage.getItem('Token');
            let authorization = { 
                headers: {
                    Authorization: `Token ${token}`
                }
            };
            axios.post('habits/', habit, authorization)
            .then(response => router.push({ name: 'home' }))
            .catch(error => console.log(error.message));
        },
        finishTheHabitDayOrDont(state, day){
            let token = localStorage.getItem('Token');
            let authorization = { 
                headers: {
                    Authorization: `Token ${token}`
                }
            };
            axios.put(`days/${day.slug}/`, day, authorization)
            .then(response => response)
            .catch(error => console.log(error.message));            
        }
    },
    actions: {
        createHabitAsync({commit}, habit){
            commit('createHabit', habit);
        },
        finishTheHabitDayOrDontAsync({commit}, day){
            commit('finishTheHabitDayOrDont', day);
        }        
    },
};

export default HabitStore;