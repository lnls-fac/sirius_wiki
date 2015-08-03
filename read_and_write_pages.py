#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Read pages from Parameter namespace in old wiki and save in new wiki."""

import pywikibot
import pywikibot.pagegenerators


FAC_NS = 102
MACHINE_NS = 116
TABLE_NS = 118

old_site = pywikibot.Site('en', 'siriuswiki')
new_site = pywikibot.Site('en', 'newsiriuswiki')
comment = ('Moving from local wiki')

g = pywikibot.pagegenerators.AllpagesPageGenerator(
    site=old_site,
    namespace=FAC_NS
)

titles = []
for page in g:
    titles.append(page.title())

print(titles)

for title in titles:
    old_page = pywikibot.Page(old_site, title)
    new_page = pywikibot.Page(new_site, title)
    new_page.text = old_page.text
    try:
        # print(new_page.text)
        new_page.save(comment)
    except pywikibot.PageNotSaved:
        print("Error saving %s" % title)
