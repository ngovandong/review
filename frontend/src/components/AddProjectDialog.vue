<template lang="">
  <v-dialog :value="show" persistent max-width="600px">
    <v-card>
      <v-card-title>
        <span class="text-h5">Add project</span>
      </v-card-title>
      <v-card-text>
        <v-container>
          <v-row>
            <v-col cols="12">
              <v-text-field
                label="Project name"
                v-model="name"
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
  props: ["show", "hide", "fetchWorkspace", "currentWorkspace"],
  data() {
    return {
      name: null,
    };
  },
  methods: {
    add() {
      if (this.name != null) {
        privateAxios
          .post("/api/project/", {
            name: this.name,
            workspace: this.currentWorkspace,
          })
          .then(() => {
            this.hide();
            this.fetchWorkspace();
            this.name = null;
          })
          .catch((error) => console.log(error));
      }
    },
  },
};
</script>
<style lang=""></style>
