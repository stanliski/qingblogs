/* Javascript */

var vm = new Vue({
  el: "#app",
  data: {
    posts: [],
    post: {
      title: "",
      id: "",
    },
  },
  methods: {
    editBlog: function(id) {
      location.href = '/admin/edit?id=' + id;
    },
    createBlog: function() {
      location.href = "/admin/post";
      this.listBlog();
    },
    onDelete: function(id, title) {
      this.post.title = title;
      this.post.id = id;
      $('.ui.small.modal').modal('show');
    },
    handleDel: function() {
      var remoteApi = "/api/v1/post"
      var self = this;
      $.ajax({
        url: remoteApi,
        type: 'DELETE',
        dataType: 'json',
        data: {
          'id': self.post.id
        },
        success: function(res) {
          if (res.success) {
            console.log(res.message)
            self.listBlog();
          }
        },
        error: function() {
          console.log('request error.')
        },
      });
      $('.ui.small.modal').modal('hide');
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
