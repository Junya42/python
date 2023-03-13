#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import feedparser
from cdifflib import CSequenceMatcher
from collections import defaultdict

links = ["http://feeds.feedburner.com/cowcotland", "https://silicon.fr/feed"]

global_list = defaultdict(list)
i = 0
for link in links:
    target = feedparser.parse(link)

    title_list = []
    for entry in target.entries:
        title_list.append(entry.title)
        title_list.append(entry.link)
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
j = 0
for titles in links:
    #print(dir(global_list))
    print("_______________________________________________________")
    print()
    print("\033[1;32mRSS Feed: \033[0m" + titles)
    print()
    content = global_list[j]
    score = defaultdict(list)
    count = 0
    for i in content:
        if count % 2 == 1:
            print("\033[1;33mLink: \033[0m", end="")
        else:
            print("\033[1;34mTitle: \033[0m", end="")
        print(i)
        print()
        count = count + 1
    exit()
    print()
    print("_______________________________________________________")
    print()
    j = j + 1

    struct list {

        tab[content][link];
        float score;
    }

    for (size_t i = 0; i < list1.size(); i++) {

        float score = 0;
        for (size_t j = 0; j < list2.size(); j++) {

            score = scorecompare(list1[i], list2[j]);
            if (score <= 0.25)
                score = 0;
            else
                break;
        }
        if (score == 0) {
            list1.erase(list1.begin() + i);
            i--;
        }
        else
            list1.score = score;
    }