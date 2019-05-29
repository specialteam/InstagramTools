# Activates Generated Instagram Accounts
# to bypass swap blocc


from __future__ import print_function
import random
import time
import hmac
import json
import hashlib
import uuid as uuid_library
import requests
import six.moves.urllib as urllib
from pprint import pprint

proxies = {}

IG_SIG_KEY = '7f2efba692e18dd385499a6727ad440a959d575568d5547594cc54c3ff5bbe35'

IG_LIST = [
    {
        'instagram_version': '91.0.0.18.118',
        'ig_version_key': '152367530'
    }
]

ANDROID_LIST = [
    {
        'android_version': 28,
        'android_release': 9,
        'dpi': '420dpi',
        'resolution': '1080x1794',
        'manufacturer': 'unknown/Android',
        'device': 'Google Pixel 2',
        'model': 'vbox86p',
        'cpu': 'vbox86'
    }
]

def get_device():
    device = {}
    _max_for_ig = len(IG_LIST) - 1
    _max_for_android = len(ANDROID_LIST) - 1
    device.update(IG_LIST[random.randint(0, _max_for_ig)])
    device.update(ANDROID_LIST[random.randint(0, _max_for_android)])
    return device


DEVICE = get_device()

USER_AGENT_BASE = (
    'Instagram {instagram_version} '
    'Android ({android_version}/{android_release}; '
    '{dpi}; {resolution}; {manufacturer}; '
    '{device}; {model}; {cpu}; en_US; {ig_version_key})'
)
user_agent = USER_AGENT_BASE.format(**DEVICE)  # just insert params
headers = {
    'User-Agent': user_agent,
    'Accept-Language': 'en-US',
    'Accept-Encoding': 'gzip, deflate',
    'X-IG-Connection-Speed': '-1kbps',
    'X-IG-Bandwidth-Speed-KBPS': '-1.000',
    'X-IG-Bandwidth-TotalBytes-B': '0',
    'X-IG-Bandwidth-TotalTime-MS': '0',
    'X-IG-VP9-Capable': 'false',
    'X-IG-Connection-Type': 'WIFI',
    'X-IG-Capabilities': '3brTvw=='
}

def HMAC(text):
    hash = hmac.new(IG_SIG_KEY.encode(), text.encode('utf-8'), hashlib.sha256)
    return hash.hexdigest()

