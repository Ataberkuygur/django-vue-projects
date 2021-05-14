<template>
  <div id="app">
    <Navbar />
    <router-view></router-view>
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue'
export default {
  name: 'app',
  components: {
    Navbar,
  }
}
</script>

<style>
.button-ocean-blue{
  color: white;
  background-color: rgb(59, 208, 185);
  border: 1px solid rgb(59, 208, 185);
}
</style>
