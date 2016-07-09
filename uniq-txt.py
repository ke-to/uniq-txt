# -*- coding: utf-8 -*-

import sys,re,os
from collections import Counter
from shutil import copyfile


if __name__ == "__main__":
    param = sys.argv
    print param
    fileName = param[1]
    f = open(fileName, 'r')
    li = []
    for line in f:
        li.append(line)
    overlap = [key for key,val in Counter(li).items() if val > 1]
    print "**Overlap line list**\n------------------------"
    for i in overlap:
        print i
    print "------------------------"
    flg = raw_input("Are you sure you want to create a unique list to remove the above-mentioned? (y/n) > ")
    if flg == "y":
        # ファイル名変更
        f.close
        rename = "%s.back" % fileName
        copyfile(fileName, rename)
        f2 = open(fileName, 'w')
        f2.write("")
        list_uniq = []
        # 順序を保持したまま重複を削除
        list_uniq = sorted(set(li), key=li.index)
        for i in list_uniq:
            f2.writelines(i)
        print "**** All completed ****"
        f2.close
    else:
        print "**** Program is ended ****"
        sys.exit()
        f.close
