new Vue({
  el: "#app",
  data: {
    textEditor: null,
    title: "",
    content: "",
    id: "",
  },
  methods: {
    updateBlog: function() {

    },
  },
  init: function() {},
  created: function() {},
  mounted: function() {
    this.textEditor = editormd("editormd", {
      path: "/static/components/editor.md/lib/",
      height: 800,
    });
    this.textEditor.setEditorTheme('monokai');
  }
})
