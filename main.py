# -*- coding: UTF-8 -*-
import sys
import os
import requests
import json

def getLyrics(dir):
    dir = dir;#"f:\\music"
    nameList = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            # print os.path.join(root, file)
            # 所有歌名的list歌名命名规则：歌手+歌名 张学友-你最珍贵
            nameList.append(str(file).split('.')[0])
    # for index in range(len(nameList)):
    #     print index,nameList[index]
    for index in range(len(nameList)):
        try: url = 'http://gecimi.com/api/lyric/'+nameList[index].split('-')[1]+'/'+nameList[index].split('-')[0]
        except IndexError:
            print(nameList[index])    
        res = requests.get(url.decode("gbk", "ignore"))
        json_response = res.json()
        if(json_response['count'] > 0):
            # print json.dumps(json_response)
            lycUrl = json_response['result'][0]['lrc']
            lycResponse = requests.get(lycUrl)
            try:
                with open('lyrics/'+nameList[index]+'.lrc', 'w') as code:
                    code.write(lycResponse.content)
                print('ok')
            except IOError:
                print(nameList[index])

if __name__ == "__main__":
    getLyrics(sys.argv[1])