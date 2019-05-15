import requests

def load_words(wordFile):
    with open(wordFile, 'r') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

def numberCheck(string):
    return any(char.isdigit() for char in string)

def check_status(username):
    if("-" not in username and '\'' not in username and '.'  not in username and len(username) <= 6):
        if(numberCheck(username) == True):
            pass
        else:
            statusRequest = requests.get("https://steamcommunity.com/id/{}".format(str(username))).text
            if('The specified profile could not be found' in statusRequest):
                return True
            else:
                return False
    else:
        pass

def main():
    print("Steam Username Checker :=-")
    
    userFile = input(str("[-] File: \n"))
    usernamesToCheck = load_words(userFile)

    for username in usernamesToCheck:
        if(check_status(username) == True):
            print("[+] {} is available".format(username))
            with open('results.txt', 'a') as outputFile:
                outputFile.write(username + "\n")
        else:
            pass
    
main()
