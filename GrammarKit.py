import requests
import time
import random
import json
import os
import requests
import _thread
import base64
import uuid
import hashlib
from hashlib import sha256
import re
import time
import ctypes
from threading import Thread
import random
from itertools import cycle
from bs4 import BeautifulSoup

# Set up username list for imported file
targetList = []

def banner():
    programArt = """
    
 ██████╗ ██████╗  █████╗ ███╗   ███╗███╗   ███╗ █████╗ ██████╗ 
██╔════╝ ██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔══██╗██╔══██╗
██║  ███╗██████╔╝███████║██╔████╔██║██╔████╔██║███████║██████╔╝
██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══██║██╔══██╗
╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║██║  ██║██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
  [-] a simple instagram toolkit, made with <3 by scktz [-]
    """
    print(programArt)

def getPremiumProxies():
    url = 'http://falcon.proxyrotator.com:51337/proxy-list/'

    params = dict(
        apiKey='9EKVT48tBSANFXkxWbeMhCUZqwzypfPa'
    )

    resp = requests.get(url=url, params=params).text
    return resp

def createProxyManager():
    dreamProxies = [
        'http://loldongs:Dragons99@154.16.91.15:80',
        'http://loldongs:Dragons99@198.23.238.83:80',
        'http://loldongs:Dragons99@107.172.181.169:80',
        'http://loldongs:Dragons99@172.245.254.181:80',
        'http://loldongs:Dragons99@104.160.4.154:80',
        'http://loldongs:Dragons99@198.12.66.156:80',
        'http://loldongs:Dragons99@104.160.4.91:80',
        'http://loldongs:Dragons99@192.3.144.146:80',
        'http://loldongs:Dragons99@185.207.177.211:80',
        'http://loldongs:Dragons99@185.207.177.204:80'
    ]

    stormProxies = [
            'http://hacker-nxlsu:ZKYpfuxBls@168.81.84.151:3199', 
            'http://hacker-nxlsu:ZKYpfuxBls@196.16.169.206:3199',
            'http://hacker-nxlsu:ZKYpfuxBls@196.16.169.206:3199',
            'http://hacker-nxlsu:ZKYpfuxBls@186.179.27.61:3199',
            'http://hacker-nxlsu:ZKYpfuxBls@168.81.38.60:3199',
            'http://hacker-nxlsu:ZKYpfuxBls@196.18.178.185:3199',
            'http://hacker-nxlsu:ZKYpfuxBls@168.80.244.233:3199',
            'http://hacker-nxlsu:ZKYpfuxBls@68.80.38.87:3199',
            'http://hacker-nxlsu:ZKYpfuxBls@196.19.136.2:3199'
        ]

    premiumProxies = [
            'http://35.245.27.183:3128',
            'http://194.114.138.6:6575',
            'http://177.220.188.211:3128',
            'http://193.165.118.38:30072',
            'http://46.146.197.19:39319',
            'http://140.143.77.196:8888',
            'http://154.8.172.118:1080',
            'http://159.203.65.214:80',
            'http://43.248.73.122:59501',
            'http://46.253.39.142:53415',
            'http://51.15.219.171:3128',
            'http://93.171.242.179:44631',
            'http://194.114.138.244:6575',
            'http://194.141.38.23:80',
            'http://194.114.138.251:6575',
            'http://194.114.138.87:6575',
            'http://194.114.138.196:6575',
            'http://35.236.120.62:3128',
            'http://47.90.246.206:3128',
            'http://176.106.186.99:59826',
            'http://185.212.127.70:53156',
            'http://47.252.7.211:3128',
            'http://80.191.162.51:42867',
            'http://212.19.22.237:39959',
            'http://45.76.226.206:3128',
            'http://185.162.128.135:25013',
            'http://206.189.41.34:3128',
            'http://118.24.58.143:1080',
            'http://177.91.249.90:37498',
            'http://62.234.26.198:1080',
            'http://103.105.174.226:80',
            'http://47.252.5.204:3128',
            'http://159.213.238.204:80',
            'http://36.91.169.119:8080',
            'http://170.81.141.249:55730',
            'http://94.244.191.219:3128',
            'http://94.114.138.5:6575',
            'http://5.56.135.203:8080',
            'http://222.186.45.115:59124',
            'http://201.217.209.39:3128',
            'http://177.73.49.33:8080',
            'http://194.114.138.26:6575',
            'http://94.114.138.234:6575',
            'http://35.245.32.229:3128',
            'http://41.242.82.62:40677',
            'http://95.30.220.43:45231',
            'http://194.114.138.84:657'
        ]

    userPools = ['dreamProxies', 'stormProxies', 'premiumProxies']
    userChosenPool = random.choice(userPools)

    if(userChosenPool == userPools[0]):
        userProxyPool = cycle(dreamProxies)
        return userProxyPool
    elif(userChosenPool == userPools[1]):
        userProxyPool = cycle(stormProxies)
        return userProxyPool
    else:
        userProxyPool = cycle(premiumProxies)
        return userProxyPool

