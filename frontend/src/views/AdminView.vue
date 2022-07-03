<template lang="">
  <v-container>
    <v-row>
      <v-col cols="12" lg="6">
        <v-card class="mx-auto mt-12">
          <v-list>
            <v-subheader>Power users</v-subheader>
            <v-list-item-group>
              <v-list-item
                v-for="pu in powerUsers"
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
              to="/add_power_user"
            >
              New power user
              <v-icon right dark> add </v-icon>
            </v-btn>
          </v-list>
        </v-card>
      </v-col>
      <v-col cols="12" lg="6">
        <v-card class="mx-auto mt-12">
          <v-list>
            <v-subheader>Normal users</v-subheader>
            <v-list-item-group>
              <v-list-item
                v-for="pu in normalUsers"
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
          </v-list>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
import { privateAxios } from "@/axios";

export default {
  data() {
    return {
      settings: 0,
      powerUsers: [],
      normalUsers: [],
    };
  },
  created() {
    privateAxios.get("api/users/power/power_user/").then((res) => {
      this.powerUsers = res.data;
    });
    privateAxios.get("api/users/power/normal_user/").then((res) => {
      this.normalUsers = res.data;
    });
  },
};
</script>
<style lang=""></style>
