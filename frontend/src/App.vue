<script setup>
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
<router-view />
</template>

<script>
export default {
  name: 'App',
  components: {
    HelloWorld
  },
  created() {
    //check if ztheres a userID in localstorage if no ask user to set one (prompt)
    var userID = localStorage.getItem('userID')
    if(!userID){
      var userID = prompt("Please enter your userID", "000PRO11");
      localStorage.setItem('userID', userID)
    }
  }
}  
</script>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
