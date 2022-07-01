<template>
  <router-view />
</template>

<script>
export default {
  name: "App",

  data: () => ({
    //
  }),
  beforeCreate() {
    if (this.$store.state.isAuthenticated) {
      this.$store.dispatch("fetchUser");
    }
  },
};
</script>