class IGAgeBypass():
    phone_id = str(uuid_library.uuid4())
    uuid = str(uuid_library.uuid4())
    waterfall_id = str(uuid_library.uuid4())
    device_id = "android-" + str(HMAC(str(random.randint(1000, 9999))))[0:min(64, 16)]

    def __init__(self, *args, **kwargs):
        super()
        self.base_generic = 'https://i.instagram.com/api/v1/'
        self.base_b = 'https://b.i.instagram.com/api/v1/'
        self.session = requests.Session()
        self.session.headers.update(headers)
        if kwargs['proxies']:
            self.session.proxies.update(kwargs['proxies'])
        self._init_challenge_signup()

    def _init_challenge_signup(self):
        point = 'si/fetch_headers/?challenge_type=signup&guid={}'.format(uuid_library.uuid4())
        res = self.session.get(self.base_generic + point)

    def check_token(self):
        point = '/api/v1/zr/token/result/?device_id={}&token_hash=&custom_device_id={}&fetch_reason=token_expired'.format(self.device_id, self.phone_id)
        res = self.session.get(self.base_b + point)
        return res

    def _make_body(self, body):
        jsonInformation = json.dumps(body)
        signedPayload = {
            'signed_body': HMAC(jsonInformation) + "." + jsonInformation,
            'ig_sig_key_version': '4',
        }
        return signedPayload
    
    def login(self, usr, psw):
        self.username = usr
        point = 'accounts/login/'
        body = {
            "country_codes": "[{\"country_code\":\"1\",\"source\":[\"default\"]}]",
            "phone_id": self.phone_id, 
            "_csrftoken": self.session.cookies.get_dict()['csrftoken'],
            "username": self.username,
            "adid": "",
            "guid": self.uuid, 
            "device_id": self.device_id,
            "google_tokens": "[]",
            "password": psw,
            "login_attempt_count": "1"
        }
        data = self._make_body(body)
        res = self.session.post(self.base_generic + point, data)
        return res


    def verify(self):
        flow = [
            self._intro_screen,
            self._qp_intro,
            self._finish,
        ]
        last_res = None

        for step in flow:
            last_res = step()
            if self.screen_key == 'already_finished':
                break

        data = last_res.json()
        if data['status'] == 'ok':
            return last_res
        else:
            return last_res

    def _intro_screen(self):
        try:
            point = 'consent/existing_user_flow/'
            try:
                body = {
                    "_csrftoken": self.session.cookies.get_dict()['csrftoken'],
                    "_uuid": self.uuid,
                }
            except KeyError:
                body = {
                    "_csrftoken": self.session.cookies.get_dict()['csrftoken'],
                    "_uuid": self.uuid
                }
            data = self._make_body(body)
            res = self.session.post(self.base_b + point, data)

            try:
                if 'screen_key' not in str(res.json()):
                    print("Account is disabled")
                else:
                    self.screen_key = res.json()['screen_key']
            except:
                print("Account is disabled...")
                
            return res
        except:
            return res

    def _qp_intro(self):
        point = 'consent/existing_user_flow/'
        body = {
            "current_screen_key": "qp_intro",
            "_csrftoken": self.session.cookies.get_dict()['csrftoken'],
            "updates": "{\"existing_user_intro_state\":\"2\"}",
            "_uid": self.session.cookies.get_dict()['ds_user_id'],
            "_uuid": self.uuid,
        }
        data = self._make_body(body)
        res = self.session.post(self.base_b + point, data)
        return res

    def _finish(self):
        point = 'consent/existing_user_flow/'
        if self.screen_key == 'tos_and_two_age_button':
            body = {
                "current_screen_key": "age_consent_two_button",
                "phone_id": self.phone_id,
                "gdpr_s": "[0,0,0,null]",
                "_csrftoken": self.session.cookies.get_dict()['csrftoken'],
                "updates": "{\"age_consent_state\":\"2\"}",
                "guid": self.uuid, 
                "device_id": self.device_id,
            }
        elif self.screen_key == 'tos':
            body = {
                "current_screen_key": "tos",
                "_csrftoken": self.session.cookies.get_dict()['csrftoken'],
                "updates": "{\"tos_data_policy_consent_state\":\"2\"}",
                "_uid": self.session.cookies.get_dict()['ds_user_id'],
                "_uuid": self.uuid,
            }
        elif self.screen_key == 'dob':
            body = {
                "current_screen_key": "dob",
                "_csrftoken": self.session.cookies.get_dict()['csrftoken'],
                "day": random.randint(1, 28),
                "_uid": self.session.cookies.get_dict()['ds_user_id'],
                "year": random.randint(1970, 2009),
                "_uuid": self.uuid,
                "month": random.randint(1, 12),
            }
        elif self.screen_key == 'already_finished':
            return {'screen_key': 'finished'}
        
        try:
            data = self._make_body(body)
        except:
            pass
        res = self.session.post(self.base_b + point, data)
        return res

def verify(username, password='loldongs'):
    ig = IGAgeBypass(proxies=proxies)
    print("[~] Activating:", username)

    ig.login(username, password)

    verifyRes = ig.verify()

    if verifyRes and verifyRes.json()['screen_key'] == 'finished':
        print("[*] Activated:", username)
    else:
        print("[!] Already Activated!")

def main():
    print("../ Instagram Account Activator /..")
    try:
        with open('accounts.txt', 'r') as f:
            for line in f:
                l = line.strip()
                verify(l)
    except:
        pass

main()

