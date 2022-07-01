<template>
  <v-app id="inspire">
    <v-main>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4>
            <v-card class="elevation-12">
              <v-toolbar dark color="primary">
                <v-toolbar-title>Login</v-toolbar-title>
              </v-toolbar>
              <v-card-text>
                <v-form ref="form" v-model="valid" lazy-validation>
                  <v-alert v-show="showError" type="error">{{ error }}</v-alert>
                  <v-text-field
                    prepend-icon="person"
                    v-model="email"
                    :rules="emailRules"
                    label="Username"
                    required
                  >
                  </v-text-field>

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
                <v-btn color="cyan" to="/signup">Signup</v-btn>
                <v-btn :disabled="!valid" color="primary" @click="handleClick"
                  >Login</v-btn
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
import { mapActions } from "vuex";
export default {
  data() {
    return {
      error: "",
      showError: false,
      valid: true,
      email: "",
      emailRules: [(v) => !!v || "Username is required"],
      password: "",
      passwordRules: [(v) => !!v || "Password is required"],
    };
  },
  methods: {
    ...mapActions(["login"]),
    handleClick() {
      this.login({ username: this.email, password: this.password }).catch(
        (error) => {
          if (error.response) {
            this.error = "Wrong username or password";
            this.showError = true;
          } else {
            this.error = "Something went wrong. Please try again";
            this.showError = true;
          }
        }
      );
    },
  },
};
</script>

<style></style>
