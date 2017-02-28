new Vue({
  el: "#app",
  data: {
    username: "",
    password: "",
    verifyCode: "",
  },
  methods: {
    onLogin: function() {
      if (this.username == '') {
        alert('用户名或邮箱不得为空');
        return
      }

      if (this.password == '') {
        alert('密码不得为空');
        return
      }

      if (this.verifyCode == '') {
        alert('验证码不得为空')
        return
      }

      var remoteApi = "/admin/login";
      var self = this;
      $.ajax({
        url: remoteApi,
        type: 'post',
        data: {
          'username': self.username,
          'password': self.password,
          'verifyCode': self.verifyCode,
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
