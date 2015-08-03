#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Read images from Parameter namespace in old wiki and save in new wiki."""

import os
import pywikibot

old_site = pywikibot.Site('en', 'siriuswiki')
new_site = pywikibot.Site('en', 'newsiriuswiki')
comment = ('Moving from local wiki')

g = old_site.allimages()

titles = []
for page in g:
    titles.append(page.title())

print(titles)

for title in titles:
    old_page = pywikibot.ImagePage(old_site, title)
    url = old_page.fileUrl()
    os.system('wget '+url)
    idx = url.rfind('/')
    filename = url[idx+1:]

    try:
        if old_page.text != '':
            new_site.upload(old_page, source_filename=filename, text=old_page.text, comment=old_page.text)
        else:
            new_site.upload(old_page, source_filename=filename, text=old_page.text, comment='Copying from local wiki')
    except:
        print('Error saving %s' % filename)

    # new_page = pywikibot.ImagePage(new_site, title)
    #
    #
    #
    # new_page.text = old_page.text
    # try:
    #     # print(new_page.text)
    #     new_page.save(comment)
    # except pywikibot.PageNotSaved:
    #     print("Error saving %s" % title)
