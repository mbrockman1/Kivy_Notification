#import <UserNotifications/UserNotifications.h>
#import "Blocks.h"

@implementation NotificationWorker
- (void)requestAuthorization {
      UNAuthorizationOptions authOptions = UNAuthorizationOptionAlert |
          UNAuthorizationOptionSound | UNAuthorizationOptionBadge;

    [[UNUserNotificationCenter currentNotificationCenter] requestAuthorizationWithOptions:authOptions
          completionHandler:^(BOOL granted, NSError * _Nullable error) {
               NSLog(@"%i %@",granted, error);
          }];
}

@end
