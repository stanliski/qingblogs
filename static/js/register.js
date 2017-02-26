new Vue({
  el: "#app",
  data: {
    username: "",
    mail: "",
    password: "",
    repasswd: "",
  },
  methods: {
    onRegister: function() {
      var remoteApi = '/admin/register'
      if (this.password != this.repasswd) {
        alert('两次密码输入不一致');
        return;
      }
      var self = this;
      $.ajax({
        url: remoteApi,
        type: 'post',
        data: {
          'username': self.username,
          'password': self.password,
          'mail': self.mail,
        },
        success: function(res) {
          if (res.success == true) {
            console.log(res.message)
            location.href = '/admin'
          }
        },
        error: function(res) {

        }
      });
    },
  },
  init: function() {},
  created: function() {},
})
