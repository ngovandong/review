<template lang="">
  <div class="wrapper">
    <div class="infor">
      <h1>My account</h1>
      <v-form class="form-info" v-if="user">
        <v-container>
          <v-row>
            <v-col cols="12" sm="3">
              <span class="label">Name:</span>
            </v-col>
            <v-col cols="12" sm="9">
              <v-text-field
                :value="user.last_name + ' ' + user.first_name"
                solo
                readonly
              ></v-text-field>
            </v-col>

            <v-col cols="12" sm="3">
              <span class="label">Username:</span>
            </v-col>
            <v-col cols="12" sm="9">
              <v-text-field :value="user.username" solo readonly></v-text-field>
            </v-col>
            <v-col cols="12" sm="3">
              <span class="label">Email:</span>
            </v-col>
            <v-col cols="12" sm="9">
              <v-text-field :value="user.email" solo readonly></v-text-field>
            </v-col>

            <v-col cols="12" sm="3">
              <span class="label">Phone:</span>
            </v-col>
            <v-col cols="12" sm="9">
              <v-text-field
                :value="user.phone_number"
                solo
                readonly
              ></v-text-field>
            </v-col>

            <v-col cols="12" sm="3">
              <span class="label">Address:</span>
            </v-col>
            <v-col cols="12" sm="9">
              <v-text-field :value="user.address" solo readonly></v-text-field>
            </v-col>
            <v-col cols="12" sm="3">
              <span class="label">Avatar:</span>
            </v-col>
            <v-col cols="12" sm="9">
              <v-img max-height="150" max-width="250" :src="avatar"></v-img>
            </v-col>
          </v-row>
        </v-container>
      </v-form>
      <div class="btn-container">
        <v-btn color="error" @click="handleLogout">Logout</v-btn>
      </div>
    </div>
  </div>
</template>
<script>
import { mapGetters, mapMutations, mapState } from "vuex";
export default {
  data() {
    return {};
  },
  methods: {
    ...mapMutations(["logout"]),
    handleLogout() {
      this.logout();
      this.$router.push("/");
    },
  },
  computed: {
    ...mapState(["user"]),
    ...mapGetters(["avatar"]),
  },
};
</script>
<style scoped>
.wrapper {
  width: 100%;
  padding: 2rem;
}

.infor {
  margin: 0 auto;
  width: 800px;
}

h1 {
  text-align: center;
  margin: 20px 0;
}

h2 {
  text-align: center;
}

span.label {
  font-size: 1.4rem;
  padding-left: 1rem;
}
.btn-container {
  width: 800px;
  display: flex;
  justify-content: center;
  margin: 4rem auto;
}
.form-info {
  margin: 2rem 0;
}
</style>
