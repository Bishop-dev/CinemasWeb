App.Models.Movie = Backbone.Model.extend({
    defaults: {
        name: 'ololo',
        duration: 45
    },
    work: function() {
        return this.get('name') + ' working';
    }
});