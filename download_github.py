from github import Github

import os
import requests
import zipfile

REPOS_DIR = 'data/'

g = Github()

def download_repo(r, dir=REPOS_DIR):
    fn = '{}/{}.zip'.format(dir, r.name)
    print(r.name)

    if not os.path.exists(fn):
        archive_link = r.get_archive_link('zipball')
        f = requests.get(archive_link)

        with open(fn, 'wb') as z:
            z.write(f.content)

    return fn

res = g.search_repositories(' stars:>50 language:"Jupyter Notebook"')

repos_stat = {}
for i in range(3):
    page = res.get_page(i)
    if page:
        for repo in page:
            print(repo.description)
            download_repo(repo)
            #
            # modules = stats_for_repo(repo)
            # repos_stat[repo.name] = modules
