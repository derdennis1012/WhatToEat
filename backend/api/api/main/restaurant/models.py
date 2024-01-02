from flask import current_app as app
from flask import Flask, request
from jose import jwt
from main import tools
import json

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

class restaurant:
    def __init__(self):
        self.defaults = {
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

    def get(self):
        token_data = jwt.decode(request.headers.get('AccessToken'), app.config['SECRET_KEY'])

        restaurant = app.db.restaurant.find_one({ "id": token_data['restaurant_id'] }, {
            "_id": 0,
            "password": 0
        })

        if restaurant:
            resp = tools.JsonResp(restaurant, 200)
        else:
            resp = tools.JsonResp({ "message": "Restaurant not found" }, 404)

        return resp  
            
    def add(self):
        data = json.loads(request.data)

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
        restaurant = app.db.restaurants.find_one({ "id": app.ObjectId(id_as_str)})
        if restaurant:
            if app.db.restaurants.update_one({ "id": app.ObjectId(id_as_str)}, { "$set": self.defaults }):
                resp = tools.JsonResp({ "message": "Restaurant updated" }, 200)
            else: 
                resp = tools.JsonResp({ "message": "Restaurant not updated" }, 400)      
        else:
            if app.db.companies.insert_one(restaurant):
                resp = tools.JsonResp({ "message": "Restaurant added" }, 201)
            else:
                resp = tools.JsonResp({ "message": "Restaurant not added" }, 400)    

        return resp
