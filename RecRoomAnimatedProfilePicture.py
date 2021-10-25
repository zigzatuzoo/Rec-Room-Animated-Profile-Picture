''' Stuff you need to update for this to work '''
'Enter your username here'
user = ''
'Enter your password here'
passwd = ''

login = rnl.login_to_recnet(username=user,password=passwd)

image1 = '2d83af05944d49c69fa9565fb238a91b.jpg'
image2 = '49b2788b672e4088a25eb0a9eff35c17.jpg'
image3 = '355c2c7e87f0489bb5f0308cdec108f6.jpg'
" ^ You need to change EACH of these to whatever you want the 3 pics to be (Currently set to a waving red zigzag)"

''' Stuff that will change how the program works '''
speed = 0.2
"^ As you can probably guess, this changes how long the PFP stays on each image"

import time
try:
    import requests
except:
    print('''You do not have the requests library installed, you need to install it via the following command:
        pip install requests
    Thank you!''')
try:
    import recnetlogin as rnl
except:
    print('''You do not have the RecNetLogin package installed, you need to install it via the following command:
        python -m pip install git+https://github.com/Jegarde/RecNet-Login.git#egg=recnetlogin
    Thank you!''')

''' Just Initializing some values '''
x = 1
BToken = ''

''' Making the strings into the format read by the rec.net image api '''
imageName1 = 'imageName=' + image1
imageName2 = 'imageName=' + image2
imageName3 = 'imageName=' + image3

''' Initial token request '''
BToken = "Bearer " + login.access_token

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
    def i1(x):
        r = requests.put('https://accounts.rec.net/account/me/profileImage', headers = Headers, data = imageName1)
        print(str(r) + " num of requests: " + str(x))
        time.sleep(speed)
        x = x + 1
    def i2(x):
        x = x + 1
        r = requests.put('https://accounts.rec.net/account/me/profileImage', headers = Headers, data = imageName2)
        print(str(r) + " num of requests: " + str(x))
        time.sleep(speed)
    def i3(x):
        x = x + 1
        r = requests.put('https://accounts.rec.net/account/me/profileImage', headers = Headers, data = imageName3)
        print(str(r) + " num of requests: " + str(x))
        time.sleep(speed)
    
    ''' In this default format, it will show image 1 first, then image 2, then image 3, then image 2 again and will LOOP this. The x value in the function calls is to make the counter function, if you don't add it to your function calls or you delete them, THE COUNTER WILL NOT WORK. '''
    i1(x)
    i2(x)
    i3(x)
    i2(x)
    
    ''' Requests a new auth token when that one is no longer valid '''
    r = requests.put('https://accounts.rec.net/account/me/profileImage', headers = Headers)

    if r.status_code == 401:
        print('Invalid Token')
        login = rnl.login_to_recnet(username=user,password=passwd)
        BToken = "Bearer " + login.access_token

        print(BToken)