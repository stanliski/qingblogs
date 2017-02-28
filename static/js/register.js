new Vue({
  el: "#app",
  data: {
    username: "",
    mail: "",
    password: "",
    repasswd: "",
    verifyCode: "",
  },
  methods: {
    onRegister: function() {
      var remoteApi = '/admin/register'

      if (this.username == '') {
        alert('输入用户名不得为空')
        return
      }

      if (this.mail == '') {
        alert('输入邮箱不得为空')
        return
      }

      if (this.password == '' || this.repasswd == '') {
        alert('输入密码不得为空')
        return
      }

      if (this.password != this.repasswd) {
        alert('两次密码输入不一致')
        return
      }

      var self = this;
      $.ajax({
        url: remoteApi,
        type: 'post',
        data: {
          'username': self.username,
          'password': self.password,
          'mail': self.mail,
          'verifyCode': self.verifyCode,
        },
        success: function(res) {
          if (res.success == true) {
            alert(res.message)
            location.href = '/admin'
          } else {
            alert(res.message)
          }
        },
        error: function(res) {
          alert('error')
        }
      });
    },
  },
  init: function() {},
  created: function() {},
})
