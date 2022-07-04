<template lang="">
  <v-col cols="12" lg="4">
    <v-card class="mx-auto mt-12">
      <v-list two-line>
        <v-subheader
          >{{ title }}
          <v-spacer></v-spacer>
          <v-btn @click="showDialog" icon><v-icon>add</v-icon></v-btn>
        </v-subheader>
        <v-list-item-group>
          <template v-for="(ticket, index) in tickets">
            <v-list-item :key="index">
              <template>
                <v-list-item-content>
                  <v-list-item-title v-text="ticket.name"></v-list-item-title>

                  <v-list-item-subtitle
                    v-text="ticket.desc"
                  ></v-list-item-subtitle>
                </v-list-item-content>

                <v-list-item-action>
                  <v-btn
                    v-if="backStatus"
                    @click="
                      () => {
                        next(ticket, backStatus);
                      }
                    "
                    icon
                  >
                    <v-icon color="orange"> arrow_back </v-icon>
                  </v-btn>
                  <v-btn
                    v-if="nextStatus"
                    @click="
                      () => {
                        next(ticket, nextStatus);
                      }
                    "
                    icon
                  >
                    <v-icon color="green"> arrow_forward </v-icon>
                  </v-btn>
                </v-list-item-action>
              </template>
            </v-list-item>

            <v-divider
              v-if="index < ticket.length - 1"
              :key="index"
            ></v-divider>
          </template>
        </v-list-item-group>
      </v-list>
    </v-card>
  </v-col>
</template>
<script>
import { privateAxios } from "@/axios";

export default {
  props: [
    "showDialog",
    "title",
    "tickets",
    "nextStatus",
    "backStatus",
    "fetchProject",
  ],
  methods: {
    next(ticket, status) {
      privateAxios
        .patch(`/api/ticket/${ticket.id}/`, {
          status: status,
        })
        .then(() => {
          this.fetchProject();
        })
        .catch((error) => console.log(error));
    },
  },
};
</script>
<style lang=""></style>
