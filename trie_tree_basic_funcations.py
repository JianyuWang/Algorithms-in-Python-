#!/usr/bin/env python
# encoding: utf-8

_end = '_end_'

def make_trie(*words):
    root = dict()
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})    #loop in to the value of letter,which presents as a dict
        current_dict[_end] = current_dict.setdefault(_end,0) + 1
    return root

def in_trie(trie, word):
    current_dict = trie
    for letter in word:
        if letter in current_dict:
            current_dict = current_dict[letter]
        else:
            return False
    else:
        if _end in current_dict and current_dict[_end] > 0:
        #if _end in current_dict:
            return True
        else:
            return False

def insert_into_trie(trie,*words):
    for word in words:
        current_dict = trie
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict[_end] = current_dict.setdefault(_end,0) + 1

def remove_from_trie(trie, word):
    current_dict = trie
    for letter in word:
        if letter in current_dict:
            current_dict = current_dict[letter]
        else:
            print "word:"+word+" not in trie ,forget about it !"
            break
    else:
        if _end in current_dict:
           current_dict[_end] = 0
        else:
            return False


if __name__ == '__main__':

    trie1 = make_trie('bar', 'barz')
    insert_into_trie(trie1,'foot','footman')
    insert_into_trie(trie1,'foot','footman')
    remove_from_trie(trie1,'foot')
    #trie = make_trie('foo', 'bar', 'baz', 'barz')
    print trie1
    remove_from_trie(trie1,'saber')
    print in_trie(trie1,'foo')
    print in_trie(trie1,'bar')
    print in_trie(trie1,'foot')
    print in_trie(trie1,'footman')
