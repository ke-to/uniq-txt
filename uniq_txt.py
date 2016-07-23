# -*- coding: utf-8 -*-

import sys,re,os
from collections import Counter
from shutil import copyfile
import csv


if __name__ == "__main__":
    param = sys.argv
    print param
    fileName = param[1]
    fileType = "csv" if fileName.find(".csv") else "txt"
    print "filetype is %s" % fileType
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
        print "completed copy."
        list_uniq = []
        # 順序を保持したまま重複を削除
        # list_uniq = sorted(set(li), key=li.index)
        def f7(seq):
            seen = set()
            seen_add = seen.add
            return [ x for x in seq if x not in seen and not seen_add(x)]
        list_uniq = f7(li)
        print "overlap is deleted."
        f2 = open("%s.txt" % fileName, 'a')
        f2.write("")
        for i in list_uniq:
            f2.writelines(i)
        # if fileType == "txt":
        #     f2 = open(fileName, 'a')
        #     f2.write("")
        #     for i in list_uniq:
        #         f2.writelines(i)
        # if fileType == "csv":
        #     os.remove(fileName)
        #     f2 = open(fileName, 'a')
        #     csvWriter = csv.writer(f2)
        #     for i in list_uniq:
        #         csvWriter.writerow(i.encode('sjis'))
        print "**** All completed ****"
        f2.close
    else:
        print "**** Program is ended ****"
        sys.exit()
        f.close
