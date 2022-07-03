<template lang="">
  <v-dialog :value="show" persistent max-width="600px">
    <v-card>
      <v-card-title>
        <span class="text-h5">Add ticket</span>
      </v-card-title>
      <v-card-text>
        <v-container>
          <v-row>
            <v-col cols="12">
              <v-text-field
                label="Workspace name"
                v-model="name"
                required
              ></v-text-field>
            </v-col>
            <v-col cols="12">
              <v-text-field
                label="Description"
                v-model="desc"
                required
              ></v-text-field>
            </v-col>
          </v-row>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" text @click="hide"> Close </v-btn>
        <v-btn color="blue darken-1" text @click="add"> Add </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
import { privateAxios } from "@/axios";

export default {
  props: ["show", "hide", "fetchProject", "status", "project"],
  data() {
    return {
      name: null,
      desc: null,
    };
  },
  methods: {
    add() {
      if (this.name != null) {
        privateAxios
          .post("/api/ticket/", {
            name: this.name,
            project: this.project,
            desc: this.desc,
            status: this.status,
          })
          .then(() => {
            this.hide();
            this.fetchProject();
            this.name = null;
            this.desc = null;
          })
          .catch((error) => console.log(error));
      }
    },
  },
};
</script>
<style lang=""></style>
