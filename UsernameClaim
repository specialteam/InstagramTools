# Title: Instagram Username Swapper
# Author: Liam (scktz)
# Date: 11/05/2019
# Description: Target an Instagram username and swap to that username
# once it becomes available for use.

import requests
import uuid
import sys
import random
import time
from platform import python_version
from itertools import cycle

if(int(python_version()[0]) < 3):
    exit("[!] Please use Python 3")

if(len(sys.argv) < 6):
    exit("* Usage: {} username password target threads sleep".format(sys.argv[0]))

loginUUID = str(uuid.uuid4())
loginUsername = str(sys.argv[1])
loginPassword = str(sys.argv[2])
targetUsername = str(sys.argv[3])
threadCount = str(sys.argv[4])
sleepCount = str(sys.argv[5])

# Set up username list for imported file
usernameList = []

def parseFile(userFile):
    try:
        with open(userFile, 'r') as usernameFile:
            for username in usernameFile:
                currentTarget = username.split()
                usernameList.extend(currentTarget)
        return usernameList
    except FileNotFoundError:
        exit("[!] {} not found!".format(str(userFile)))

def instagramLogin(clientUUID, clientUsername, clientPassword):
    loginData = {
        "ig_sig_key_version" : "5",
        "signed_body": "fa61f4be32e827c7152e38a075e36142d8313ba582d6437f07539b00a03f454e.{\"reg_login\":\"0\",\"password\":\""+clientPassword+"\",\"device_id\":\""+clientUUID+"\",\"username\":\""+clientUsername+"\",\"adid\":\"FE4FD084-9DCB-481A-A248-57E0E32E25ED\",\"login_attempt_count\":\"0\",\"phone_id\":\""+clientUUID+"\"}"
    }

    loginHeaders = {
        "Accept": "*/*",
        "X-IG-Capabilities": "36r/Vw==",
        "User-Agent": "Instagram 82.0.0.17.95 (iPhone9,3; iOS 12_0; en_US; en-US; scale=2.00; gamut=wide; 750x1334) AppleWebKit/420+",
        "Connection": "close",
        "X-IG-ABR-Connection-Speed-KBPS": "0",
        "X-IG-Connection-Speed": "-1kbps",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"en-US;q=1",
        "X-IG-Connection-Type":"WiFi",
        "X-IG-App-ID":"124024574287414",
        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"
    }

    loginRequest = requests.post("https://i.instagram.com/api/v1/accounts/login/", data=loginData, headers=loginHeaders)
    if("logged_in_user" in loginRequest.content.decode('utf-8')):

        parsedSessionID = loginRequest.cookies['sessionid']
        parsedCSRFToken = loginRequest.cookies['csrftoken']
        parsedDSUserID = loginRequest.cookies['ds_user_id']
        parsedMID = loginRequest.cookies['mid']

        return parsedSessionID, parsedCSRFToken, parsedDSUserID, parsedMID
    else:
        print("Unable to login!")

