"""
This file contains helpful miscellaneous functions.

 @author: ysvang@uci.edu
"""
#这个函数是将小写的true和false转换为True和False

def str2bool(word):
    if word.lower() == 'true':
        return True
    else:
        return False
