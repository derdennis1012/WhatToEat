from flask import current_app as app
from flask import request
from main import tools
import json
import requests
import datetime        

class Restaurant:
    def __init__(self):
        self._headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0',
            'Accept':'application/json, text/plain, */*',
            'Accept-Language':'de',
            'Accept-Encoding':'gzip, deflate, br',
            'Referer':'https://www.lieferando.de/',
            'X-Language-Code':'de',
            'X-Country-Code':'de',
            'X-Session-ID':'f5f08e76-a359-434d-899a-817c16ab679c',
            'X-Requested-With':'XMLHttpRequest',
            'Origin':'https://www.lieferando.de',
            'Connection':'keep-alive',
            'Sec-Fetch-Dest':'empty',
            'Sec-Fetch-Mode':'cors',
            'Sec-Fetch-Site':'cross-site',
            'TE':'trailers'}
        
        self._defaults = {
            "id": tools.randID(),
            "last_updated": tools.nowDatetimeUTC(),
            "restaurantId": "",
            "primarySlug": "",
            "name": "",
            "branchName": "",
            "restaurantPhoneNumber": "",
            "rating":   {"votes": "",
                        "score": ""},
            "location": {
                "streetName": "",
                "streetNumber": "",
                "postalCode": "",
                "city": "",
                "country": "",
                "lat": "",
                "lng": "",
                "timeZone": ""
            },
            # Wann wird geliefert
            "delivery": {},
            # Wann kann man abholen
            "pickup": {},
            "menu": {},
            "supports": {
                "delivery": True,
                "pickup": True,
                "stampCards": True,
                "vouchers": True,
                "productRemarks": True,
                "onlinePayments": True,
                "tipping": True
            },
            "payment": {
                "methods": [],
                "paymentMethodFees": {},
                "fees": [],
                "messages": {
                    "onlinePayment": [],
                    "offlinePayment": []
                },
                "issuers": {}
            }
        }

    def sendRestaurantRequest(self, slug):
        param = {'slug': slug}
        header = self._headers
        response = requests.get(url = 'https://cw-api.takeaway.com/api/v33/restaurant', params = param, headers = header)
        try:
            data = response.json()
            return data
        except:
            #return the error message
            return response.text

    def checkGetResponse(self, data):
        if type(data) is str:
            resp = tools.JsonResp(data, 400)
        else:
            self.insertRestaurant(data)
            resp = tools.JsonResp(data, 200)   
        return resp     

    def get(self, slug):
        restaurant = app.db.restaurants.find_one({ "primarySlug": slug})
        if restaurant:
            if restaurant['last_updated'] < datetime.datetime.now()-datetime.timedelta(days=1):
                app.db.restaurants.delete_one({ "primarySlug": slug})
                resp = self.checkGetResponse(self.sendRestaurantRequest(slug))    
            else: 
                resp = tools.JsonResp(restaurant, 200)    
        else:
            resp = self.checkGetResponse(self.sendRestaurantRequest(slug))
        return resp    
    
    def getArea(self, area):
        param = {'postalCode': area,
                 'isAccurate': False,
                 'filterShowTestRestaurants': False}
        header = self._headers
        response = requests.get(url = 'https://cw-api.takeaway.com/api/v33/restaurants', params = param, headers = header)
        try:
            data = response.json()
            resp = tools.JsonResp(data, 200)
            return resp
        except:
            return tools.JsonResp('Could not retrieve Restaurants in area code', 404)
            
    def insertRestaurant(self, data):
        expected_data = {
            "restaurantId": data["restaurantId"],
            "primarySlug": data["primarySlug"],
            "name": data["brand"]["name"],
            "branchName": data["brand"]["branchName"],
            "restaurantPhoneNumber": data["restaurantPhoneNumber"],
            "rating":   {"votes": data["rating"]["votes"],
                        "score": data["rating"]["score"]},
            "location": {
                "streetName": data["location"]["streetName"],
                "streetNumber": data["location"]["streetNumber"],
                "postalCode": data["location"]["postalCode"],
                "city": data["location"]["city"],
                "country": data["location"]["country"],
                "lat": data["location"]["lat"],
                "lng": data["location"]["lng"],
                "timeZone": data["location"]["timeZone"]
            },
            "delivery": data["delivery"],
            "pickup": data["pickup"],
            "menu": data["menu"],
            "supports": {
                "delivery": data["supports"]["delivery"],
                "pickup": data["supports"]["pickup"],
                "stampCards": data["supports"]["stampCards"],
                "vouchers": data["supports"]["vouchers"],
                "productRemarks": data["supports"]["productRemarks"],
                "onlinePayments": data["supports"]["onlinePayments"],
                "tipping": data["supports"]["tipping"]
            },
            "payment": {
                "methods": data["payment"]["methods"],
                "paymentMethodFees": data["payment"]["paymentMethodFees"],
                "fees": data["payment"]["fees"],
                "messages": {
                    "onlinePayment": data["payment"]["messages"]["onlinePayment"],
                    "offlinePayment": data["payment"]["messages"]["offlinePayment"]
                },
                "issuers": data["payment"]["issuers"]
            }
        }

        self._defaults.update(expected_data)

        id_as_str = str(expected_data['restaurantId'])
        restaurant = app.db.restaurants.find_one({ "id": id_as_str})
        if restaurant:
            if app.db.restaurants.update_one({ "id": id_as_str}, { "$set": self._defaults }):
                resp = tools.JsonResp({ "message": "Restaurant updated" }, 200)
            else: 
                resp = tools.JsonResp({ "message": "Restaurant not updated" }, 400)      
        else:
            if app.db.restaurants.insert_one(self._defaults):
                resp = tools.JsonResp({ "message": "Restaurant added" }, 201)
            else:
                resp = tools.JsonResp({ "message": "Restaurant not added" }, 400)    

        return resp
    
    def add(self):
        data = json.loads(request.data)
        return self.insertRestaurant(data)  

    def addAll(self):
        data = json.loads(request.data)
        if data["restaurants"] is None:
            resp = tools.JsonResp({ "message": "No restaurant data was sent" }, 400)
        else:
            for restaurant in data["restaurants"]:
                self.insertRestaurant(restaurant)
            resp = tools.JsonResp({ "message": "Restaurants added" }, 201)    
        return resp

    def delete(self, restaurantId):
        restaurant = app.db.restaurants.find_one({ "id": restaurantId})
        if restaurant:
            if app.db.restaurants.delete_one({ "id": restaurantId}):
                resp = tools.JsonResp({ "message": "Restaurant deleted" }, 200)
            else: 
                resp = tools.JsonResp({ "message": "Restaurant not deleted" }, 400)      
        else:
            resp = tools.JsonResp({ "message": "Restaurant not found" }, 404)    

        return resp        

    def deleteAll(self):
        if app.db.restaurants.delete_many({}):
            resp = tools.JsonResp({ "message": "Restaurants deleted" }, 200)
        else: 
            resp = tools.JsonResp({ "message": "Restaurants not deleted" }, 400)      

        return resp

