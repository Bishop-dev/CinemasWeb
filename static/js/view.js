App.Views.MovieView = Backbone.View.extend({
    // working tag (even if not created yet)
    tagName: 'li',
    template: _.template($('#movie-tmpl').html()),
    // rendering - create content of tag using model
    render: function() {
        var time = this.model.get('session');
        this.model.set('session', this.convertDate(time));
        this.$el.html(this.template(this.model.toJSON()));
        return this;
    },
    events: {
        // 'hover span' : 'showAlert'
        'click' : 'showAlert'
    },
    convertDate: function(miliseconds) {
        var date = new Date(miliseconds.$date);
        var d = date.getDate();
        var h = date.getHours();
        var m = date.getMinutes();
        return d + ' ' + h + ':' + m;
    }
});

App.Views.MoviesView = Backbone.View.extend({
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