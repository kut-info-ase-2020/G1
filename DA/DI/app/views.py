import json
import os
import re

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from DI.settings import MEDIAS_ROOT


def find_NewFile(path):
    # 获取文件夹中的所有文件
    lists = os.listdir(path)
    if not lists or len(lists) <= 0:
        return ""
    # 对获取的文件根据修改时间进行排序
    lists.sort(key=lambda x: os.path.getmtime(path + '/' + x))
    if ".DS_Store" == lists[-1]:
        lists.remove(lists[-1])
        if not lists or len(lists) <= 0:
            return ""
        return lists[-1]
    return lists[-1]


def findNewFile():
    image1 = find_NewFile(MEDIAS_ROOT + '1/').replace('./', '/')
    image2 = find_NewFile(MEDIAS_ROOT + '2/').replace('./', '/')
    image3 = find_NewFile(MEDIAS_ROOT + '3/').replace('./', '/')

    try:
        searchObj = re.search(r'(.*)-NUM:(.*)-Nom:(.*)-..*', image1, re.M | re.I)
        image1Time = searchObj.group(1)
        image1Num = searchObj.group(2)
        image1Nom = searchObj.group(3)
    except:
        image1Time = ""
        image1Num = ""
        image1Nom = ""
    image1Time = image1Time.replace("_", ':').replace("-", "+", 2).replace("-", " ").replace("+", "-", 2)
    data = {"image1": {"f": image1, "t": image1Time, "num": image1Num, "nom": image1Nom},
            "image2": {"f": image2},
            "image3": {"f": image3, }}
    return data


def allPage(request):
    info_dict = findNewFile()
    return render(request, 'all.html', {'data': info_dict})


def refresh(request):
    import requests
    # url = "http://"
    # res = requests.get(url)
    # print(res.text)
    data = findNewFile()
    return HttpResponse(json.dumps(data))
