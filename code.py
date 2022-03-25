import urllib.request, urllib.parse, urllib.error
import json

barcode = input("Enter Barcode: ")
serviceurl = "https://world.openfoodfacts.org/api/v0/product/"+barcode+".json"

uh = urllib.request.urlopen(serviceurl)
data = uh.read()
js = json.loads(data)


print("ingredients: ", js["product"]["ingredients_text"])
