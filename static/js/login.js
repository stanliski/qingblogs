new Vue({
  el: "#app",
  data: {
    username: "",
    password: "",
  },
  methods: {
    onLogin: function() {
      var remoteApi = "/admin/login";
      var self = this;
      $.ajax({
        url: remoteApi,
        type: 'post',
        data: {
          'username': self.username,
          'password': self.password,
        },
        success: function(res) {
          if (res.success) {
            location.href = '/admin'
          } else {
            console.log(res.success + ":" + res.message);
          }
        },
        error: function() {}
      });
    },

    onForget: function() {
      location.href = "/admin/find"
    },
  },
  init: function() {

  },
  created: function() {

  },
})