def instagramEdit(clientUUID, clientUsername, clientPassword, clientTarget, clientEmail, clientSessionID, clientCSRFToken, clientDSUserID, clientMID, proxyServer):
    editData = {
        "ig_sig_key_version": "5",
        "signed_body": "66ab4c58537eead820f066daecac18eb319af61529d3da92845e9ed7d811bcd5.{\"gender\":\"3\",\"_csrftoken\":\""+clientCSRFToken+"\",\"_uuid\":\""+clientUUID+"\",\"_uid\":\""+clientDSUserID+"\",\"external_url\":\"\",\"username\":\""+clientTarget+"\",\"email\":\""+clientEmail+"\",\"phone_number\":\"\",\"biography\":\"\",\"first_name\":\"\"}"
    }

    editHeaders = {
        "Accept": "*/*",
        "X-IG-Capabilities": "36r/Bw==",
        "User-Agent": "Instagram 82.0.0.12.95 (iPhone9,3; iOS 12_0; en_US; en-US; scale=2.00; gamut=wide; 750x1334) AppleWebKit/420+",
        "Connection": "close",
        "X-IG-ABR-Connection-Speed-KBPS": "0",
        "X-IG-Connection-Speed": "319kbps",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US;q=1",
        "X-IG-Connection-Type": "WiFi",
        "X-IG-App-ID": "124024574287414",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
    editCookies = {
        "urlgen": "\"{\\\"107.99.45.23\\\": 7922\\054 \\\"2601:2c3:877f:db78:835:4e84:b991:95f6\\\": 7922}:1h4px5:GmcZFuickg3NXINWN7E4OhGsdLc\"",
        "igfl": clientUsername,
        "ds_user": clientUsername,
        "ds_user_id": clientDSUserID,
        "mid": clientMID,
        "shbts":"1552658440.473448",
        "sessionid": clientSessionID,
        "csrftoken": clientCSRFToken,
        "shbid":"15035",
        "rur":"ATN",
        "is_starred_enabled":"yes"
    }

    editRequest = requests.post("https://i.instagram.com/api/v1/accounts/edit_profile/", data=editData, headers=editHeaders, cookies=editCookies, proxies={'https': str(proxyServer)}).content.decode('utf-8')
    return editRequest


def main():
    createUserSession = instagramLogin(loginUUID, loginUsername, loginPassword)

    validSessionID = createUserSession[0]
    validCSRFToken = createUserSession[1]
    validDSUserID = createUserSession[2]
    validMID = createUserSession[3]

    validEmail = "stbr{}@stabber.net".format(random.randint(0, 1337))

    userProxies = [
        'http://hacker-nxlsu:ZKYpfuxBls@168.81.84.151:3199', 
        'http://hacker-nxlsu:ZKYpfuxBls@196.16.169.206:3199',
        'http://hacker-nxlsu:ZKYpfuxBls@196.16.169.206:3199',
        'http://hacker-nxlsu:ZKYpfuxBls@186.179.27.61:3199',
        'http://hacker-nxlsu:ZKYpfuxBls@168.81.38.60:3199',
        'http://hacker-nxlsu:ZKYpfuxBls@196.18.178.185:3199',
        'http://hacker-nxlsu:ZKYpfuxBls@168.80.244.233:3199',
        'http://hacker-nxlsu:ZKYpfuxBls@168.80.38.87:3199',
        'http://hacker-nxlsu:ZKYpfuxBls@196.19.136.2:3199'
    ]

    userProxyPool = cycle(userProxies)
    requestCounter = 0

    # Check to see if we imported a file or not.
    if(".txt" in targetUsername):
        # Call file parser to parse usernames out of our file and start loop
        parseFile(targetUsername)
        while True:
            try:
                proxyConnection = next(userProxyPool)
                time.sleep(1)
                for x in usernameList:
                    editClientProfile = instagramEdit(loginUUID, loginUsername, loginPassword, x, validEmail, validSessionID, validCSRFToken, validDSUserID, validMID, proxyConnection)
                    if("spam" in str(editClientProfile)):
                        print("[?] {} : Rate Limited!".format(x))
                    elif("ok" in str(editClientProfile)):
                        print("[?] {} has been claimed!".format(x))
                    else:
                        requestCounter += 1
                        print("[?] {} - {} ".format(requestCounter, x))
            except KeyboardInterrupt:
                exit()
    else:
        while True:
            try:
                proxyConnection = next(userProxyPool)
                time.sleep(1)
                editClientProfile = instagramEdit(loginUUID, loginUsername, loginPassword, targetUsername, validEmail, validSessionID, validCSRFToken, validDSUserID, validMID, proxyConnection)
                if("spam" in str(editClientProfile)):
                    print("[?] {} : Rate Limited!".format(targetUsername))
                elif("ok" in str(editClientProfile)):
                    print("[?] {} has been claimed!".format(targetUsername))
                else:
                    requestCounter += 1
                    print("[?] {} - {} ".format(requestCounter, targetUsername))
            except KeyboardInterrupt:
                exit()

# Start program
main()
