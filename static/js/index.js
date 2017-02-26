/* Javascript */

var vm = new Vue({
  el: "#app",
  data: {
    posts: []
  },
  methods: {
    createBlog: function() {
      location.href = "/admin/post";
      this.listBlog();
    },
    listBlog: function() {
      var self = this
      $.ajax({
        url: '/api/v1/post',
        type: "GET",
        dataType: "json",
        success: function(res) {
          if (res.success == true) {
            self.posts = res.posts;
            console.log(self.posts.length);
          } else {
            console.log(res.message)
          }
        },
        error: function() {
          console.log('error');
        },
      });
    },
  },
  created: function() {
    this.listBlog();
  }
})
