import json
import logging
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import OpenUrlAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

from github import Github

import threading

logger = logging.getLogger(__name__)

hacktricks_url = "https://book.hacktricks.xyz/welcome/readme"
github_url = "https://github.com/carlospolop/hacktricks."

blacklisted_files = [".git", ".gitbook", ".github", ".gitignore"]


def search_files(repo_code, repo, q, root):    
    results = []
    results_file = open("results.txt", "w")
    for file in repo_code:
        if file.name not in blacklisted_files:
            new_filename = root + "/" + file.name
            print(f"checking {new_filename} for {q}")
            if type(repo.get_contents(new_filename)) == list:
                search_files(repo.get_contents(new_filename), repo, q, new_filename)
            else:
                if q in repo.get_contents(new_filename).decoded_content.decode("utf-8"):
                    print(f"{new_filename} contains {q}")
                    results_file.write(f"{new_filename}\n")
                else:
                    continue

def query_github(g, q):
    repo = g.get_repo("carlospolop/hacktricks")
    root = ""
    repo_code = repo.get_contents(root)
    search_files(repo_code, repo, q, root)


def query_hacktricks(q):
    url = f"{url}?q={q}"
    
def open_url(url):
    pass

class SearchHacktricks(Extension):

    def __init__(self):
        super(SearchHacktricks, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())

        

class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []
        g = Github(extension.preferences['github_token'])
        x = threading.Thread(target=query_github, args=(g,event.get_argument(),), daemon=True)
        results = query_github(g, event.get_argument())
        logger.info('preferences %s' % json.dumps(extension.preferences))
        for result in results:
            url = result.url
            result_name = result.split('/')[-1]
            # data = {'name': '%s %s was clicked' % (item_name, i)}
            items.append(ExtensionResultItem(icon='images/icon.png',
                                             name='%s %s' % (result_name),
                                             description=result_name,
                                             on_enter=OpenUrlAction(url)))

        return RenderResultListAction(items)
class ItemEnterEventListener(EventListener):
    
    def on_event(self, event, extension):
        data = event.get_data()
        return RenderResultListAction([ExtensionResultItem(icon='images/icon.png',
                                                           name=data['new_name'],
                                                           on_enter=HideWindowAction())])

if __name__ == '__main__':
    SearchHacktricks().run()
