import requests
import time

''' Stuff you need to update for this to work '''
userCookies = 'ARRAffinity=a9d4cad7bd10f6fe1eb98ddbba36ff70b73ceb123fb4e398cf4ea51c69240ec9; ARRAffinitySameSite=a9d4cad7bd10f6fe1eb98ddbba36ff70b73ceb123fb4e398cf4ea51c69240ec9; amplitude_id_e1693a1003671058b6abc356c8ba8d59rec.net=eyJkZXZpY2VJZCI6IjVlOWQ5ZTZjLWRjZDEtNDAyNS05NTVhLWE1YzEzYjdhODhiZlIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTYyOTIxMjI5MTczNSwibGFzdEV2ZW50VGltZSI6MTYyOTIxMjI5MTczNiwiZXZlbnRJZCI6MSwiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjF9; .AspNetCore.Antiforgery.w5W7x28NAIs=CfDJ8MXx3-OwfdNOk2b7CQa2mdVT5jt0y9NQLMAUc28x9-N5ptsZi-iIXxXrq2NxrurMyvxZqS_QZcK9rhQzD515U4sNkRMLBPtAR5MoZT6hrd3fEv31HgQ3vg6v_iq1smglx38wGbnEPjScyLh0UwaBPGM; ai_user=EaPlitm3qcX5onP1YOqt2j|2021-08-17T14:58:14.979Z; ai_session=uN7F5aYy5QIrfFGyy2lFjA|1629212295587|1629212295587; idsrv.session=VUvbAs5P1QHdbbKAV2Tt7w; .AspNetCore.Identity.Application=CfDJ8MXx3-OwfdNOk2b7CQa2mdUPIEDv7e5qG68LMYXh-8MDpeE7STH1_TOIV6kEbg66ewcOUVtrVHloJILNWDh4aze8GYo4HjtnY6w6puyMoB0GwNf9a-IeteV0kY3_LYkLDgdpgubrsRseBrTpw-A2TqvaaMYYNM1q3ztGPiZAOTH9Op4YtbNVXN_EUJAQ-0uAptvItaTM9BdxxwYUX4Zhge-wtWQLGGTtmnOpNGWjMTDs4uMnEal35bRQBDnaJEtTACzMeDdCR9DjtEUoR6xN_GcSV3Pd7oVmko9qEU_gnYzdq2lSpiY7FC4owOeVgZWrv-jgg7PjQb2C4yOLtcm-mJY1uQUY8MGDTZqIxJZlIqN2hnJvYgBCQNpennJUJxyqqJhFIcOFgpSHRwcBL5ulXlaG1erY_7esGSVRBeaPKpXgNgv1qMAhkIUdEtOAw55p9kcsuxPgMVJN_V-uyc-IDo7szUkpzAHaxaRySZgnDdf7jcY0BPstwyblc12cDuX8WA8580SkqHJYzs-DCvGWfSxpdBd8C45C3SPbrnXC7425NY7m5Cw91gQ28VQPO5oveijPjBPve-eD7aXxoGZqxpj6TubFXPs-ZjZpbM6NGvKkyJzXs1xxkyo8uvV5Z6lzybtJYhhoxQy3vnigIi9AimpuPMGsKJVUam7YzBdKbbVlLG6rh3cPWob6tHhJRjDE5A; ARRAffinity=f9a15b6c249c0744b045bf29e58dcae139ef240f0e380839c73418245056289b; ARRAffinitySameSite=f9a15b6c249c0744b045bf29e58dcae139ef240f0e380839c73418245056289b'


"This ^ userCookies variable is how Rec.Net knows that you are updating YOUR account, Currently i have it set to a default account @RecRoomAutomatedPFP if you want to mess around with it and see it in game before you put it on your account"

image1 = '2d83af05944d49c69fa9565fb238a91b.jpg'
image2 = '49b2788b672e4088a25eb0a9eff35c17.jpg'
image3 = '355c2c7e87f0489bb5f0308cdec108f6.jpg'
" ^ You need to change EACH of these to whatever you want the 3 pics to be (Currently set to a waving red zigzag)"

''' Stuff that will change how the program works '''
speed = 0.2
"^ As you can probably guess, this changes how long the PFP stays on each image"

''' Just Initializing some values '''
x=0
BToken = ''
tc1 = 945
tc2 = 2025

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
    
nonbtoken = authR.url[tc1:tc2]
   
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
        r = requests.put('https://accounts.rec.net/account/me/profileImage', headers = Headers, data = imageName1)
        print(str(r) + " num of requests: " + str(x))
        time.sleep(speed)
    def i2():
        r = requests.put('https://accounts.rec.net/account/me/profileImage', headers = Headers, data = imageName2)
        print(str(r) + " num of requests: " + str(x))
        time.sleep(speed)
    def i3():
        r = requests.put('https://accounts.rec.net/account/me/profileImage', headers = Headers, data = imageName3)
        print(str(r) + " num of requests: " + str(x))
        time.sleep(speed)
    
    ''' In this default format, it will show image 1 first, then image 2, then image 3, then image 2 again and will LOOP this also the x = x + 1 is how the request counter adds 1 each time it makes a request '''
    i1()
    x = x + 1
    i2()
    x = x + 1
    i3()
    x = x + 1
    i2()
    x = x + 1
    
    ''' Requests a new auth token when that one is no longer valid '''
    r = requests.put('https://accounts.rec.net/account/me/profileImage', headers = Headers)

    if r.status_code == 401:
        print('Invalid Token')

        authR = requests.get('https://auth.rec.net/connect/authorize?client_id=recnet&redirect_uri=https%3A%2F%2Frec.net%2Fauthenticate%2Fsilent&response_type=id_token%20token&scope=openid%20rn.api%20rn.notify%20rn.match.read%20rn.chat%20rn.accounts%20rn.auth%20rn.link%20rn.clubs%20rn.rooms&state=3b0bbf22ce1c40e7966dc6dd0f2df854&nonce=1ec7e44b909c416bbffae6b5e00ccb38&prompt=none', headers = authHeader, allow_redirects=True)
    
        nonbtoken = authR.url[tokenCut]
   
        BToken = "Bearer " + nonbtoken + ""

        print(BToken)
        
    