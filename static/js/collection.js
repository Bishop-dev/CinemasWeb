App.Collections.MovieCollection = Backbone.Collection.extend({
    model : App.Models.Movie,
    url: '/movies/start',
    events : {
        'then': 'show',
        'fetch': 'show'
    },
    show: function() {
        console.log(this.models);
        console.log(this.collection);
    }
});