App.Collections.MovieCollection = Backbone.Collection.extend({
    model : App.Models.Movie,
    url: '/movies/start',
    additionalFetchURL: '/movies/additional/'
});