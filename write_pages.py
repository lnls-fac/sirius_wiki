#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pywikibot


titles = os.listdir('parameters')

comment = ('Moving from local wiki')
site = pywikibot.Site('en', 'newsiriuswiki')

num_titles = len(titles)
num_iteration = 0
num_titles_saved = 0
titles_not_saved = []
while len(titles) > 0:
    for title in titles:
        with open('parameters/'+title, 'r') as f:
            text = f.read()
        page = pywikibot.Page(site, title)
        page.text = text.decode('utf-8')
        try:
            page.save(comment)
            num_titles_saved += 1
        except pywikibot.PageNotSaved:
            print("Error saving %s" % title)
            titles_not_saved.append(title)
    titles = titles_not_saved
    titles_not_saved = []
    num_iteration += 1
    print('Iteration %d - saved titles: %d/%d' % (num_iteration, num_titles_saved, num_titles))
