new Vue({
    el: "#app",
    data: {
        username: "",
        passwd: "",
    },
    methods: {
        onLogin: function() {
            var remoteApi = "/admin/login";
            var self = this;
            console.log(this.username);
            console.log(this.passwd);
            $.ajax({
                url: remoteApi,
                type: 'post',
                data: {
                    'username': self.username,
                    'passwd': self.passwd
                },
                success: function(res) {
                    console.log(res.success + ":" + res.message);
                },
                error: function() {

                }
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
