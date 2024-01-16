class WhatToEatAPI{
    //constructor
    constructor(){
        this.url = "http://localhost:5555/";
        this.auth = new AuthAPI();
        this.restaurant = new RestaurantAPI();
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

class AuthAPI extends APIUtils{
    //constructor
    constructor(){
        super();
        this.url = "http://localhost:5555/user/"
    }
    login(data){
        return this.post("login", data);
    }
}

class RestaurantAPI extends APIUtils{
    //constructor
    constructor(){
        super();
        this.url = "restaurant/"
    }
    searchByPostalCode(postalCode){
        return this.get(`postcode/${postalCode}`);
    }
}

export default WhatToEatAPI;