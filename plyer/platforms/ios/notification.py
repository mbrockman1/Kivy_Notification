"""
https://github.com/kivy/pyobjus/blob/master/docs/source/core_tutorials.rst .

https://developer.apple.com/documentation/usernotifications/scheduling_a_notification_locally_from_your_app?language=objc

https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/SchedulingandHandlingLocalNotifications.html
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
        self._notification_worker.requestAuthorization()

    def _notify(self, **kwargs):

        def string_to_ns(x):
            NSString.alloc().initWithUTF8String_(x)

        local_noti = UNMutableNotificationContent.alloc().init()

        local_noti.title = string_to_ns(kwargs.get('title'))
        local_noti.body = string_to_ns(kwargs.get('message'))

        trigger =\
            UNTimeIntervalNotificationTrigger.triggerWithTimeInterval_repeats_(5, False)
        request = UNNotificationRequest.requestWithIdentifier_content_trigger_(
            objc_str('Five Seconds'),
            local_noti,
            trigger)

        center = UNUserNotificationCenter.currentNotificationCenter()
        center.addNotificationRequest_(request)
        print("Request Sent")

def instance():
    return IosNotification()
