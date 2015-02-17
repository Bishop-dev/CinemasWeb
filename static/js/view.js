App.Views.MovieView = Backbone.View.extend({
    // invokes automatically on initialisation
    initialize: function() {
        console.log('view initialized');
    },
    // working tag (even if not created yet)
    tagName: 'li',
    // rendering - create content of tag using model
    render: function() {
        this.$el.html(this.model.get('name'));
    }
});