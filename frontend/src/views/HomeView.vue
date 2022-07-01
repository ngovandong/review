<template>
  <div>
    <p>Username: {{ user.username }}</p>
    <p>Name: {{ user.last_name + " " + user.firstName }}</p>
    <p>Address: {{ user.address }}</p>
    <p>Phone number: {{ user.phone_number }}</p>
    <p>Email: {{ user.email }}</p>
    <p>Role: {{ user.role }}</p>
    <p>Avatar:</p>
    <v-img
      max-height="150"
      max-width="250"
      :src="'http://127.0.0.1:8000' + user.avatar"
    ></v-img>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "HomeView",
  computed: {
    ...mapState(["user"]),
  },
};
</script>
