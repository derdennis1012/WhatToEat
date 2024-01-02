from flask import current_app as app
from flask import Flask, request
from jose import jwt
from main import tools

class location:
    def __init__(self):
        self.defaults = {
            "last_updated": tools.nowDatetimeUTC(),
            "streetName": "",
            "streetNumber": "",
            "postalCode": "",
            "city": "",
            "country": "",
            "lat": "",
            "lng": "",
            "timeZone": ""
        }

class delivery:
    def __init__(self):
        self.defaults = {
            "last_updated": tools.nowDatetimeUTC(),
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
            "isOpenForOrder": True,
            "isOpenForPreorder": True,
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
            "last_updated": tools.nowDatetimeUTC(),
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
            "date_created": tools.nowDatetimeUTC(),
            "last_updated": tools.nowDatetimeUTC(),
            "restaurantId": "",
            "primarySlug": "",
            "name": "",
            "branchName": "",
            "restaurantPhoneNumber": "",
            "rating":   {"votes": "",
                        "score": ""},
            "location": location(),
            # Wann wird geliefert
            "delivery": delivery(),
            # Wann kann man abholen
            "pickup": delivery(),
            "menu": menu(),
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
            },
        }

    def get(self):
        token_data = jwt.decode(request.headers.get('AccessToken'), app.config['SECRET_KEY'])

        company = app.db.companies.find_one({ "id": token_data['company_id'] }, {
            "_id": 0,
            "password": 0
        })

        if company:
            resp = tools.JsonResp(company, 200)
        else:
            resp = tools.JsonResp({ "message": "Company not found" }, 404)

        return resp  
            
                
