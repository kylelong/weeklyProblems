from typing import Dict, Union, List
def recipe(ingredients: List[Dict[str, Union[str, int]]], targetServings: int):
    res = [{**ingredient, "amount": ingredient['amount'] * targetServings} for ingredient in ingredients]
    return res

ingredients = [
  { "name": "flour", "amount": 200 }, # 200g per
  { "name": "sugar","amount": 100 }, # 100g per
  {"name": "eggs", "amount": 2 }     # 2 eggs per
]
targetServings = 3

expected =  [
  { "name": "flour", "amount": 600 }, # 600g per
  { "name": "sugar","amount": 300 }, # 300g per
  {"name": "eggs", "amount": 6 }     # 6 eggs per
]

assert recipe(ingredients, targetServings) == expected