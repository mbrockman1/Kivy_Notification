from os.path import join, dirname, realpath

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from plyer import notification
from plyer.utils import platform


class NotificationDemo(BoxLayout):

    def do_notify(self, mode='normal'):
        title = self.ids.notification_title.text
        message = self.ids.notification_text.text
        ticker = self.ids.ticker_text.text
        kwargs = {'title': title, 'message': message, 'ticker': ticker}

        notification.notify(**kwargs)


class NotificationDemoApp(App):
    def build(self):
        return NotificationDemo()

    def on_pause(self):
        return True


if __name__ == '__main__':
    NotificationDemoApp().run()
