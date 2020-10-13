'''
iOS HealthKit

https://developer.apple.com/documentation/healthkit/hkhealthstore

https://github.com/StanfordBioinformatics/healthkit-exporter/blob/master/SCGPM%20HealthKit%20Export/ViewController.swift

---------------------
'''

from pyobjus import autoclass, protocol
from pyobjus.dylib_manager import load_framework
from plyer.facades import HealthKitFacades

load_framework('/System/Library/Frameworks/HealthKit.framework')
HKHealthStore = autoclass('HKHealthStore')


class IOSHealthKit(HealthKit):

    def _configure(self):
        if not hasattr(self, '_healthkit_manager'):
            self._healthkit_manager = HKHealthStore.alloc().init()

    def _get_biologicalSex(self):
        return elf._healthkit_manager.biologicalSex()

def instance():
    '''
    Instance for facade proxy
    '''
    return IOSHealthKit()
