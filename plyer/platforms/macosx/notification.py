"""
https://github.com/kivy/pyobjus/blob/master/docs/source/core_tutorials.rst .

https://developer.apple.com/documentation/usernotifications/scheduling_a_notification_locally_from_your_app?language=objc

https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/SchedulingandHandlingLocalNotifications.html
"""
from plyer.facades import Notification
from pyobjus import *
from pyobjus.dylib_manager import *
import random, string

from plyer import uniqueid

load_framework(INCLUDE.Foundation)
load_framework('/System/Library/Frameworks/UserNotifications.framework')

UNMutableNotificationContent = autoclass('UNMutableNotificationContent')
UNNotificationRequest = autoclass('UNNotificationRequest')
UNTimeIntervalNotificationTrigger = autoclass('UNTimeIntervalNotificationTrigger')
UNUserNotificationCenter = autoclass('UNUserNotificationCenter')
NSString = autoclass('NSString')

make_dylib('./macoslib/Blocks.m', frameworks=['Foundation', 'UserNotifications'])
load_dylib('./macoslib/Blocks.dylib')


class macosNotification(Notification):
    def __init__(self):
        super().__init__()
        self._notification_worker = autoclass('NotificationWorker').alloc().init()

    def _random_string(self):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(10))

    def _notify(self, **kwargs):
        self._notification_worker.requestNotificationCenter_withbody_withtiming_withid_withrepeat_(
            objc_str(kwargs.get('title')),
            objc_str(kwargs.get('message')),
            kwargs.get('timing'),
            objc_str(self._random_string()),
            kwargs.get('repeat'))
        print("Request Sent")

    def _remove_notifications(self):
        self._notification_worker.removePendingNotifications()

def instance():
    return macosNotification()
