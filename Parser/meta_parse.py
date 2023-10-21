# curl -i -s -k -X $'GET' -H $'Host: prodslms.ilteacher.com' -H $'Sec-Ch-Ua: \"Not A(Brand\";v=\"24\", \"Chromium\";v=\"110\"' -H $'Accept: application/json, text/plain, */*' -H $'Content-Type: application/json' -H $'Sec-Ch-Ua-Mobile: ?0' -H $'Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiIyMjQzMDE2ODgiLCJUZW5hbnRJZCI6MiwiUm9sZU5hbWUiOiJTdHVkZW50IiwiREJJZCI6IjM0NDQ2OTQiLCJGaXJzdE5hbWUiOiJQUkFNT0QgVklLTkVTSCIsIlRlbmFudENvZGUiOiJzcmljaGFpdGFueWEiLCJMYXN0TmFtZSI6IkUgUiIsImV4cCI6MTY5NzkzNTQ1MCwiUm9sZUlkIjoiMSIsImlhdCI6MTY5Nzg0OTA1MH0.4A8JUxR60_GakSai0oIe2mJOCLfJ6yKhbDIw6ugyKq8' -H $'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.78 Safari/537.36' -H $'Sec-Ch-Ua-Platform: \"Linux\"' -H $'Origin: https://srichaitanyameta.com' -H $'Sec-Fetch-Site: cross-site' -H $'Sec-Fetch-Mode: cors' -H $'Sec-Fetch-Dest: empty' -H $'Referer: https://srichaitanyameta.com/' -H $'Accept-Encoding: gzip, deflate' -H $'Accept-Language: en-US,en;q=0.9' $'https://prodslms.ilteacher.com/v2/test/getStudentTestDetails?studentTestId=150365103&platform=WEB&platformVersion=Chrome%20110'
# https://colab.research.google.com/drive/1FHsIwUN-ylvav9KmunG2RsArNJeqKJEn#scrollTo=cYUVqQVM_flr

import json

def parseit(js):
  ans = js['scheduleTest'][0]['subjectStructures']
  count=1
  for sub in ans:
    print('\n', sub['subjectName'])
    for sec in sub['sections']:
      print('\t', sec['sectionName'], ' - ', sec['questionListDetails'][0]['question_type'])
      for ques in sec['questionListDetails']:
        print('\t\t',count,'\b) ',ques['question_data']['question']['correct_answer'])
        count=count+1
  print('\n')

with open('find.json', encoding='UTF8') as f:
  c=f.readlines()
# print(c[21:])
  print("Find_1 Retrived Successfully")

with open('find2.json', 'w', encoding='UTF8') as f2:
  for x in c[21:]:
    f2.write(x)
  print("Find_2 Complied Successfully")

with open('find2.json', 'r', encoding='UTF8') as f3:
  data = json.load(f3)
print(type(data))

parseit(data)