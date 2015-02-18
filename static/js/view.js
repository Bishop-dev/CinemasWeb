App.Views.MovieView = Backbone.View.extend({
    // invokes automatically on initialisation
    initialize: function() {
        console.log('view initialized');
    },
    // working tag (even if not created yet)
    tagName: 'li',
    template: _.template($('#movie-tmpl').html()),
    // rendering - create content of tag using model
    render: function() {
        this.$el.html(this.template(this.model.toJSON()));
        return this;
    }
});

App.Views.MoviesView = Backbone.View.extend({
    initialize: function() {
        console.log('movies collection initialized');
    },
    tagName: 'ul',
    render: function() {
        // loop each movie in collection
        this.collection.each(function(movie){
            // create view for each movie in collection
            var movieView = new App.Views.MovieView({model: movie});
            // append view of item to view of collection
            this.$el.append(movieView.render().el);
            // use context 'this' of MoviesView
            // anonymous function 'function(movie){' use WINDOW as default context
        }, this);
        return this;
    }
});