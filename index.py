from io import DEFAULT_BUFFER_SIZE
import requests
from uuid import uuid4
UID = str(uuid4())
DEFAULT_NAME = "Mr28"
DEFAULT_BIO = "2B | !2B @qq_iq"
DEFAULT_URL = "https://discord.gg/tFdgRrq344"
USER_AGENT = 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)'
USER_AGENT_LIKE = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
HEADERS = {'User-Agent': USER_AGENT}

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
 2 - Like POST
''')

OPT = input('\n Enter Option : ')


def LOGIN():
    LOGIN_URL = 'https://b.i.instagram.com/api/v1/accounts/login/'
    data = {
        'uuid': UID,
        'username': 'bwtrykh.krr',
        'password': '07704856654',
        'device_id': UID,
        'from_reg': 'false',
        'csrftoken': 'missing',
        'login_attempt_countn': '0'
    }
    LOGIN_REQ = requests.post(LOGIN_URL, data=data, headers=HEADERS)
    return LOGIN_REQ.cookies.get_dict()


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


def FollowUser(user):
    _LOGIN = LOGIN()
    UserID = GET_USER_ID(user)
    if(requests.post(F'https://www.instagram.com/web/friendships/{UserID}/follow/', headers=GET_HEADERS(_LOGIN)).status_code == 200):
        print('[+] Followed')
    else:
        print('[-] Not Followed')
        print('[*] Trying Again ...')
        FollowUser(user)


def POST_LIKE(post_url):
    _LOGIN = LOGIN()
    POST_ID = 0
    try:
        POST_ID = requests.get(
            F"https://api.instagram.com/oembed/?url={post_url}", headers=HEADERS).json()['media_id'].split("_")[0]
    except:
        print('[-] Post Not Found')
        exit()
    LIKE_REQ = requests.post(F'https://www.instagram.com/web/likes/{POST_ID}/like/', headers=GET_HEADERS(_LOGIN, USER_AGENT_LIKE))
    if(LIKE_REQ.status_code != 204 and LIKE_REQ.headers["content-type"].strip().startswith("application/json")):
        if(LIKE_REQ.json()["status"] == 'ok'):
            print('[+] LIKED')
        else:
            print('[-] Not Liked')
            print('[*] Trying Again ...')
            POST_LIKE(post_url)
    else:
        print('[-] Not Liked') 
        print('[*] Trying Again ...')
        POST_LIKE(post_url)


# Run Options :
if(OPT == '1'):
    USERNAME = input('\n Enter Username : ')
    FollowUser(USERNAME)
elif(OPT == '2'):
    POST_URL = input('\n Enter POST URL : ')
    POST_LIKE(POST_URL)
else:
    print('[-] Invalid Option')
    print('[*] Exiting ...')
    exit()

