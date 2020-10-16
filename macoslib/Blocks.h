#import <Foundation/Foundation.h>
#import <UserNotifications/UserNotifications.h>


@interface NotificationWorker : NSObject {}

- (void)requestAuthorization;
- (void)requestNotificationCenter:(NSString *)py_title withbody:(NSString *)py_body withtiming:(int)py_timing;

@end
