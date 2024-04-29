<template>
  <layout-div>
    <div class="row justify-content-md-center">
      <div class="col-12">
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
          <div class="container-fluid">
            <a class="navbar-brand" href="#">Purchase system</a>
            <div class="d-flex">
              <ul class="navbar-nav">
                <li class="nav-item">
                  <a @click="logoutAction()" class="nav-link" aria-current="page" href="#">Logout</a>
                </li>
              </ul>
            </div>
          </div>
        </nav>
        <h2 class="text-left mt-2">User name: {{ this.name }}</h2>
        <div id="app">
          <table>
            <thead>
              <tr>
                <th v-for="col in keys" :key="col">{{ col }}</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(row, index) in filteredRows" :key="index">
                <td v-html="row.title"></td>
                <td v-html="row.categories"></td>
                <td v-html="row.authors"></td>
                <td v-html="row.ratings"></td>
                <td v-html="row.price"></td>
              </tr>
            </tbody>
          </table>
          <input type="text" placeholder="Filter by title or categories" v-model="filter" />
        </div>
        <div>
          <button @click="submit_record">Submit</button>
          <tr>{{submitted}}</tr>
        </div>
        <br/>
        <div>

        </div>
        <div id="app">
          <br/>
          <h2 class="text-left mt-2">Purchased record</h2>
          <table>
            <thead>
              <tr>
                <th v-for="col in this.tracking_keys" :key="col">{{ col }}</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(row, index) in this.filteredpurchaserecord" :key="index">
                <td v-html="row.record_number"></td>
                <td v-html="row.name"></td>
                <td v-html="row.title"></td>
                <td v-html="row.price"></td>
              </tr>
            </tbody>
          </table>
          <input type="text" placeholder="Filter by title or categories" v-model="filter_purchase" />
        </div>
        <div>
          <button @click="delete_record">Delete record</button>
          <tr>{{submitted}}</tr>
        </div>
      </div>
    </div>
  </layout-div>
</template>

<script>
import axios from "axios";
import LayoutDiv from "../LayoutDiv.vue";

export default {
  name: "DashboardPage",
  components: {
    LayoutDiv
  },
  data() {
    return {
      user: {},
      results: [],
      rows: [],
      keys: [],
      search: '',
      filter: '',
      submitted: '',
      name: [],
      purchase_record: {},
      tracking_record : [],
      tracking_keys: [],
      filter_purchase: '',
      delete_record_array: {}
    };
  },
  created() {
    this.load_book_list();
    this.name = localStorage.getItem("name");
    this.show_purchase_record();
  },
  methods: {

    logoutAction() {
      localStorage.setItem("token", "");
      this.$router.push("/");
    },
    load_book_list() {
      axios
        .get("http://127.0.0.1:80/book_list")
        .then((r) => {
          this.results = r.data;
          for (var i = 0; i < r.data.length; i++) {
            this.rows.push(i);
          }
          this.keys = Object.keys(this.results[0]);
          // console.log(this.keys);
        })
        .catch((e) => {
          return e;
        });
    },
    submit_record() {
      this.purchase_record.name = this.name
      this.purchase_record.title = this.filteredRows[0].title
      this.purchase_record.price = this.filteredRows[0].price
      console.log(this.purchase_record)
      axios
        .post("http://127.0.0.1:80/buy_new_book", this.purchase_record)
        .then((response) => {
            console.log(response.data)
            this.show_purchase_record();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    show_purchase_record(){
      var post = {'name':this.name}
      axios
        .post("http://127.0.0.1:80/show_user_purchase_record", post)
        .then((response) => {
            this.tracking_record = response.data
            this.tracking_keys = Object.keys(this.tracking_record[0]);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    delete_record(){
      console.log(this.filteredpurchaserecord[0])
      axios
        .post("http://127.0.0.1:80/delete_purchase_record", this.filteredpurchaserecord[0])
        .then((response) => {
            console.log(response.data)
            this.show_purchase_record()
            this.filter_purchase = ""
        })
        .catch((error) => {
          console.log(error);
        });
    }

  },
  computed: {
    filteredRows() {
      return this.results.filter(row => {
        const title = row.title.toString();
        const categories = row.categories;
        const authors = row.authors.toString();
        const ratings = row.ratings;
        const price = row.price.toString();
        const searchTerm = this.filter;
        return (
          title.includes(searchTerm) || categories.includes(searchTerm) ||
          authors.includes(searchTerm) || ratings.includes(searchTerm) ||
          price.includes(searchTerm)
        );
      });
    },
    filteredpurchaserecord(){
      return this.tracking_record.filter(row => {
        const trackingname = row.name.toString();
        const trackingtitle = row.title.toString();
        const trackingsearchTerm = this.filter_purchase;
        return (
          trackingtitle.includes(trackingsearchTerm) || trackingname.includes(trackingsearchTerm)
        );
      });
    }
  }
}

</script>

<style scoped>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td,
th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

th {
  background-color: #dddddd;
}

input[type=text],
select {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  margin-top: 25px;
}
</style>