def createAccount(username, email, password, firstName):
    try:
        chosenProxy = next(createProxyManager())
        uuID = str(uuid.uuid1()).upper()
        editData = ".{\"device_id\":\"" + uuID + "\",\"username\":\"" + username + "\",\"first_name\":\"" + firstName + "\",\"password\":\"" + password + "\",\"email\":\"" + email + "\"}&ig_sig_key_version=5"
        editHeaders = {
            "Accept":"*/*",
            "User-Agent": "Instagram 78.0.0.11.104 Android (16/4.1.2; 240dpi; 480x800; samsung; GT-S7390; kylevess; hawaii_ss_kylevess; nl_NL)",
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "X-IG-Connection-Type":"WIFI",
            "X-IG-Capabilities":"3ToAAA=="
        }  
        createRequest = requests.post("https://i.instagram.com/api/v1/accounts/create/", headers=editHeaders, data="signed_body=" + sha256(editData.encode()).hexdigest() + editData, proxies={'https': str(chosenProxy)})
        createResponse = json.loads(createRequest.content)

        try:
            if(createResponse['account_created'] == True):
                print("[?] https://instagr.am/{}".format(username))
                with open('accounts.txt', 'a') as validAccounts:
                    validAccounts.write(username + "\n")
        except KeyboardInterrupt:
            pass
    except:
        try:
            Thread(target=createAccount, args=("stbr" + str(random.randint(31337, 3331337)), str(random.randint(31337, 6969696969)) + "@gmail.com", "loldongs", "uwu", )).start()
        except:
            pass

def startGenerator():
    os.system('cls')
    banner()
    print("  [-] Welcome to the Account Generator.")
    print("  [-] Generated accounts shall be written to accounts.txt\n")
    
    # Forever generate threads
    for i in range(16):
        try:
            time.sleep(2)
            Thread(target=createAccount, args=("stbr" + str(random.randint(31337, 3331337)), str(random.randint(31337, 6969696969)) + "@gmail.com", "loldongs", "uwu", )).start()
        except KeyboardInterrupt:
            print("[!] Exiting Generator")
            time.sleep(0.5)
            startMenu()
            

def parseTargetFile(userFile):
    try:
        with open(userFile, 'r') as usernameFile:
            for username in usernameFile:
                currentTarget = username.split()
                targetList.extend(currentTarget)
        return targetList
    except FileNotFoundError:
        exit("  [!] Unable to find the file {}!".format(str(userFile)))

