<template lang="">
  <v-container v-if="project">
    <h1>{{ project.name }}</h1>
    <v-row>
      <table-card
        :showDialog="
          () => {
            showDialog('TD');
          }
        "
        title="To Do"
        :tickets="this.todos()"
        nextStatus="IP"
        :fetchProject="fetchProject"
      />
      <table-card
        :showDialog="
          () => {
            showDialog('IP');
          }
        "
        title="In Progress"
        :tickets="this.inProgresses()"
        nextStatus="DO"
        :fetchProject="fetchProject"
      />
      <table-card
        :showDialog="
          () => {
            showDialog('DO');
          }
        "
        title="Done"
        :tickets="this.dones()"
        :nextStatus="null"
        :fetchProject="fetchProject"
      />
    </v-row>

    <add-ticket-dialog
      v-if="project"
      :fetchProject="fetchProject"
      :show="show"
      :hide="
        () => {
          show = false;
        }
      "
      :status="selectedStatus"
      :project="project.id"
    />
  </v-container>
</template>
<script>
import { privateAxios } from "@/axios";
import AddTicketDialog from "@/components/AddTicketDialog.vue";
import TableCard from "@/components/TableCard.vue";

export default {
  components: {
    AddTicketDialog,
    TableCard,
  },
  props: ["id"],
  data() {
    return {
      selectedStatus: "TO",
      show: false,
      project: null,
    };
  },
  computed: {
    todos() {
      return () => {
        return this.project.tickets.filter((t) => t.status == "TD");
      };
    },
    inProgresses() {
      return () => this.project.tickets.filter((t) => t.status == "IP");
    },
    dones() {
      return () => this.project.tickets.filter((t) => t.status == "DO");
    },
  },
  methods: {
    showDialog(status) {
      this.selectedStatus = status;
      this.show = true;
    },
    fetchProject() {
      privateAxios
        .get(`/api/project/${this.id}/`)
        .then((res) => (this.project = res.data));
    },
  },
  created() {
    this.fetchProject();
  },
};
</script>
<style lang=""></style>
