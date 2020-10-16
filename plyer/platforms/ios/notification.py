"""
https://github.com/kivy/pyobjus/blob/master/docs/source/core_tutorials.rst .

https://developer.apple.com/documentation/usernotifications/scheduling_a_notification_locally_from_your_app?language=objc

https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/SchedulingandHandlingLocalNotifications.html

https://useyourloaf.com/blog/local-notifications-with-ios-10/
"""
from plyer.facades import Notification
from pyobjus import *
from pyobjus.dylib_manager import *

from plyer import uniqueid

load_framework(INCLUDE.Foundation)
load_framework('/System/Library/Frameworks/UserNotifications.framework')

UNMutableNotificationContent = autoclass('UNMutableNotificationContent')
UNNotificationRequest = autoclass('UNNotificationRequest')
UNTimeIntervalNotificationTrigger = autoclass('UNTimeIntervalNotificationTrigger')
UNUserNotificationCenter = autoclass('UNUserNotificationCenter')
NSString = autoclass('NSString')

load_dylib('./UniBlocks.dylib')


class IosNotification(Notification):
    def __init__(self):
        super().__init__()
        self._notification_worker = autoclass('NotificationWorker').alloc().init()

    def _notify(self, **kwargs):
        self._notification_worker.requestNotificationCenter_withbody_withtiming_(
            objc_str(kwargs.get('title')),
            objc_str(kwargs.get('message')),
            kwargs.get('timing'))
        print("Request Sent")

def instance():
    return IosNotification()
