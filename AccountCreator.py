# Title: Instagram Account Creator
# Author: Liam (scktz)
# Date: 11/05/2019
# Description: Create an Instagram account using the 
# Mobile API endpoints.

import requests
import hmac
import random
import string
import time
import hashlib
import json
import uuid

def HMAC(text):
    hash = hmac.new(b'3f0a7d75e094c7385e3dbaa026877f2e067cbd1a4dbcf3867748f6b26f257117', text.encode('utf-8'), hashlib.sha256)
    return hash.hexdigest()

def randomString(size):
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))

def createAccount(username, email, password, firstName):
    sessionHeaders = {
        'User-Agent':'Instagram 7.1.1 Android (21/5.0.2; 480dpi; 1080x1776; LGE/Google; Nexus 5; hammerhead; hammerhead; en_US)',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'en-US,en;q=0.8',
        'upgrade-insecure-requests':'1'
    }

    clientSession = requests.session()
    clientSession.get('https://instagram.com/', headers=sessionHeaders)

    clientGUID = randomString(8) + "-" + randomString(8) + "-" + randomString(4) + "-" + randomString(4) + "-" + randomString(4) + "-" + randomString(12)
    clientDeviceID = "android-" + str(HMAC(str(random.randint(1000,9999))))[0:min(64,16)]
    clientInformation = {
        'username': username,
        'first_name': firstName,
        'password': password,
        'email': email,
        'device_id': clientDeviceID,
        'guid': clientGUID
    }

    jsonInformation = json.dumps(clientInformation)
    clientSignedPayload = {
        'ig_sig_key_version': '4',
        'signed_body' : HMAC(jsonInformation) + "." + jsonInformation
    }

    createHeaders = {
        'Host':'i.instagram.com',
        'User-Agent':'Instagram 7.1.1 Android (21/5.0.2; 480dpi; 1080x1776; LGE/Google; Nexus 5; hammerhead; hammerhead; en_US)',
        'Accept-Language':'en-US',
        'Accept-Encoding':'gzip',
        'Cookie2':'$Version=1',
        'X-IG-Connection-Type':'WIFI',
        'X-IG-Capabilities':'BQ=='
    }

    editProxies = {
        'http' : 'http://loldongs:Dragons99@192.3.144.146:80',
        'https' : 'http://loldongs:Dragons99@192.3.144.146:80',
    }

    addressChecker = requests.get("http://icanhazip.com", proxies=editProxies).text
    print("[?] Address", addressChecker)

    createRequest = clientSession.post("https://i.instagram.com/api/v1/accounts/create/", data=clientSignedPayload, headers=createHeaders, proxies=editProxies)
    accountResponse = json.loads(createRequest.content)
    return accountResponse

def main():
    print(".: Instagram Account Creator :.\n")
    
    inputUsername = input(str("[?] Username: "))
    inputPassword = input(str("[?] Password: "))
    generatedEmail = "scktz{}@stabber.net".format(str(random.randint(1000, 9999)))

    print("\n[-] Attempting to create account.\n")
    makeAccount = createAccount(inputUsername, generatedEmail, inputPassword, 'PyCreator 1.0')
    
    if(makeAccount['account_created'] == True):
        print("[+] Account Created Successfully!")
        print("[-] https://instagr.am/{}".format(inputUsername))
    else:
        print("[-] Unable to register Account!")
    
main()
