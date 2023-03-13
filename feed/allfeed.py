#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import feedparser
from cdifflib import CSequenceMatcher
from collections import defaultdict
import sys

links = ["https://www.zdnet.com/blog/500-words-into-the-future/rss.xml", "https://www.zdnet.com/blog/france/rss.xml"]

global_list = defaultdict(list)
first_count = 0
i = 0
size = len(sys.argv)
if size == 1:
    exit(0)
ratio = float(sys.argv[1]) / 100
for link in links:
    target = feedparser.parse(link)

    title_list = []
    for entry in target.entries:
        title_list.append(entry.title)
        title_list.append(entry.link)
        if i == 0:
            first_count = first_count + 1
        #print(entry.link)
        #print()
    global_list[i].append(title_list)
    i = i + 1

    """    
    sm = CSequenceMatcher(a=title_list[0], b=title_list[1])
    print(title_list[0])
    print()
    print(title_list[1])
    print()
    print(sm.ratio())
    print()
    print()
    """

final_list = []
add = 0
final_count = 0
comp_count = 0
for content_a in global_list[0]:
    score = defaultdict(list)
    count = 0
    for i in content_a:
        if add == 1:
            final_list.append(i)
        add = 0
        if count % 2 == 0:
            score = 0
            for content_b in global_list[1]:
                count_b = 0
                for x in content_b:
                    if count_b % 2 == 0:
                        comp_count = comp_count + 1
                        sm = CSequenceMatcher(a=i, b=x)
                        score = sm.ratio()
                        #print(score)
                        if score > ratio:
                            #print(x)
                            break
                        else:
                            score = 0
                    count_b = count_b + 1
            if score > 0.25:
                add = 1
                final_list.append(i)
                final_count = final_count + 1
        count = count + 1
print("Total Compare values: ", end="")
print(comp_count)
print("Total Values in first RSS Flux: ", end="")
print(first_count)
print("Final Values count: ", end="")
print(final_count)
print()

choice = 1
for ok in final_list:
    if choice:
        print("\033[1;33mTitle: \033[0m", end="")
    else:
        print("\033[1;34mLink: \033[0m", end="")
    print(ok)
    print()
    choice ^= 1
