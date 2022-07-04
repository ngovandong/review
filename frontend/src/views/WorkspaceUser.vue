<template lang="">
  <div>
    <v-card class="mx-auto mt-12">
      <v-list>
        <v-subheader>User in workpace</v-subheader>
        <v-list-item-group v-if="users">
          <v-list-item
            v-for="pu in users"
            :key="pu.id"
            @click="$router.push('/user_detail/' + pu.id)"
          >
            <v-list-item-action>
              <v-checkbox :input-value="true"></v-checkbox>
            </v-list-item-action>

            <v-list-item-content>
              <v-list-item-title>{{ pu.username }}</v-list-item-title>
              <v-list-item-subtitle>{{
                pu.first_name + " " + pu.last_name
              }}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
        <v-btn
          color="rgb(56, 83, 216)"
          class="ma-2 white--text"
          @click="showDialog = true"
        >
          Add user
          <v-icon right dark> add </v-icon>
        </v-btn>
      </v-list>
    </v-card>
    <add-user-dialog
      v-if="showDialog"
      :show="showDialog"
      :hide="
        () => {
          showDialog = false;
        }
      "
      :fetchUser="fetchUser"
      :workspaceId="id"
    />
  </div>
</template>
<script>
import { privateAxios } from "@/axios";
import AddUserDialog from "@/components/AddUserDialog.vue";
export default {
  props: ["id"],
  components: {
    AddUserDialog,
  },
  data() {
    return {
      users: null,
      showDialog: false,
    };
  },
  methods: {
    fetchUser() {
      privateAxios
        .get("/api/users/power/workspace_user/", {
          params: { id: this.id },
        })
        .then((res) => (this.users = res.data));
    },
  },
  created() {
    this.fetchUser();
  },
};
</script>
<style lang=""></style>
