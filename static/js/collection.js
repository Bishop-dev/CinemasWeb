App.Collections.MovieCollection = Backbone.Collection.extend({
    model : App.Models.Movie,
    url: '/movies/start',
    initialize: function() {
        this.on('sync', this.compressData, this);
    },
    compressData: function() {
        var result = [];
        function isMatches(first, second) {
            return first.get('session').$date == second.get('session').$date
                && first.get('name') == second.get('name')
                && first.get('_id') != second.get('_id')
                && first.get('cinema') != second.get('cinema');
        }
        function joinCinemas(first, second) {
            var property = first.get('cinema');
            if (typeof property === 'string') {
                 first.set('cinema', [property, second.get('cinema')]);
            } else {
                 first.get('cinema').push(second.get('cinema'));
            }
            return first;
        }
        for (var i = 0; i < this.models.length; i++) {
            var current = this.models[i];
            if (result.length == 0) {
                result.push(current);
            } else {
                var previous = result[result.length - 1];
                if (isMatches(previous, current)) {
                    result[result.length - 1] = joinCinemas(previous, current);
                } else {
                    result.push(current);
                }
            }
        }
        this.models = result;
    }
});