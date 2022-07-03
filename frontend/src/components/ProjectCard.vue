<template lang="">
  <div class="project-card">
    <v-card
      height="100%"
      width="100%"
      class="card"
      :img="imgs[Math.floor(Math.random() * imgs.length)]"
      @click="handleClick"
    >
      <p class="title">{{ project.name }}</p>
    </v-card>
  </div>
</template>
<script>
export default {
  props: ["project"],
  data() {
    return {
      imgs: [
        "https://cdn.vuetifyjs.com/images/cards/house.jpg",
        "https://cdn.vuetifyjs.com/images/cards/road.jpg",
        "https://cdn.vuetifyjs.com/images/cards/plane.jpg",
        "https://cdn.vuetifyjs.com/images/cards/sunshine.jpg",
      ],
    };
  },
  methods: {
    handleClick() {
      this.$router.push("/project/" + this.project.id);
    },
  },
};
</script>
<style scoped>
.project-card {
  padding: 10px;
  width: 33.3%;
  height: 140px;
}
.card {
}

.title {
  padding: 10px;
  font-size: 16px;
  color: white;
  font-weight: 700;
}
</style>
