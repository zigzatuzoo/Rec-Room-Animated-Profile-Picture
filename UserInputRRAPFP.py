import requests
import time

''' DISCLAMER THIS IS AN ACTIVE PROJECT THIS DOES NOT WORK IN ITS CURRENT STATE '''


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
speed = 1


''' starting questions '''
imageNum = input("How Many Images? 1-9")
imageOrder = array.array(input("What Order Do You Want The Images In? ex: 1,4,7,2,9,8,3 (no spaces in between the numbers"))
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
authPrompt = input("Please Input Your Auth Token. ex: Bearer (long string of numbers and leters here)")

userAuth = authPrompt

''' headers for the packet '''
Headers = {'sec-ch-ua':'";Not A Brand";v="99", "Chromium";v="88"',
          'Accept' : '*/*',
          'sec-ch-ua-mobile' : '?0',
          'Authorization' : userAuth,
          'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
          'Origin' : 'https://rec.net',
          'Sec-Fetch-Site' : 'same-site',
          'Sec-Fetch-Mode' : 'cors',
          'Sec-Fetch-Dest' : 'empty',
          'Referer' : 'https://rec.net/',
          'Accept-Encoding' : 'gzip, deflate',
          'Accept-Language' : 'en-US,en;q=0.9',
          }

''' defining the image requests '''
def imagePutRequest(imageNumber):
    r = requests.put('https://accounts.rec.net/account/me/profileImage', headers = Headers, data = imageNumber)
    print(r)



while 1 == 1:
    


    imagePutRequest()
    time.sleep(imageSpeed)