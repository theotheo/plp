from github import Github

import os
import requests
import click
from tqdm import tqdm

REPOS_DIR = 'data/'

g = Github()

def download_repo(r, dir):
    fn = '{}/{}.zip'.format(dir, r.name)

    if not os.path.exists(fn):
        archive_link = r.get_archive_link('zipball')
        f = requests.get(archive_link)

        with open(fn, 'wb') as z:
            z.write(f.content)

    return fn


@click.command()
@click.option('--pages', default=1, help='Number of pages.')
@click.option('--query', prompt='Github search query', default='stars:>50 language:"Jupyter Notebook"',
    show_default=True)
@click.option('--dir', default=REPOS_DIR, help='Directory to save repos (default: {})'.format(REPOS_DIR))
def get_repos(pages, query,  dir):
    res = g.search_repositories(query)

    for i in tqdm(range(pages)):
        page = res.get_page(i)
        if page:
            for repo in tqdm(page):
                print(repo.description)
                download_repo(repo, dir)

if __name__ == '__main__':
    get_repos()
