#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Read pages from Parameter namespace in old wiki and save in new wiki."""

import requests
import pywikibot
import pywikibot.pagegenerators
import config


PARAMETER_NS = 104

old_site = pywikibot.Site('en', 'siriuswiki')

g = pywikibot.pagegenerators.AllpagesPageGenerator(
    site=old_site,
    namespace=PARAMETER_NS
)

titles = []
for page in g:
    titles.append(page.title())

BASEURL = 'http://10.0.21.132/mediawiki-1.23.1/index.php'

USER = config.user
PASSWORD = config.password
APIURL = config.baseurl + 'api.php'
REASON = 'Change parameter naming scheme'

prms = '?action=login&lgname=%s&lgpassword=%s&format=json' % (USER, PASSWORD)

r1 = requests.post(APIURL+prms)

token = r1.json()['login']['token']
prms += '&lgtoken=%s' % token

r2 = requests.post(APIURL + prms, cookies=r1.cookies)

edit_token_prms = '?action=tokens&type=edit&format=json'
r3 = requests.post(APIURL+edit_token_prms, cookies=r1.cookies)
edit_token = r3.json()['tokens']['edittoken'].replace('+\\', '%2B%5C')

num_titles = len(titles)
i = 1
for title in titles:
    edit_prms = '?title=%s&action=edit&token=%s' % (title, edit_token)
    r4 = requests.get(BASEURL+edit_prms, cookies=r1.cookies)
    spos = r4.text.find('==Data==')
    epos = r4.text.find('</textarea>')
    text = r4.text[spos:epos].replace('&lt;', '<')
    print('Writing page %d/%d...' % (i, num_titles))
    i += 1
    with open('parameters/%s' % (title), 'w') as f:
        f.write(text.encode('utf-8'))
