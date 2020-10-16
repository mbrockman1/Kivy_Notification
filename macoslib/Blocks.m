#import <UserNotifications/UserNotifications.h>
#import <Foundation/Foundation.h>
#import "Blocks.h"

// https://useyourloaf.com/blog/local-notifications-with-ios-10/

@implementation NotificationWorker
- (void)requestAuthorization {
      UNAuthorizationOptions authOptions = UNAuthorizationOptionAlert |
          UNAuthorizationOptionSound | UNAuthorizationOptionBadge;

    [[UNUserNotificationCenter currentNotificationCenter] requestAuthorizationWithOptions:authOptions
          completionHandler:^(BOOL granted, NSError * _Nullable error) {
               NSLog(@"%i %@",granted, error);
          }];
}


- (void)requestNotificationCenter:(NSString *)py_title withbody:(NSString *)py_body withtiming:(int)py_timing{
      UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
      UNAuthorizationOptions options = UNAuthorizationOptionAlert + UNAuthorizationOptionSound;

      [center requestAuthorizationWithOptions:options
       completionHandler:^(BOOL granted, NSError * _Nullable error) {
        if (!granted) {
          NSLog(@"Something went wrong");
        }
      }];

      UNMutableNotificationContent *content = [UNMutableNotificationContent new];
      NSLog(@"@", py_title);
      content.title = py_title;
      content.body = py_body;
      content.sound = [UNNotificationSound defaultSound];

      UNTimeIntervalNotificationTrigger *trigger = [UNTimeIntervalNotificationTrigger
        triggerWithTimeInterval:py_timing repeats:NO];

        NSString *identifier = @"UYLLocalNotification";
        UNNotificationRequest *request = [UNNotificationRequest requestWithIdentifier:identifier
          content:content trigger:trigger];

        [center addNotificationRequest:request withCompletionHandler:^(NSError * _Nullable error) {
          if (error != nil) {
            NSLog(@"Something went wrong: %@",error);
          }
        }];



}


@end
