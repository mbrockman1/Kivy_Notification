#import <Foundation/Foundation.h>
#import <UserNotifications/UserNotifications.h>


@interface NotificationWorker : NSObject {}

- (void)requestNotificationCenter:
        (NSString *)py_title
        withbody:(NSString *)py_body
        withtiming:(int)py_timing
        withid:(NSString *)py_uniqueid
        withrepeat:(bool)py_repeat;
- (void)removePendingNotifications;

@end
