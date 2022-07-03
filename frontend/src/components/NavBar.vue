<template>
  <div>
    <v-app-bar app dark color="#3853D8">
      <v-app-bar-nav-icon @click="toogleDrawer"></v-app-bar-nav-icon>

      <v-toolbar-title
        ><router-link class="home-link" to="/">
          Trello</router-link
        ></v-toolbar-title
      >

      <v-spacer></v-spacer>
      <template v-if="showSearchBar">
        <v-text-field
          class="mt-5"
          v-if="showSearch"
          @change="setSearchString($event)"
          autofocus
        ></v-text-field>
        <v-btn icon @click="switchSearch">
          <v-icon>mdi-magnify</v-icon>
        </v-btn>
      </template>
      <v-btn icon x-large to="/my">
        <v-avatar size="36">
          <img :src="thumbnail" alt="John" />
        </v-avatar>
      </v-btn>
    </v-app-bar>
    <drawer-left v-model="drawer" />
    <v-dialog v-model="showCart" persistent max-width="600px">
      <VCart :closeCart="closeCart" />
    </v-dialog>
  </div>
</template>

<script>
import { mapGetters, mapMutations, mapState } from "vuex";
import DrawerLeft from "./DrawerLeft.vue";
export default {
  data() {
    return {
      drawer: null,
      showSearch: false,
      showCart: false,
    };
  },
  methods: {
    handleClick() {
      if (this.isAuthenticated) {
        this.showCart = true;
      } else {
        this.$router.push("/login");
      }
    },
    toogleDrawer() {
      this.drawer = !this.drawer;
    },
    closeCart() {
      this.showCart = false;
    },
    ...mapMutations(["setSearchString"]),
    switchSearch() {
      this.showSearch = !this.showSearch;
      this.setSearchString("");
    },
  },
  computed: {
    ...mapState(["isAuthenticated"]),
    showSearchBar() {
      return this.$route.path == "/";
    },
    ...mapGetters(["thumbnail"]),
  },
  components: { DrawerLeft },
};
</script>

<style>
.v-toolbar__title {
  font-size: 1rem !important;
}

.v-badge__badge {
  font-size: 10px !important;
  height: 18px !important;
  min-width: 18px !important;
}
.home-link {
  text-decoration: none;
  color: white;
  font-size: 1.2rem;
  font-weight: bold;
}
.home-link:visited {
  color: white;
}
</style>
