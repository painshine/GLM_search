import os
import platform
import numpy as np
import heapq

from SemanticSearch import simlist
from GLM import GLMresp
from Doclib.load_Filelist import filelist


os_name = platform.system()
clear_command = 'cls' if os_name == 'Windows' else 'clear'

# HelperList
fl,fnl = filelist()

def find_content(cos_list,fl):
    #topk
    # 获取下标， 输出top 2下标
    fnumb = heapq.nlargest(3, range(len(cos_list)), cos_list.__getitem__)

    # 获取数值， 输出top 2 得分
    fscore = heapq.nlargest(3,cos_list)

    # coner case 1: 最高分不匹配问题,阈值0.5
    if max(fscore) < 0.5:
        content = ''

    elif (max(fscore) > 0.6) and (min(fscore) > 0.6):
    # coner case 2: 两条文档均匹配问题，阈值0.6
        fnumb1 = fnumb[0]
        fnumb2 = fnumb[1]

        # topk只取1时，且不考虑similarity是否合理，读入文档
        fn1 = fl[fnumb1]
        fn2 = fl[fnumb2]
        file_path1 = f'./Doclib/DocFiles/{fn1}'
        file_path2 = f'./Doclib/DocFiles/{fn2}'
        with open(file_path1, 'r',encoding='utf-8') as f:
            content1 = f.read()
        with open(file_path2, 'r',encoding='utf-8') as f:
            content2 = f.read()
        content = content1 + '\n' + content2

    # 正常情况，只取top1
    else:
        fn = fl[fnumb[0]]
        file_path = f'./Doclib/DocFiles/{fn}'
        with open(file_path, 'r',encoding='utf-8') as f:
            content = f.read()
            
    # 取出相关搜索结果
    search_result = '\033[93m\n相关搜索：\033[0m'
    for idx, numb in enumerate(fnumb):
        if idx < len(fnumb)-1:
            _fn = fl[numb].split('_')[1]
            _fn = _fn.split('.txt')[0]
            search_result = search_result + '\033[4;91m' + _fn + '\033[0m 、 '
        else:
            _fn = fl[numb].split('_')[1]
            _fn = _fn.split('.txt')[0]
            search_result = search_result + '\033[4;91m' + _fn + '\033[0m'
 
    return content,search_result


def main():
    while True:
        query = input("\033[93m\n用户输入：\033[0m")
        if query == "stop":
            print("\033[93m\n小助手：\033[0m \033[92m感谢您的使用，下次再见！\033[0m")
            break
        
        # cal similarity
        cos_list = simlist(query)

        # find content
        content,search_result = find_content(cos_list,fl)

        # response
        try:
            response = GLMresp(content, query)
        except:
            print('\033[93m\n小助手：\033[0m \033[92m糟糕，刚才发生了键盘抖动，请再次输入。\033[0m')
            main()

        print("\033[93m\n小助手：\033[0m \033[92m" + str(response) + '\033[0m')
        print(search_result)
        print("===========================================================================================")


if __name__ == "__main__":
    print("\033[94m************************************************************************************\033[0m")
    print("\033[94m*欢迎使用 云空间 帮助中心 小助手，请输入您的问题，clear 清空对话历史，stop 终止程序*\033[0m")
    print("\033[94m************************************************************************************\033[0m")
    main()
