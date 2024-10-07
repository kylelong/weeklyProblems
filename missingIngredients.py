from datetime import datetime

# date tested 10/7/2024

def fresh(date):
    today = datetime.now()
    return datetime.strptime(date, "%m/%d/%Y") >= today

def missing(recipe, pantry):
    fresh_pantry = {item["ingredient"] for item in pantry if fresh(item["expDate"])}
    return sum(ingredient not in fresh_pantry for ingredient in recipe)
            

assert missing(["eggs", "flour", "sugar", "butter"],
                [{"ingredient": "sugar", "expDate": "01/28/2025"},
                   {"ingredient": "butter", "expDate": "09/15/2024"},
                     {"ingredient": "milk", "expDate": "10/01/2024"}] ) == 3

assert missing(["eggs", "flour", "sugar", "butter"],
                [{"ingredient": "sugar", "expDate": "01/28/2025"},
                   {"ingredient": "butter", "expDate": "12/15/2024"},
                     {"ingredient": "milk", "expDate": "10/01/2024"}] ) == 2

assert missing(["eggs", "flour", "sugar", "butter"],
                [{"ingredient": "sugar", "expDate": "01/28/2012"},
                   {"ingredient": "butter", "expDate": "03/15/2020"},
                     {"ingredient": "milk", "expDate": "10/23/2024"}] ) == 4