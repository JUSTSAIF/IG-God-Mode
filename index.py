# Coded By SAIF | INSTAGRAM: @qq_iq | Github: @JUSTSAIF
import random,requests,json,time
from bs4 import BeautifulSoup as bs4
from datetime import datetime
import os

HEADERS = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}
POST_URL = ''
POST_ID = None
USER_ID = ""
COUNT = 0

def GET_USER_ID(username):
    USER_ID_URL = 'https://www.instagram.com/' + username + '/?__a=1'
    USER_ID_REQ = requests.get(USER_ID_URL, headers=HEADERS)
    try:
        return USER_ID_REQ.json()['graphql']['user']['id']
    except:
        print('[-] User Not Found')
        exit()

def GET_HEADERS(SESSION_ID,CSRFTOKEN=""):
    try:
        CS = requests.get("https://instagram.com/").cookies['csrftoken'] if CSRFTOKEN == "" else CSRFTOKEN
        return {
                'cookie': f'sessionid={SESSION_ID};csrftoken={CS};',
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
                'x-requested-with': 'XMLHttpRequest',
                'x-csrftoken': CS,
                'x-instagram-ajax': '1284f5c4fcfb',
                'x-ig-app-id': '936619743392459',
                }
    except:return {}

def follow_me(SESSION_ID,CSRFTOKEN):
    try:
        global COUNT
        print('[+] User ID: ' + USER_ID)
        FOLLOW_REQ = requests.post(F'https://www.instagram.com/web/friendships/{USER_ID}/follow/', headers=GET_HEADERS(SESSION_ID,CSRFTOKEN))
        if(FOLLOW_REQ.status_code != 204 and FOLLOW_REQ.headers["content-type"].strip().startswith("application/json")):
            if(FOLLOW_REQ.json()["status"] == 'ok'):
                COUNT += 1
                print(f'[+][{COUNT}] Followed')
            else:
                print('[-] Not Followed')
        else:
            print('[-] Not Followed')
    except:print('[-] Err ... passing')

def POST_LIKE(SESSION_ID,CSRFTOKEN):
    LIKE_REQ = requests.post(F'https://www.instagram.com/web/likes/{POST_ID}/like/', headers=GET_HEADERS(SESSION_ID,CSRFTOKEN))
    if(LIKE_REQ.status_code != 204 and LIKE_REQ.headers["content-type"].strip().startswith("application/json")):
        if(LIKE_REQ.json()["status"] == 'ok'):
            print('[+] LIKED')
        else:
            print('[-] Not Liked')
    else:
        print('[-] Not Liked !')

def GetRandomComment():
    file = open("Comments.txt", "r", encoding="utf-8")
    line = next(file)
    for num, aline in enumerate(file, 2):
        if random.randrange(num):
            continue
        line = aline
    return line.strip()

def COMMENTS(SESSION_ID,CSRFTOKEN):
    COMMENT_URL = F"https://www.instagram.com/web/comments/{POST_ID}/add/"
    try:
        response = requests.post(COMMENT_URL, headers=GET_HEADERS(SESSION_ID,CSRFTOKEN), data={'comment_text':GetRandomComment()})
        if response.status_code == 200:
            print('[+] Done')
        else:
            print('[-] Error')
    except:print('[#] ERR .')

def delete_duplicate_lines():
    number_seen = []
    try:
        FileName = input(" [!] Enter file name: ")
        if os.path.exists(FileName):
            outfile = open(F"NEW_{FileName}", "w")
            for Number in open(FileName, "r").read().splitlines():
                Number = Number.strip()
                if Number not in number_seen:
                    outfile.write(Number+"\n")
                    number_seen.append(Number)
            outfile.close()
        else:
            print("\n [!] File not found!")
    except KeyboardInterrupt:
        print("\n [!] Bye!")
    except:
        print(" [-] Error!")
    input("\n\n Done! Press Enter to exit.")
    exit()
