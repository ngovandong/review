<template lang="">
  <v-list-item v-if="!isOwner" @click="setSelectedWorkspace">
    <v-list-item-content>
      <v-list-item-title v-text="space.name"></v-list-item-title>
    </v-list-item-content>
  </v-list-item>
  <v-list-group v-else @click="setSelectedWorkspace">
    <template v-slot:activator>
      <v-list-item-title>{{ space.name }}</v-list-item-title>
    </template>

    <v-list-item @click="$router.push(`/space_user/${space.id}`)">
      <v-list-item-title>Management</v-list-item-title>
      <v-list-item-icon>
        <v-icon>mdi-account-multiple-outline</v-icon>
      </v-list-item-icon>
    </v-list-item>

    <v-list-item>
      <v-list-item-title>Settings</v-list-item-title>
      <v-list-item-icon>
        <v-icon>mdi-cog-outline</v-icon>
      </v-list-item-icon>
    </v-list-item>
  </v-list-group>
</template>
<script>
export default {
  props: ["space", "isOwner", "setSelectedWorkspace"],
};
</script>
<style lang=""></style>
