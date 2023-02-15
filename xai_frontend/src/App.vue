<template>
  <div id="app">
    <router-view :key="this.$route.path"></router-view>
  </div>
</template>

<script>

export default {
  name: 'App',
  components: {
  },
}
</script>

<style>

body {
  background: rgb(255, 255, 255);
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  padding: 4em;
}
</style>
