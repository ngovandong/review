<template>
  <v-app id="inspire">
    <v-main>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4>
            <v-card class="elevation-12">
              <v-toolbar dark color="primary">
                <v-toolbar-title>Sign Up</v-toolbar-title>
              </v-toolbar>
              <v-card-text>
                <v-form ref="form" v-model="valid" lazy-validation>
                  <v-alert v-show="showError" type="error">{{ error }}</v-alert>
                  <v-text-field
                    prepend-icon="person"
                    v-model="firstName"
                    :rules="firstNameRules"
                    label="First name"
                    required
                  ></v-text-field>
                  <v-text-field
                    prepend-icon="person"
                    v-model="lastName"
                    :rules="lastNameRules"
                    label="Last name"
                    required
                  ></v-text-field>
                  <v-text-field
                    prepend-icon="person"
                    v-model="username"
                    :rules="usernameRules"
                    label="Username"
                    required
                  ></v-text-field>
                  <v-text-field
                    prepend-icon="email"
                    v-model="email"
                    :rules="emailRules"
                    label="Email"
                    required
                  >
                  </v-text-field>
                  <v-text-field
                    prepend-icon="phone"
                    v-model="phone"
                    :rules="phoneRules"
                    label="Phone"
                    required
                  >
                  </v-text-field>
                  <v-text-field
                    prepend-icon="home"
                    v-model="address"
                    :rules="addressRules"
                    label="Address"
                    required
                  >
                  </v-text-field>
                  <v-file-input
                    label="Avatar"
                    accept="image/*"
                    prepend-icon="mdi-camera"
                    @change="onFilePicked"
                  ></v-file-input>
                  <v-text-field
                    prepend-icon="lock"
                    v-model="password"
                    :rules="passwordRules"
                    label="Password"
                    type="password"
                    required
                  ></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn :disabled="!valid" color="primary" @click="handleClick"
                  >Add</v-btn
                >
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import { privateAxios } from "@/axios";
import { mapActions } from "vuex";
export default {
  data() {
    return {
      error: "",
      showError: false,
      valid: true,
      email: "",
      emailRules: [(v) => !!v || "email is required"],
      firstName: "",
      firstNameRules: [(v) => !!v || "First name is required"],
      lastName: "",
      lastNameRules: [(v) => !!v || "Last name is required"],
      password: "",
      passwordRules: [(v) => !!v || "Password is required"],
      phone: "",
      phoneRules: [(v) => !!v || "Phone is required"],
      address: "",
      addressRules: [(v) => !!v || "Adress is required"],
      username: "",
      usernameRules: [(v) => !!v || "Username is required"],
      avatar: null,
    };
  },
  methods: {
    ...mapActions(["signup"]),
    handleClick() {
      const bodyFormData = new FormData();
      bodyFormData.append("username", this.username);
      bodyFormData.append("first_name", this.firstName);
      bodyFormData.append("last_name", this.lastName);
      bodyFormData.append("email", this.email);
      bodyFormData.append("address", this.email);
      bodyFormData.append("phone_number", this.phone);
      bodyFormData.append("avatar", this.avatar);
      bodyFormData.append("password", this.username);
      privateAxios
        .post("/api/users/power/", bodyFormData, {
          headers: { "Content-Type": "multipart/form-data" },
        })
        .then(() => {
          this.$router.push("/admin");
        });
    },
    onFilePicked(file) {
      this.avatar = file;
    },
  },
};
</script>

<style></style>
