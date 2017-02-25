new Vue({
    el: "#app",
    data: {
        textEditor: null,
        title: "",
        content: "",
    },
    methods: {
        postBlog: function() {
            this.content = $('#editormd textarea').val();
            var self = this
            if (this.title != "" && this.content != "") {
                $.post(
                    "/admin/post", {
                        "title": self.title,
                        "content": self.content,
                    },
                    function(res) {
                        alert(res.success);
                    }
                );
            } else {
                alert("标题内容不得为空");
            }
        },
    },
    init: function() {
        var self = this;
    },
    created: function() {},
    mounted: function() {
        this.textEditor = editormd("editormd", {
            path: "/static/components/editor.md/lib/",
            height: 800,
        });
        this.textEditor.setEditorTheme('monokai');
    }
})
