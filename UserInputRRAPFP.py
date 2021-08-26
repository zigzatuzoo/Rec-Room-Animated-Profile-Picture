import requests
import time

''' DISCLAMER THIS IS AN ACTIVE PROJECT THIS DOES NOT WORK IN ITS CURRENT STATE '''

infoFile = open('info.txt')


''' initializing the values '''
image1 = ''
image2 = ''
image3 = ''
image4 = ''
image5 = ''
image6 = ''
image7 = ''
image8 = ''
image9 = ''
imageNumber = 0
currentImage = 0
imageSpeed = 1
imageIndex = 1

''' starting questions '''
imageOrder = array.array(input("What Order Do You Want The Images In? ex: 1,4,7,2,9,8,3 (no spaces in between the numbers"))

if infoFile.redline(0) != '':
    imageInput = input('Images saved, would you like to change the images? y or n.')
    if imageInput == 'y':
        print("To get the image names, go to the picture you want on rec.net and right click it to open it in a new tab. In the url it will show the image name. The url should be img.rec.net/(Insert Random Numbers And Letters Here).jpg")
        image1 = input("What Is The First Image Name? (If Not Used Leave Blank)")
        
        image2 = input("What Is The Second Image Name? (If Not Used Leave Blank)")
        image3 = input("What Is The Third Image Name? (If Not Used Leave Blank)")
        image4 = input("What Is The Fourth Image Name? (If Not Used Leave Blank)")
        image5 = input("What Is The Fifth Image Name? (If Not Used Leave Blank)")
        image6 = input("What Is The Sixth Image Name? (If Not Used Leave Blank)")
        image7 = input("What Is The Seventh Image Name? (If Not Used Leave Blank)")
        image8 = input("What Is The Eighth Image Name? (If Not Used Leave Blank)")
        image9 = input("What Is The Nineth Image Name? (If Not Used Leave Blank)")
        imageSpeed = input("How Long Do You Want The Images To Be On Your Profile? (The number that you put will be the amount of seconds it takes to change to the next image, minimum of 0.8, maximum of ... whatever you want honestly.")
        cookiePrompt = input("Please Input Your Auth Cookie.")
        infoFile.writelines({0 : 'active',
                            1 : image1,
                            2 : image2,
                            3 : image3, 
                            4 : image4, 
                            5 : image5, 
                            6 : image6, 
                            7 : image7, 
                            8 : image8, 
                            9 : image9, 
                            10 : imageSpeed,
                            11 : cookiePrompt})

    if imageInput == 'n':
        print("Okay, continuing.")
if infoFile.readline(1) == '':
    print("To get the image names, go to the picture you want on rec.net and right click it to open it in a new tab. In the url it will show the image name. The url should be img.rec.net/(Insert Random Numbers And Letters Here).jpg")
    image1 = input("What Is The First Image Name? (If Not Used Leave Blank)")
    image2 = input("What Is The Second Image Name? (If Not Used Leave Blank)")
    image3 = input("What Is The Third Image Name? (If Not Used Leave Blank)")
    image4 = input("What Is The Fourth Image Name? (If Not Used Leave Blank)")
    image5 = input("What Is The Fifth Image Name? (If Not Used Leave Blank)")
    image6 = input("What Is The Sixth Image Name? (If Not Used Leave Blank)")
    image7 = input("What Is The Seventh Image Name? (If Not Used Leave Blank)")
    image8 = input("What Is The Eighth Image Name? (If Not Used Leave Blank)")
    image9 = input("What Is The Nineth Image Name? (If Not Used Leave Blank)")
    imageSpeed = input("How Long Do You Want The Images To Be On Your Profile? (The number that you put will be the amount of seconds it takes to change to the next image, minimum of 0.8, maximum of ... whatever you want honestly.")
    cookiePrompt = input("Please Input Your Auth Cookie.")
    infoFile.writelines({0 : 'active',
                         1 : image1,
                         2 : image2,
                         3 : image3, 
                         4 : image4, 
                         5 : image5, 
                         6 : image6, 
                         7 : image7, 
                         8 : image8, 
                         9 : image9, 
                         10 : imageSpeed,
                         11 : cookiePrompt})

image1 = infoFile.readline(1)
image2 = infoFile.readline(2)
image3 = infoFile.readline(3)
image4 = infoFile.readline(4)
image5 = infoFile.readline(5)
image6 = infoFile.readline(6)
image7 = infoFile.readline(7)
image8 = infoFile.readline(8)
image9 = infoFile.readline(9)
imageSpeed = infoFile.readline(10)
cookiePrompt = infoFile.readline(11)

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
             'Cookie' : userCookie
             }

x = 0
''' defining the image requests '''
def imagePutRequest(imageNumber):
    if x == 0:
        authR = requests.get('https://auth.rec.net/connect/authorize?client_id=recnet&redirect_uri=https%3A%2F%2Frec.net%2Fauthenticate%2Fsilent&response_type=id_token%20token&scope=openid%20rn.api%20rn.notify%20rn.match.read%20rn.chat%20rn.accounts%20rn.auth%20rn.link%20rn.clubs%20rn.rooms&state=3b0bbf22ce1c40e7966dc6dd0f2df854&nonce=1ec7e44b909c416bbffae6b5e00ccb38&prompt=none', headers = authHeader, allow_redirects=True)
    
        nonbtoken = authR.url[945:2025]
    
        BToken = "Bearer " + nonbtoken

        "The BToken var is your Bearer Token that you need to make most requests to any rec.net api"
        print("Token: " + BToken)

        ''' headers for the packet '''
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
        x = 1
    
    r = requests.put('https://accounts.rec.net/account/me/profileImage', headers = Headers, data = imageNumber)
    print(r)
    if r.statuscode != '200':
        x = 0


while 1 == 1:
    currentImage = imageOrder[imageIndex]
    if currentImage == 1:
        imageNumber = image1
    elif currentImage == 2:
        imageNumber = image2
    elif currentImage == 3:
        imageNumber = image3
    elif currentImage == 4:
        imageNumber = image4
    elif currentImage == 5:
        imageNumber = image5
    elif currentImage == 6:
        imageNumber = image6
    elif currentImage == 7:
        imageNumber = image7
    elif currentImage == 8:
        imageNumber = image8
    elif currentImage == 9:
        imageNumber = image9
    else:
        print("error")

    imagePutRequest(imageNumber)
    imageIndex = imageIndex + 2
    time.sleep(imageSpeed)