def clean_invalid_usernames():
    L = input(" [*] Enter list: ")
    try:
        if os.path.exists(L):
            F = open("ValidUsernames.txt", "a")
            for user in open(L).readlines():
                user = user.strip()
                if user[0] != "." and user[-1] != ".":
                    F.write(user + "\n")
            F.close()
        else:
            print("\n [!] File not found!")
    except KeyboardInterrupt:
        print("\n [!] Bye!")
    except:
        print(" [-] Error!")
    input("\n\n Done! Press Enter to exit.")
    exit()
def get_contact_numbers(SESSION):
    try:
        print(F" [+] Session : {SESSION}")
        API = "https://www.instagram.com/graphql/query/?query_hash=68b15837c4c60cf5bb0c3df17a4791f8"
        REQ = requests.get(API,headers=GET_HEADERS(SESSION)).json()
        print("[+] Get PN Success")
        F = open("ContactNumbers.txt","a")
        for PN in REQ["data"]["user"]["contact_history"]:
                if len(PN["raw_value"]) > 9:
                    GG = PN["raw_value"]
                    F.write(F"0{GG}\n")
        F.close()
    except:pass
def create_combo():
    file = input("Enter file name (users): ")
    file2 = input("Enter file name (passwords): ")
    if os.path.exists(file) and os.path.exists(file2):
        users = open(file, 'r').read().splitlines()
        passs = open(file2, 'r').read().splitlines()
        for i in users:
            for e in passs:
                with open('combo wx.txt', 'a') as combo:
                    combo.write(f"{i}:{e}\n")
        print("[*] successful create")
    else:
        print("[!] file not found")
        input("\n\n Done! Press Enter to exit.")
        exit()
print('''
     _____  _____             _          __  __             _
    |_   _|/ ____|           | |        |  \/  |           | |
      | | | |  __   ___    __| | ______ | \  / |  ___    __| |  ___
      | | | | |_ | / _ \  / _` ||______|| |\/| | / _ \  / _` | / _ \\
     _| |_| |__| || (_) || (_| |        | |  | || (_) || (_| ||  __/
    |_____|\_____| \___/  \__,_|        |_|  |_| \___/  \__,_| \___|

                              IG : @qq_iq
========================================================================

 1 - Followers (Sessions Required)
 2 - POST Likes (Sessions Required)
 3 - POST Comments (Sessions Required)
 4 - Delete Duplicate lines in file
 5 - Delete invalid usernames 
 6 - Get Contact Numbers from Account (Sessions Required)
 7 - Create Combo *username:password
 ''')
# Get Username or Post URL
OPT = input('\n Enter Option : ')
if(OPT == '1'):
    USER_ID = input('\n Enter USER ID : ')
elif(OPT == '2' or OPT == '3'):
    POST_URL = input('\n Enter POST URL : ')
    try:
        POST_ID = requests.get(f'{POST_URL}?__a=1', headers=HEADERS).json()['graphql']['shortcode_media']['id']
        print(POST_ID)
    except:
        print(' [-] Post Not Found')
        exit()
elif(OPT == '3'):pass
elif(OPT == '4'):delete_duplicate_lines()
elif(OPT == '5'):clean_invalid_usernames()
elif(OPT == '6'):pass
elif(OPT == '7'):create_combo()

# Loop On Users
if(OPT == '1' or OPT == '2' or OPT == '3' or OPT == '6'):
    for line in open('s.txt').readlines():
        ACC = line.strip()
        SESSION_ID = ACC.split(':')[0]
        CSRFTOKEN = requests.get("https://www.instagram.com/").cookies['csrftoken']
        print(" [+] SESSIONID: "+SESSION_ID)
        if(OPT == '1'):follow_me(SESSION_ID,CSRFTOKEN)
        elif(OPT == '2'):POST_LIKE(SESSION_ID,CSRFTOKEN)
        elif(OPT == '3'):COMMENTS(SESSION_ID,CSRFTOKEN)
        elif(OPT == '6'):get_contact_numbers(SESSION_ID)
        else:print(' [-] User Login Failed ... passing')