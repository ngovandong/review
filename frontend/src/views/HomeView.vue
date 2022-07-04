<template>
  <v-container>
    <v-row>
      <v-col cols="12" lg="4">
        <v-card class="mx-auto mt-12">
          <v-list>
            <v-subheader>Workspace</v-subheader>

            <v-list-item-group :value="selectedWorkspace" color="primary">
              <workspace-card
                v-for="(space, i) in workspaces"
                :key="i"
                :setSelectedWorkspace="() => setSelectedWorkspace(i)"
                :isOwner="user.id == space.owner_id && role == 'PU'"
                :space="space"
              />
            </v-list-item-group>
            <v-btn
              v-if="role == 'PU'"
              color="rgb(56, 83, 216)"
              class="ma-2 white--text"
              @click="
                () => {
                  showAddWorkspace = true;
                }
              "
            >
              New workspace
              <v-icon right dark> add </v-icon>
            </v-btn>
          </v-list>
        </v-card>
      </v-col>
      <v-col cols="12" lg="8">
        <p>Projects</p>
        <div class="project-container" v-if="currentWorkspace">
          <project-card
            v-for="project in currentWorkspace.projects"
            :key="project.id"
            :project="project"
          />
          <create-project-card
            :handleClick="
              () => {
                showAddProject = true;
              }
            "
          />
        </div>
      </v-col>
    </v-row>
    <add-workspace-dialog
      :fetchWorkspace="fetchWorkspace"
      v-if="showAddWorkspace"
      :show="showAddWorkspace"
      :hide="
        () => {
          showAddWorkspace = false;
        }
      "
    />
    <add-project-dialog
      v-if="currentWorkspace"
      :fetchWorkspace="fetchWorkspace"
      :show="showAddProject"
      :hide="
        () => {
          showAddProject = false;
        }
      "
      :currentWorkspace="currentWorkspace.id"
    />
  </v-container>
</template>

<script>
import ProjectCard from "@/components/ProjectCard.vue";
import CreateProjectCard from "@/components/CreateProjectCard.vue";
import { mapGetters, mapState } from "vuex";
import { privateAxios } from "@/axios";
import WorkspaceCard from "@/components/WorkspaceCard.vue";
import AddWorkspaceDialog from "@/components/AddWorkspaceDialog.vue";
import AddProjectDialog from "../components/AddProjectDialog.vue";

export default {
  components: {
    ProjectCard,
    CreateProjectCard,
    WorkspaceCard,
    AddWorkspaceDialog,
    AddProjectDialog,
  },
  data() {
    return {
      selectedWorkspace: 0,
      workspaces: [],
      showAddWorkspace: false,
      showAddProject: false,
    };
  },
  methods: {
    setSelectedWorkspace(i) {
      this.selectedWorkspace = i;
    },
    fetchWorkspace() {
      privateAxios
        .get("/api/myworkspace/")
        .then((res) => (this.workspaces = res.data));
    },
  },
  computed: {
    ...mapState(["user"]),
    ...mapGetters(["role"]),
    currentWorkspace() {
      if (this.workspaces) {
        return this.workspaces[this.selectedWorkspace];
      }
      return null;
    },
  },

  mounted() {
    this.fetchWorkspace();
  },
};
</script>

<style scoped>
.project-container {
  width: 100%;
  display: flex;
  flex-wrap: wrap;
}
</style>
