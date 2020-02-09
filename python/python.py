from facebook_scraper import get_posts


x = ['ritardo', 'ritardi', 'chiuso', 'imprevisto', 'fermo', 'carabinieri', 'cancellato', 'cancellati', 'guasto', 'guasti', 'posticipato', 'posticipati', 'arrestato', 'arrestati']
y = [item.upper() for item in x]
y.extend([item.capitalize() for item in x])
x.extend(y)
print(x)
l = []

try:
    for post in get_posts('ilbinario20bis', pages = 15):
        if any(a in post['text'] for a in x):
            #print(post['text'] + '\n')
            l.append(post)
except:
    pass

print(len(l))


import os
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'notizie-2020.txt')
path1 = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'roba_notizie-2020.txt')

with open(path, 'w+', encoding='utf-8') as f:
    for item in l:
        f.write(item['time'].strftime("%d/%m/%Y") + '\n' + item['text'] + ('\n' * 2) + item['post_url'].replace('m.', '').replace('www.', '') + ('\n' * 3))

import json
with open(path1, 'w+', encoding='utf-8') as f:
    f.write(json.dumps(l, indent=4, sort_keys=True, default=str))