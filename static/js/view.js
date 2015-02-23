App.Views.MovieView = Backbone.View.extend({
    // working tag (even if not created yet)
    tagName: 'li',
    template: _.template($('#movie-tmpl').html()),
    // rendering - create content of tag using model
    render: function () {
        var time = this.model.get('session');
        this.model.set('session', this.convertDate(time));
        this.$el.html(this.template(this.model.toJSON()));
        return this;
    },
    convertDate: function (miliseconds) {
        var d = new Date(miliseconds.$date);
        var h = d.getHours();
        var m = d.getMinutes();
        return (h < 10 ? '0' + h : h) + ':' + (m < 10 ? '0' + m : m);
    }
});

App.Views.MoviesView = Backbone.View.extend({
    pageSize: 40,
    tagName: 'ul',
    initialize: function () {
        _.bindAll(this, 'scroll');
        $(window).scroll(this.scroll);
    },
    scroll: function () {
        if ($(window).scrollTop() == ($(document).height() - $(window).height())) {
            var self = this;
            var models = this.collection.models;
            var lastMovieId = models[models.length - 1].get('_id').$oid;
            var url = this.collection.additionalFetchURL + lastMovieId + '/';
            // remove = false - to not to remove existing items
            // overriding url
            this.collection.fetch({remove: false, url: url}).then(function() {
                self.renderAdditional();
            });
        }
    },
    render: function () {
        // loop each movie in collection
        this.collection.each(function (movie) {
            // create view for each movie in collection
            var movieView = new App.Views.MovieView({model: movie});
            // append view of item to view of collection
            this.$el.append(movieView.render().el);
            // use context 'this' of MoviesView
            // anonymous function 'function(movie){' use WINDOW as default context
        }, this);
        return this;
    },
    renderAdditional: function() {
        var coll = this.collection;
        var len = this.collection.length;
        coll = this.collection.slice(len - this.pageSize, len);
        for (var i = 0; i < coll.length; i++) {
            var movie = coll[i];
            var movieView = new App.Views.MovieView({model: movie});
            this.$el.append(movieView.render().el);
        }
        return this;
    }
});