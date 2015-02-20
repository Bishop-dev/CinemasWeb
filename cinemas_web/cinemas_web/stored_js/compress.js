function compress(limit) {
    var cursor = db.daily_20_02_15.find({'session': {'$gt': new Date()}}).limit(limit * 2);
    var result = [];
    
    function isMatches(first, second) {
        return first.session == second.session 
            && first.name == second.name 
            && first._id != second._id
            && first.cinema != second.cinema;
    }
    
    function joinCinemas(first, second) {
        var property = first.cinema;
        if (typeof property === 'string') {
             first.cinema = [property];
        } else {
             first.cinema.push(second.cinema);
        }
    }
    
    while (cursor.hasNext()) {
        var current = cursor.next();
        if (result.lenght != 0) {
            var previous = result[result.length - 1];
            if (isMatches(previous, current)) {
                joinCinemas(previous, current);
            } else {
                result.push(current);    
            }
        } else {
            result.push(current);
        }
        if (cursor.hasNext()) {
            var item = cursor.next();
            if (isMatches(item, current)) {
                joinCinemas(result[result.length - 1], item);
            } else {
                if (result.length == limit) {
                    return true;
                }
                result.push(item);
            }
        }
        while (cursor.hasNext() && result.length == limit) {
            var next = cursor.next();
            var last = result[29];
            if (isMatches(last, next)) {
                joinCinemas(last, next);
            } else {
                break;    
            }
        }
    }
    return result;
}