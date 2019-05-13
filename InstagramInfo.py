import requests
import re
import json
import os
from bs4 import BeautifulSoup
import time

def retreiveUID(instagramUsername):
    requestURL = "https://www.instagram.com/{}".format(str(instagramUsername))
    sendRequest = requests.get(requestURL)
    try:
        soupInstance = BeautifulSoup(sendRequest.content, "lxml")
        findScript = soupInstance.find_all('script', type="text/javascript", text=re.compile('window._sharedData'))
        jsonOutput = findScript[0].get_text().replace('window._sharedData = ', '')[:-1]
        parseUID = json.loads(jsonOutput)['entry_data']['ProfilePage'][0]
        userID = parseUID["logging_page_id"].replace("profilePage_", "")

        return userID
    except:
        print("] Error: Username {} doesn't exist".format(str(instagramUsername)))

def retreiveInfo(instagramUserID):
    requestURL = "https://i.instagram.com/api/v1/users/{}/info/".format(str(instagramUserID))
    informationRequest = requests.get(requestURL).json()

    return informationRequest

def constructData(instagramUsername):
    parsedUserID = retreiveUID(instagramUsername)
    parsedAccountInfo = retreiveInfo(parsedUserID)['user']

    nameOnAccount = parsedAccountInfo['full_name']
    followersOnAccount = parsedAccountInfo['follower_count']
    followingOnAccount = parsedAccountInfo['following_count']
    avatarOnAccount = parsedAccountInfo['profile_pic_url']
    taggedPhotoCount = parsedAccountInfo['usertags_count']
    userBiography = parsedAccountInfo['biography']

    print("\n[-] Discoverd Information on: {}".format(str(instagramUsername)))
    print("[+] Name:", str(nameOnAccount))
    print("[+] Followers:", str(followersOnAccount))
    print("[+] Following:", str(followingOnAccount))
    print("[+] Profile Photo:", str(avatarOnAccount))
    print("[+] Profile Bio:", str(userBiography))
    print("[+] Tagged in {} Other Images".format(str(taggedPhotoCount)))

def parseFile(suppliedFile):
    parsedUsernames = []
    try:
        with open(suppliedFile, 'r') as accounts:
            for _ in accounts:
                splitLine = _.split()
                parsedUsernames.extend(splitLine)
            return parsedUsernames
    except FileNotFoundError:
        exit("  [-] File: {} could not be found!".format(str(suppliedFile)))

def banner():
    os.system('clear')
    print("Instagram Account Information Viewer")

def main():
    banner()
    fileChoice = input(str("[-] Import a file of usernames? [Y/n]: ")).upper()
    if(fileChoice == 'Y' or fileChoice == 'YES'):
        banner()

        fileName = input(str("[-] Filename: "))
        usernameList = parseFile(fileName)

        banner()
        if(len(usernameList) > 0):
            print("[-] {} Usernames Imported!".format(len(usernameList)))
            time.sleep(2)
        else:
            exit("[-] Error importing file")
        banner()
        for user in usernameList:
            constructData(user)
        print("\n[-] Finished Scraping Information")
    else:
        banner()
        targetUsername = input(str("[-] Instagram Username: "))
        constructData(targetUsername)
        print("\n[-] Finished Scraping Information")
main()
