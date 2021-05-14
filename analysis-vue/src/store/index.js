import Vue from 'vue'
import Vuex from 'vuex'
import AuthStore from './Auth/index.js'
import CategoryStore from './Category/index.js'
import HabitStore from './Habit/index.js'

Vue.use(Vuex);

const store = new Vuex.Store({
    state: {},
    getters: {},
    mutations: {},
    actions: {},
    modules: {
        AuthStore,
        CategoryStore,
        HabitStore,
    },
});

export default store;