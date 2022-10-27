thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

dict = {
"name" : "Jay",
"age" : 20,
"year" : 2002,
"class" : "BSCS"
}
x = dict.keys()
print(x)

car = {
"brand": "Suzuki",
"model": "Alto",
"year": 2017
}
x = car.keys()
print(x)
car["color"] = "white"
print(x) 


car = {
"brand": "Suzuki",
"model": "Alto",
"year": 2017
}
x = car.values()
print(x)

carmodel = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in carmodel:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


