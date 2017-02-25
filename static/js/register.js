new Vue({
    el: "#app",
    data: {
        username: "",
        mail: "",
        passwd: "",
        repasswd: "",
    },
    methods: {
        onRegister: function() {
            var remoteApi = '/admin/register'
            var self = this;
            $.ajax({
                url: remoteApi,
                type: 'post',
                data: {
                    'username': self.username,
                    'passwd': self.passwd,
                    'mail': self.mail,
                },
                success: function(res) {
                    console.log(res.success);
                },
                error: function(res) {

                }
            });
        },
    },
    init: function() {},
    created: function() {},
})
