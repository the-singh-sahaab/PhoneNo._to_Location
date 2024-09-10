
#  this program will give out yhr loaction of your phone number but only the loaction 

import phonenumbers
from track import phone_number
from phonenumbers import geocoder
from phonenumbers import carrier
import opencage
from opencage.geocoder import OpenCageGeocode
import folium
 
pepnumber = phonenumbers.parse(phone_number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)
service_pro = phonenumbers.parse(phone_number)

print(carrier.name_for_number(service_pro,"en"))

key = "f5b7de006ad94441897c218681d79034"
geocoder = OpenCageGeocode(key)

query = str(location)
results = geocoder.geocode(query)
# print(results)

lat = results[0]["geometry"]["lat"]
lng = results[0]["geometry"]["lng"]

print(lat, lng)

my_map = folium.Map(location = [lat, lng], zoom_start = 10)
folium.Marker([lat, lng], popup = location).add_to(my_map)

my_map.save("try_project\P19_LOCATON\my_location.html")