import phonenumbers
from phonenumbers import geocoder, carrier, timezone

phone_number=input("enter phone number that you want to track")
phone_number1=phonenumbers.parse(phone_number)

print(geocoder.description_for_number(phone_number1, 'en'))

print(carrier.name_for_number(phone_number1, 'en'))

print(timezone.time_zones_for_number(phone_number1))