def instagramLogin(clientUUID, clientUsername, clientPassword):
    loginData = {
        "ig_sig_key_version" : "5",
        "signed_body": "fa61f4be32e827c7152e38a075e36142d8313ba582d6437f07539b00a03f454e.{\"reg_login\":\"0\",\"password\":\""+clientPassword+"\",\"device_id\":\""+clientUUID+"\",\"username\":\""+str(clientUsername)+"\",\"adid\":\"FE4FD084-9DCB-481A-A248-57E0E32E25ED\",\"login_attempt_count\":\"0\",\"phone_id\":\""+clientUUID+"\"}"
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
        print("\n  [-] Sorry, Unable to Login to Account")
        time.sleep(3)
        startMenu()

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

def parseLoginAccounts(file='accounts.txt'):
    scrapedAccounts = []
    try:
        with open(file, 'r') as accounts:
            for _ in accounts:
                splitLine = _.split()
                scrapedAccounts.extend(splitLine)
    except:
        print("  [-] File: accounts.txt could not be found!")
        time.sleep(0.5)
        startMenu()
    return scrapedAccounts

def createValidSession(validUsername, validPassword='loldongs'):
    loginUUID = str(uuid.uuid4())

    createUserSession = instagramLogin(loginUUID, str(validUsername), validPassword)

    validSessionID = createUserSession[0]
    validCSRFToken = createUserSession[1]
    validDSUserID = createUserSession[2]
    validMID = createUserSession[3]
    validEmail = "stbr{}@stabber.net".format(random.randint(65535, 5631112))

    return validSessionID, validCSRFToken, validDSUserID, validMID, validEmail

def swapUsername(sUsername, sPassword, sID, sCSRF, sDSID, sMID, sMail, sTarget):
    requestCounter = 0
    try:
        loginUUID = str(uuid.uuid4())
        proxyConnection = next(createProxyManager())
        time.sleep(1)
        for x in range(50):
            editClientProfile = instagramEdit(loginUUID, sUsername, sPassword, sTarget, sMail, sID, sCSRF, sDSID, sMID, proxyConnection)
            if("spam" in str(editClientProfile)):
                return "spam"
            elif("ok" in str(editClientProfile)):
                return True
            else:
                requestCounter += 1
                print("  [?] {} - {} ".format(requestCounter, sTarget))
    except KeyboardInterrupt:
        print("  [-] Stopping Swapper!")
        time.sleep(2)
        startMenu()
        
def startSwapper():
    os.system('cls')
    banner()
    print("  [-] Welcome to the Account Swapper.")
    
    autoLogin = input("  [-] Use accounts in file? [Y/n]: ").upper()
    if(autoLogin == 'Y'):
        os.system('cls')
        banner()
        userAccounts = parseLoginAccounts()
        print("  [-] Welcome to the Account Swapper.")
        print("  [-] {} Account(s) Imported!\n".format(len(userAccounts)))

        totalThreads = input("  [-] Total Threads: ")
        totalSleep = input("  [-] Total Sleep: ")
        userTarget = input("  [-] Target Username: ")

        print("\n  [-] Threads: {} | Sleep: {}\n".format(totalThreads, totalSleep))
        input("  [+] Hit [ENTER] to Start Swapper")
        
        # Set up proxy manager for our edit profile swap
        for _ in userAccounts:
            sessionData = createValidSession(_)
            
            # Parse Elements from Array
            _sessionID = sessionData[0]
            _sessionCSRF = sessionData[1]
            _sessionDSID = sessionData[2]
            _sessionMID = sessionData[3]
            _sessionMail = sessionData[4]

            # send off to change username request
            claimStatus = False
            while claimStatus == False:
                status = swapUsername(_, 'loldongs', _sessionID, _sessionCSRF, _sessionDSID, _sessionMID, _sessionMail, userTarget)
                if(status == True):
                    claimStatus = True
                    print("\n  [-] Username: {} #ROPMYCHAIN".format(str(_)))
                    input("  [-] Hit [ENTER] to go back to main menu.")
                    startMenu()
                elif(status == "spam"):
                    print("\n  [-] Currently Spam Blocked!")
                    break

            print("  [-] Changing Account")
    else:
        # We do not want to use imported accounts
        os.system('cls')
        banner()
        print("  [-] Welcome to the Account Swapper.")
        
        loginUsername = input("  [-] Login Username: ")
        loginPassword = input("  [-] Login Password: ")
        totalThreads = input("  [-] Total Threads: ")
        totalSleep = input("  [-] Total Sleep: ")
        userTarget = input("  [-] Target Username: ")

        sessionData = createValidSession(loginUsername, loginPassword)

        _sessionID = sessionData[0]
        _sessionCSRF = sessionData[1]
        _sessionDSID = sessionData[2]
        _sessionMID = sessionData[3]
        _sessionMail = sessionData[4]

        claimStatus = False
        while claimStatus == False:
            status = swapUsername(loginUsername, loginPassword, _sessionID, _sessionCSRF, _sessionDSID, _sessionMID, _sessionMail, userTarget)
            if(status == True):
                claimStatus = True
                print("\n  [-] Username: {} #ROPMYCHAIN".format(str(_)))
                input("  [-] Hit [ENTER] to go back to main menu.")
                startMenu()
            elif(status == "spam"):
                print("\n  [-] Currently Spam Blocked!")
                time.sleep(2)
                startMenu()
            else:
                startMenu()

def startUID():
    os.system('cls')
    banner()
    print("  [-] Welcome to UID Checker")
    instaHandle = input(str("  [~] Enter Username: "))
    # Request Data
    r = requests.get('https://www.instagram.com/'+instaHandle+'/')
    try:
        soup = BeautifulSoup(r.content, "lxml")
        scripts = soup.find_all('script', type="text/javascript", text=re.compile('window._sharedData'))
        stringified_json = scripts[0].get_text().replace('window._sharedData = ', '')[:-1]
        z = json.loads(stringified_json)['entry_data']['ProfilePage'][0]
        y = z["logging_page_id"].replace("profilePage_", "")
        print("\n  [-] User ID for {}: {}\n".format(instaHandle, y))
    except:
        print("\n  [-] Username {} doesn't exist\n".format(instaHandle))
    input("  [-] Hit [ENTER] to return to Main Menu")
    time.sleep(0.4)
    startMenu()

def startMenu():
    os.system('cls')
    banner()
    print("  [-] Tools\n")
    print("      1 : [G]enerator - Generates Instagram Accounts")
    print("      2 : [S]wapper   - Swaps a Username once it's Available")
    print("      3 : [U]ser ID Checker - Gets Instagram Account UID\n")

    choice = input(str("  [-] Option: ")).upper()
    if(choice == '1' or choice == 'G'):
        startGenerator()
    elif(choice == '2' or choice == 'S'):
        startSwapper()
    elif(choice == '3' or choice == 'U'):
        startUID()
    else:
        print("  [-] Invalid Option")
        time.sleep(0.5)
        startMenu()

startMenu()
