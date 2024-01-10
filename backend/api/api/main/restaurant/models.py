from flask import current_app as app
from flask import request
from bson.json_util import dumps
from main import tools
import json
import requests

class delivery:
    def __init__(self):
        self.defaults = {
            "times": {
                "0": [
                    {
                    "start": "",
                    "end": ""
                    }
                ],
                "1": [
                    {
                    "start": "",
                    "end": ""
                    }
                ],
                "2": [
                    {
                    "start": "",
                    "end": ""
                    }
                ],
                "3": [
                    {
                    "start": "",
                    "end": ""
                    }
                ],
                "4": [
                    {
                    "start": "",
                    "end": ""
                    }
                ],
                "5": [
                    {
                    "start": "",
                    "end": ""
                    }
                ],
                "6": [
                    {
                    "start": "",
                    "end": ""
                    }
                ],
            },
            "isOpenForOrder": False,
            "isOpenForPreorder": False,
            "durationRange": {
                "min": 0,
                "max": 0
            }
        }    

class optionGroup:
    def __init__(self):
        self.defaults = {
            "name": "",
            "isTypeMulti": False,
            "isRequired": True,
            "minChoices": 1,
            "maxChoices": 1,
            # List of option
            "optionIds": []
        }        

class option:
    def __init__(self):
        self.defaults = {
            "name": "",
            "minAmount": 1,
            "maxAmount": 1,
            "prices": {
                "delivery": 0,
                "pickup": 0,
                "deposit": 0
            },
            "metric": {
                "unit": "",
                "quantity": 0
            },
            "priceUnit": "",
            "pricePerUnitPickup": None,
            "pricePerUnitDelivery": None,
            "alcoholVolume": None,
            "caffeineAmount": "",
            "isSoldOut": False,
            "isExcludedFromMov": False
        }        

class productVariant:
    def __init__(self):
        self.defaults = {
            "id": "",
            "name": "",
            "optionGroupIds": [],
            "shippingTypes": [],
            "prices": {
                "delivery": 0,
                "pickup": 0,
                "deposit": 0
            },
            "metric": {
                "unit": "",
                "quantity": 0
            },
            "priceUnit": "",
            "pricePerUnitPickup": None,
            "pricePerUnitDelivery": None,
            "alcoholVolume": None,
            "caffeineAmount": "",
            "isSoldOut": False,
            "isExcludedFromMov": False
        }        

class product:
    def __init__(self):
        self.defaults = {
            "name": "",
            "description": [],
            "imageUrl": None,
            # List of productVariant
            "variants": []
        }        

class category:
    def __init__(self):
        self.defaults = {
            "id": "",
            "name": "",
            "description": [],
            "timeRestrictions": {},
            "productIds": [],
        }        

class menu:
    def __init__(self):
        self.defaults = {
            "currency": {
                "denominator": 0,
                "code": ""
            },            
            # List of category
            "categories": [],
            # Dicionary of optionGroup ("optionGroupId": optionGroup())
            "optionGroups": {},
            # Dicionary of option ("optionId": option())
            "options": {},
            # Dicionary of product ("productId": product())
            "products": {},
            "popularProductIds": [],
            "discounts": []
        }           

class Restaurant:
    def __init__(self):
        self.defaults = {
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

    def get(self):
        # extract the parameter sent with the get request
#        restaurantId = request.args.get('restaurantId')

#        restaurant = app.db.restaurants.find_one({ "restaurantId": restaurantId })
        
        param = {'slug': request.args.get('primarySlug')}
        header = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0',
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
            'TE':'trailers',
            'Cookie':'__cf_bm=1JYIrMHX.NiQ4UqiCzQJqstHubz4g03UtihYChOyQ1c-1704872334-1-AYxyh9kPUmSCEumnxqBF5WYs08yej067FYp/wpVvpiHqmsNYvf0U8euWUv6RciquWzfyTj4g4LU2YS0seuvDf1dUIZcXuWEex1WfHS7CSb06; Path=/;' +
            'Domain=takeaway.com; Secure; HttpOnly; Expires=Wed, 10 Jan 2024 08:08:54 GMT;'}
        response = requests.get(url = 'https://cw-api.takeaway.com/api/v33/restaurant', params = param, headers = header)
        data = response.json()
        self.insertRestaurant(data)
        resp = tools.JsonResp(data, 200)

#        if restaurant:
#            resp = tools.JsonResp(restaurant, 200)
#        else:
#            resp = tools.JsonResp({ "message": "Restaurant not found" }, 404)

        return resp  
        

    def getAll(self):
        cursor = app.db.restaurants.find({})
        list_cur = list(cursor)
        restaurants = json.loads(dumps(list_cur))
        if restaurants:
            resp = tools.JsonResp(restaurants, 200)
        else:
            resp = tools.JsonResp({ "message": "No restaurants found" }, 404)

        return resp    
            
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

        self.defaults.update(expected_data)

        id_as_str = str(expected_data['restaurantId'])
        restaurant = app.db.restaurants.find_one({ "id": id_as_str})
        if restaurant:
            if app.db.restaurants.update_one({ "id": id_as_str}, { "$set": self.defaults }):
                resp = tools.JsonResp({ "message": "Restaurant updated" }, 200)
            else: 
                resp = tools.JsonResp({ "message": "Restaurant not updated" }, 400)      
        else:
            if app.db.restaurants.insert_one(self.defaults):
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

    def delete(self):
        restaurantId = request.args.get('restaurantId')
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

