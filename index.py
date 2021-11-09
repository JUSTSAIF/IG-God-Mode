# Coded By SAIF | INSTAGRAM: @qq_iq | Github: @JUSTSAIF
import requests
import time
from uuid import uuid4
UID = str(uuid4())
DEFAULT_NAME = "Mr28"
DEFAULT_BIO = "2B | !2B @qq_iq"
DEFAULT_URL = "https://discord.gg/tFdgRrq344"
USER_AGENT = 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)'
USER_AGENT_LIKE = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
HEADERS = {'User-Agent': USER_AGENT}
USERNAME = ''
POST_URL = ''
POST_ID = None
COMMENT_MSG = "0w0"

print('''
     _____  _____             _          __  __             _
    |_   _|/ ____|           | |        |  \/  |           | |
      | | | |  __   ___    __| | ______ | \  / |  ___    __| |  ___
      | | | | |_ | / _ \  / _` ||______|| |\/| | / _ \  / _` | / _ \\
     _| |_| |__| || (_) || (_| |        | |  | || (_) || (_| ||  __/
    |_____|\_____| \___/  \__,_|        |_|  |_| \___/  \__,_| \___|

                              IG : @qq_iq
========================================================================

 1 - Followers
 2 - POST Likes
 3 - POST Comments
 ''')

OPT = input('\n Enter Option : ')
USERS_FILE = 'u.txt' #input('\n Enter Users File Name : ')
USERS_PASS = '0w0_P__7BebeWala @IRAQ_BOOBS' #input('\n Enter Users PASSWORD : ')


def LOGIN(u, p):
    LOGIN_URL = 'https://b.i.instagram.com/api/v1/accounts/login/'
    data = {
        'uuid': UID,
        'username': u,
        'password': p,
        'device_id': UID,
        'from_reg': 'false',
        'csrftoken': 'missing',
        'login_attempt_countn': '0'
    }
    try:
        LOGIN_REQ = requests.post(LOGIN_URL, data=data, headers=HEADERS)
        return LOGIN_REQ.cookies.get_dict() if 'logged_in_user' in LOGIN_REQ.json() else False
    except:return False

def GET_HEADERS(login_cookies, ua=USER_AGENT):
    try:
        return {'cookie': "; ".join([str(x)+"="+str(y) for x, y in login_cookies.items()]),
                'User-Agent': ua,
                'x-requested-with': 'XMLHttpRequest',
                'x-csrftoken': login_cookies['csrftoken'],
                'x-instagram-ajax': '9f7a9dddd48c',
                'x-ig-app-id': '936619743392459',
                }
    except:return {}


def GET_USER_ID(username):
    USER_ID_URL = 'https://www.instagram.com/' + username + '/?__a=1'
    USER_ID_REQ = requests.get(USER_ID_URL, headers=HEADERS)
    try:
        return USER_ID_REQ.json()['graphql']['user']['id']
    except:
        print('[-] User Not Found')
        exit()


def FollowUser(u):
    try:
        UserID = GET_USER_ID(USERNAME)
        FOLLOW_REQ = requests.post(F'https://www.instagram.com/web/friendships/{UserID}/follow/', headers=GET_HEADERS(u))
        if(FOLLOW_REQ.status_code != 204 and FOLLOW_REQ.headers["content-type"].strip().startswith("application/json")):
            if(FOLLOW_REQ.json()["status"] == 'ok'):
                print('[+] Followed')
            else:
                print('[-] Not Followed')
                # print('[*] Trying Again ...')
                # FollowUser(USERNAME)
        else:
            print('[-] Not Followed')
            # print('[*] Trying Again ...')
            # FollowUser(USERNAME)
    except:print('[-] Err ... passing')

def POST_LIKE(u):
    LIKE_REQ = requests.post(F'https://www.instagram.com/web/likes/{POST_ID}/like/', headers=GET_HEADERS(u, USER_AGENT_LIKE))
    if(LIKE_REQ.status_code != 204 and LIKE_REQ.headers["content-type"].strip().startswith("application/json")):
        if(LIKE_REQ.json()["status"] == 'ok'):
            print('[+] LIKED')
        else:
            print('[-] Not Liked')
            # print('[*] Trying Again ...')
            # POST_LIKE(POST_URL)
    else:
        print('[-] Not Liked !')
        # print('[*] Trying Again ...')
        # POST_LIKE(POST_URL)
    time.sleep(1)

def COMMENTS(u):
    COMMENT_URL = F"https://www.instagram.com/web/comments/{POST_ID}/add/"
    try:
        response = requests.post(COMMENT_URL, headers=GET_HEADERS(u, USER_AGENT_LIKE), data=f"comment_text={COMMENT_MSG}&replied_to_comment_id=".encode('utf-8'))
        if response.status_code == 200:
            print('[+] Done')
        else:
            print('[-] Error')
    except:print('[#] ERR .')


# Get Username or Post URL
if(OPT == '1'):
    USERNAME = input('\n Enter Username : ')
elif(OPT == '2' or OPT == '3'):
    POST_URL = input('\n Enter POST URL : ')
    if OPT == '3':COMMENT_MSG = input('\n Enter Comment Message (DEFAULT : 0w0) : ')
    try:
        POST_ID = requests.get(f'{POST_URL}?__a=1', headers=HEADERS).json()['graphql']['shortcode_media']['id']
    except:
        print('[-] Post Not Found')
        exit()
else:
    print('[-] Invalid Option')
    print('[*] Exiting ...')
    exit()

# Loop On Users
for USR in open(USERS_FILE, 'r'):
    _LOGIN = LOGIN(USR, USERS_PASS)
    if _LOGIN != False:
        print('[+] '+USR.replace('\n','')+' : Logged In Successfully ')
        if(OPT == '1'):FollowUser(_LOGIN)
        elif(OPT == '2'):POST_LIKE(_LOGIN)
        elif(OPT == '3'):COMMENTS(_LOGIN)
    else:print('[-] User Login Failed ... passing')

