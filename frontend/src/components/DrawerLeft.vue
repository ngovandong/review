<template lang="">
  <v-navigation-drawer :value="value" absolute temporary>
    <v-list v-if="role == 'AD'" flat>
      <v-subheader>Functions</v-subheader>
      <v-list-item-group v-model="selectedItem" color="primary">
        <v-list-item @click="$router.push('/admin')">
          <v-list-item-icon>
            <v-icon>people</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>Admin site</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list-item-group>
    </v-list>
  </v-navigation-drawer>
</template>
<script>
import { mapGetters } from "vuex";

export default {
  props: ["value"],
  data() {
    return {
      show: false,
      selectedItem: null,
    };
  },
  computed: {
    ...mapGetters(["role"]),
  },
};
</script>
<style lang=""></style>
