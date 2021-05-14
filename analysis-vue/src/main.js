import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import router from './router/index.js'
import store from './store/index.js'

axios.defaults.baseURL = 'http://localhost:8000/';

new Vue({
  el: '#app',
  render: h => h(App),
  router: router,
  store: store,
});
