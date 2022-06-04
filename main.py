<<<<<<< HEAD
=======
import json
import logging
from time import sleep
>>>>>>> 7713e939b80fa031af6d18f172937f3c0670c022
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
<<<<<<< HEAD
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

=======
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

logger = logging.getLogger(__name__)

>>>>>>> 7713e939b80fa031af6d18f172937f3c0670c022

class SearchHacktricks(Extension):

    def __init__(self):
<<<<<<< HEAD
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
=======
        super(SearchHacktricks, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())
>>>>>>> 7713e939b80fa031af6d18f172937f3c0670c022


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []
<<<<<<< HEAD
        for i in range(5):
            items.append(ExtensionResultItem(icon='images/icon.png',
                                             name='Item %s' % i,
                                             description='Item description %s' % i,
                                             on_enter=HideWindowAction()))

        return RenderResultListAction(items)

if __name__ == '__main__':
    SearchHacktricks().run()
=======
        logger.info('preferences %s' % json.dumps(extension.preferences))
        for i in range(5):
            item_name = extension.preferences['item_name']
            data = {'new_name': '%s %s was clicked' % (item_name, i)}
            items.append(ExtensionResultItem(icon='images/icon.png',
                                             name='%s %s' % (item_name, i),
                                             description='Item description %s' % i,
                                             on_enter=ExtensionCustomAction(data, keep_app_open=True)))

        return RenderResultListAction(items)


class ItemEnterEventListener(EventListener):

    def on_event(self, event, extension):
        data = event.get_data()
        return RenderResultListAction([ExtensionResultItem(icon='images/icon.png',
                                                           name=data['new_name'],
                                                           on_enter=HideWindowAction())])


if __name__ == '__main__':
    SearchHacktricks().run()
>>>>>>> 7713e939b80fa031af6d18f172937f3c0670c022
