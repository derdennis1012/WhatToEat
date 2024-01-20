class WhatToEatAPI{
    //constructor
    constructor(){
        this.url = "http://localhost:5555/";
        this.restaurant = new RestaurantAPI();
        this.votes = new Votes();
    }
}

class APIUtils{
    //constructor
    constructor(){
        this.url = "http://localhost:5555/";
    }
    get(url){
        return fetch(this.url + url).then(res => res.json());
    }
    post(url, data){
        console.log(this.url + url)
        return fetch(this.url + url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data),
        }).then(res => res.json());
    }
    put(url, data){
        return fetch(this.url + url, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data),
        }).then(res => res.json());
    }
    delete(url){
        return fetch(this.url + url, {
            method: 'DELETE',
        }).then(res => res.json());
    }
}

class Votes extends APIUtils{
    constructor(){
        super();
        this.url = "http://localhost:5555/votes/"
    }
    getAllVotes(){
        return this.get(``);
    }
    resetVote(){
        return this.delete(``);
    }
    addVote(slug){
        //get userid form localstorage
        var userID = localStorage.getItem('userID')
        return this.post(``,{
            restaurant_slug: slug,
            user_id:userID
        });
    
    }
}

class RestaurantAPI extends APIUtils{
    //constructor
    constructor(){
        super();
        this.url = "http://localhost:5555/restaurant/"
    }

    searchByPostalCode(postalCode){
        return this.get(`area/${postalCode}/`);
    }
    getBySlug(slug){
        return this.get(`${slug}/`);
    }
}

export default WhatToEatAPI;