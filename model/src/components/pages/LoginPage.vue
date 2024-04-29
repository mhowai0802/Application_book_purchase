<template>
  <layout-div>
    <div class="row justify-content-md-center mt-5">
      <div class="col-4">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title mb-4">Sign In</h5>
            <form>
              <div class="mb-3">
                <label htmlFor="phone_number" class="form-label">
                  User name
                </label>
                <input v-model="name" type="name" class="form-control" id="name"
                  name="name" />
              </div>
              <div class="mb-3">
                <label htmlFor="password" class="form-label">Password </label>
                <input v-model="password" type="password" class="form-control" id="password" name="password" />
              </div>
              <div class="d-grid gap-2">
                <button @click="loginAction()" type="button" class="btn btn-primary btn-block">
                  Login
                </button>
                <p class="text-center">
                  Don't have account?
                  <router-link to="/register">Register here </router-link>
                </p>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </layout-div>
</template>

<script>
import axios from "axios";
import LayoutDiv from "../LayoutDiv.vue";

export default {
  name: "LoginPage",
  components: {
    LayoutDiv,
  },
  data() {
    return {
      name: "",
      password: "",
    };
  },
  methods: {
    loginAction() {
      this.isSubmitting = true;
      let payload = {
        name: this.name,
        password: this.password,
      };
      axios
        .post("http://127.0.0.1:80/login", payload)
        .then((response) => {
          console.log(response.data.password)
          if (response.data.password == this.password){
          localStorage.setItem("name", response.data.name);
          this.$router.push("/dashboard");
          return response;
          }
          else if (response.data.password == 'nouser'){
            alert("Not registered user").then(() => {
          });}
          else if (response.data.password != this.password){
            alert("Wrong password").then(() => {
          });}
        })
        .catch((error) => {
          console.log(error);
        });
    }
  },
};
</script>

<style scoped></style>