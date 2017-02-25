new Vue({
    el: "#app",
    data: {
        posts: [],
    },
    methods: {
        createBlog: function() {
            location.href = "/admin/post";
        },
        listBlog: function() {
            $.ajax({

            });
        }
    },
    init: function() {

    },
    created: function() {},

})
