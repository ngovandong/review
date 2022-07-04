<template lang="">
  <v-dialog :value="show" persistent max-width="600px">
    <v-card>
      <v-card-title>
        <span class="text-h5">Add User</span>
      </v-card-title>
      <v-card-text>
        <v-alert v-show="error" type="error">User not found!</v-alert>
        <v-container>
          <v-row>
            <v-col cols="12" lg="10">
              <v-text-field
                label="email"
                v-model="email"
                required
              ></v-text-field>
            </v-col>
            <v-col cols="12" lg="2">
              <v-btn @click="search" :disabled="!email" icon>
                <v-icon>search</v-icon>
              </v-btn>
            </v-col>
            <v-col v-if="user" cols="10">
              <v-card class="px-5 pt-2">
                <h4>{{ user.email }}</h4>
                <p>{{ user.username }}</p>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" text @click="hide"> Close </v-btn>
        <v-btn color="blue darken-1" :disabled="!user" text @click="add">
          Add
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
import { privateAxios } from "@/axios";

export default {
  props: ["show", "hide", "fetchUser", "workspaceId"],
  data() {
    return {
      email: null,
      result: null,
      user: null,
      error: false,
    };
  },
  methods: {
    add() {
      privateAxios
        .post(`/api/workspace/${this.workspaceId}/add_user/`, {
          user_id: this.user.id,
        })
        .then(() => {
          this.hide();
          this.fetchUser();
        })
        .catch((error) => console.log(error));
    },
    search() {
      privateAxios
        .get("/api/users/power/search_user/", {
          params: {
            email: this.email,
          },
        })
        .then((res) => {
          if (res.data) {
            this.user = res.data;
          } else {
            this.error = true;
          }
        });
    },
  },
};
</script>
<style lang=""></style>
