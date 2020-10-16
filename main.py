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
        timing = self.ids.timing_text.text
        repeat = self.ids.repeat_text.active
        kwargs = {'title': title, 'message': message,
                  'timing': timing, 'repeat': repeat}

        notification.notify(**kwargs)

    def remove_notifications(self):
        notification.remove_notifications()

    def repeat_active(self, state):
        repeat_bool = False
        if state:
            repeat_bool = True
        else:
            repeat_bool = False
        return repeat_bool



class NotificationDemoApp(App):
    def build(self):
        return NotificationDemo()

    def on_pause(self):
        return True


if __name__ == '__main__':
    NotificationDemoApp().run()
