import glob
import os
from datetime import datetime


def get_tags(file):
    # tags: [dict, def]
    # title: Material para o curso de python
    tags = []
    description = ''
    with open(file) as f:
        for line in f.readlines():
            line = line.strip()
            if line.startswith('tags:') and '[' in line and ']' in line:
                line = line[line.index('[')+1:].replace(']', '').strip()
                tags = [word.strip()
                        for word in line.split(',')
                        if word.strip()]
            elif line.startswith('title:'):
                description = line.split(
                    ':', 1)[1].replace('Python - ', '').strip()

    return tags, description


def update_index(index, tags, links):
    print(f'Atualizando {index}...')
    links.sort(key=lambda x: x[1].upper())
    tags = sorted(list(set(tags)))
    tmp = index+'.tmp'
    with open(tmp, 'w') as f:
        f.write("""---
title: Curso de Python
description: Material para o curso de python
---
# Tópicos

""")
        for filename, filedescription in links:
            mtime = datetime.fromtimestamp(
                os.path.getmtime(filename)).strftime('%d/%m/%Y %H:%M')
            print(f' + {filename}: {filedescription} @ {mtime}')
            filename = os.path.basename(filename).replace('.md', '')
            f.write(f'- [{filedescription}]({filename}) @ {mtime}\n')

        f.write('\n## Tags\n\n')
        print(f'\n + Tags: {tags}')
        for tag in tags:
            f.write(f'[{tag}](/?tag={tag}) ')
        f.write('\n')
        f.write(
            f'\nPublicado em: {datetime.now().strftime("%d/%m/%Y %H:%M")}\n')

    if os.path.isfile(index):
        mtime = datetime.fromtimestamp(os.path.getmtime(index))
        bkp = index+'.'+mtime.strftime('%Y%m%d%H%M%S')
        os.rename(index, bkp)
    os.rename(tmp, index)


index = 'python-curso.md'
tags = []
links = []

for file in glob.glob('python-*.md'):
    if file == index:
        continue
    file_tags, file_description = get_tags(file)
    tags.extend(file_tags)
    if file_description:
        links.append((file, file_description))


update_index(index, tags, links)
