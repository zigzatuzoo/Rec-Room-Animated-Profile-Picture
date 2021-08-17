import requests
import time

''' Stuff you need to update for this to work '''
userCookies = 'ARRAffinity=9d4f8c6d791fcb3cd5fdd416eb5c15cd8479b00ebabc0deb503b9fdce8c20c3c; ARRAffinitySameSite=9d4f8c6d791fcb3cd5fdd416eb5c15cd8479b00ebabc0deb503b9fdce8c20c3c; ai_user=6306LThwShjYfGm3V/ARdu|2021-08-14T02:14:23.594Z; __stripe_mid=c51a6b9d-b166-48dd-87ab-7750c17f9d9860990c; ai_session=fIj59WeLPXSWha8SI8eFBZ|1629160321507|1629160323589; __stripe_sid=8aa32273-df0a-437d-be71-139b51019aa9ce09b0; amplitude_id_e1693a1003671058b6abc356c8ba8d59rec.net=eyJkZXZpY2VJZCI6ImVmY2Q1YTMyLWQyZjItNGMwZi04MDBlLTcyMDA4Yzc0OThkMVIiLCJ1c2VySWQiOiIxNTY4MTMiLCJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOjE2MjkxNjAzMjA4OTcsImxhc3RFdmVudFRpbWUiOjE2MjkxNjAzMjQ2ODQsImV2ZW50SWQiOjE0NSwiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjE0NX0='
"This ^ userCookies variable is how Rec.Net knows that you are updating YOUR account, Currently i have it set to a default account @RecRoomAutomatedPFP if you want to mess around with it and see it in game before you put it on your account"

image1 = '2d83af05944d49c69fa9565fb238a91b.jpg'
image2 = '49b2788b672e4088a25eb0a9eff35c17.jpg'
image3 = '355c2c7e87f0489bb5f0308cdec108f6.jpg'
" ^ You need to change EACH of these to whatever you want the 3 pics to be"

''' Stuff that will change how the program works '''
speed = 0.2
"^ As you can probably guess, this changes how long the PFP stays on each image"

''' Just Initializing some values '''
x=0
BToken = ''


''' Making the strings into the format read by the rec.net image api '''
imageName1 = 'imageName=' + image1
imageName2 = 'imageName=' + image2
imageName3 = 'imageName=' + image3

''' Setting up the request header for the reauth script '''
authHeader= {'Host' : 'auth.rec.net',
             'Connection' : 'close',
             'sec-ch-ua' : '";Not A Brand";v="99", "Chromium",v="88"',
             'sec-ch-ua-mobile' : '?0',
             'Upgrade-Insecure-Requests' : '1',
             'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
             'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
             'Sec-Fetch-Site' : 'same-site',
             'Sec-Fetch-Mode' : 'navigate',
             'Sec-Fetch-Dest' : 'iframe',
             'Referer' : 'https://rec.net',
             'Accept-Encoding' : 'gzip, deflate',
             'Accept-Language' : 'en-US,en;q=0.9',
             'Cookie' : userCookies} 

''' Initial token request '''
authR = requests.get('https://auth.rec.net/connect/authorize?client_id=recnet&redirect_uri=https%3A%2F%2Frec.net%2Fauthenticate%2Fsilent&response_type=id_token%20token&scope=openid%20rn.api%20rn.notify%20rn.match.read%20rn.chat%20rn.accounts%20rn.auth%20rn.link%20rn.clubs%20rn.rooms&state=3b0bbf22ce1c40e7966dc6dd0f2df854&nonce=1ec7e44b909c416bbffae6b5e00ccb38&prompt=none', headers = authHeader, allow_redirects=True)
    
nonbtoken = authR.url[942:2038]
   
BToken = "Bearer " + nonbtoken + ""

print(BToken)

''' The loop program that actually makes the picure move '''
while 1 == 1:
    ''' The HTTP header for changing your In-Game pfp '''
    Headers = {'sec-ch-ua':'";Not A Brand";v="99", "Chromium";v="88"',
          'Accept' : '*/*',
          'sec-ch-ua-mobile' : '?0',
          'Authorization' : BToken,
          'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
          'Origin' : 'https://rec.net',
          'Sec-Fetch-Site' : 'same-site',
          'Sec-Fetch-Mode' : 'cors',
          'Sec-Fetch-Dest' : 'empty',
          'Referer' : 'https://rec.net/',
          'Accept-Encoding' : 'gzip, deflate',
          'Accept-Language' : 'en-US,en;q=0.9',
          }
    ''' The easy way to edit what pfp plays after what '''
    def i1():
        x = x + 1
        r = requests.put('https://accounts.rec.net/account/me/profileImage', headers = Headers, data = imageName1)
        print(str(r) + " num of requests: " + str(x))
        time.sleep(speed)
    def i2():
        x = x + 1
        r = requests.put('https://accounts.rec.net/account/me/profileImage', headers = Headers, data = imageName2)
        print(str(r) + " num of requests: " + str(x))
        time.sleep(speed)
    def i3():
        x = x + 1
        r = requests.put('https://accounts.rec.net/account/me/profileImage', headers = Headers, data = imageName3)
        print(str(r) + " num of requests: " + str(x))
        time.sleep(speed)
    
    ''' In this default format, it will show image 1 first, then image 2, then image 3, then image 2 again and will LOOP this '''
    i1()
    i2()
    i3()
    i2()
    
    ''' Requests a new auth token when that one is no longer valid '''
    r = requests.put('https://accounts.rec.net/account/me/profileImage', headers = Headers)

    if r.status_code == 401:
        print('Invalid Token')

        authR = requests.get('https://auth.rec.net/connect/authorize?client_id=recnet&redirect_uri=https%3A%2F%2Frec.net%2Fauthenticate%2Fsilent&response_type=id_token%20token&scope=openid%20rn.api%20rn.notify%20rn.match.read%20rn.chat%20rn.accounts%20rn.auth%20rn.link%20rn.clubs%20rn.rooms&state=3b0bbf22ce1c40e7966dc6dd0f2df854&nonce=1ec7e44b909c416bbffae6b5e00ccb38&prompt=none', headers = authHeader, allow_redirects=True)
    
        nonbtoken = authR.url[942:2038]
   
        BToken = "Bearer " + nonbtoken + ""

        print(BToken)
    