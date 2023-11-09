# It can forward answers to your discord too !!

rookie_id = '<YOUR_ROOKIE>'  
rookie_pwd = "<IL Meta Password>"
test_id = "<TEST-ID>" 
channel = '<YOUR-WEBHOOK>'  # Optional
send_dscd = False # Set true if rediredting to discord

import json
import requests

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

url = f"https://prodslms.ilteacher.com/v2/test/getStudentTestDetails?studentTestId={test_id}&platform=WEB&platformVersion=Chrome%20110"
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
