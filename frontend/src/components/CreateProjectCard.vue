<template lang="">
  <div class="project-card">
    <v-card height="100%" width="100%" class="card" @click="handleClick">
      <v-icon size="40">add</v-icon>
    </v-card>
  </div>
</template>
<script>
export default {
  props: ["handleClick"],
  data() {
    return {};
  },
  methods: {},
};
</script>
<style scoped>
.project-card {
  padding: 10px;
  width: 33.3%;
  height: 140px;
}
.card {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
