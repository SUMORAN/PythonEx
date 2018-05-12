#!/usr/bin/evn python3
# -*- coding:utf-8 -*-
import codecs
import os
import re
'''
f1 = open("D:\\python\\test1.txt", "r").readlines()
f2 = open("D:\\python\\test2.txt", "r").readlines()
f3 = open("D:\\python\\test_out.txt", "a")
for line in f1:
    print("line", line)
    for line_tar in f2:
        if line.split()[0] == line_tar.split()[0]:
            seq = [line_tar.strip("\n"), "\t", line.split()[-1], "\n"]
            print("seq=", seq)
            f3.writelines(seq)
            f3.flush()
        continue
f3.close()
'''

'''
f1 = open("D:\\python\\evaluation.ner.ssplit.token4.BIO", "r").readlines()
f3 = open("D:\\python\\222-evaluation.ner.ssplit.token4.BIO", "a")
for line in f1:
    line_0 = line.strip()
    seq = [line_0,"\n"]
    f3.writelines(seq)
    f3.flush()
f3.close()
'''
def zero_digits(s):
#{{{
    """
    Replace every digit in a string by a zero.
    """
    return re.sub('\d', '0', s)
#}}}

#f5 = open("D:\\python\\222-evaluation.ner.ssplit.token4.BIO", "a")
#f6 = open("D:\\python\\222-evaluation.ner.ssplit.token4.BIO", "a")

sentence =[]
sentences =[]
count = 0
for line in codecs.open("D:\\Att-ChemdNER-master\\data\\biochem_corpus\\biochem_training.ner.sen.token4.BIO_allfea",'r', 'utf8'):
    line = zero_digits(line.rstrip())
    if not line:
        if len(sentence) > 0:
            if 'DOCSTART' not in sentence[0][0]:
                sentences.append(sentence)
            sentence = []
    else:
        #print("len(line)", len(line))
        word = line.split()
        count +=1
        if len(word) >= 2:
            print("line:",count,"len(word)", len(word),"word",word)
        assert len(word) >= 2
        sentence.append(word)