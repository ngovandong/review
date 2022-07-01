<template lang="">
  <v-navigation-drawer :value="value" absolute temporary> </v-navigation-drawer>
</template>
<script>
export default {
  props: ["value"],
  data() {
    return {
      show: false,
    };
  },
};
</script>
<style lang=""></style>
