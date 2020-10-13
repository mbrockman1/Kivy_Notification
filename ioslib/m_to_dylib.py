import os
import sys


def iphone_dev_id_finder():
    buildozer_output = os.popen('security find-identity -v -p codesigning').read().split('\n')
    iphone_dev_id = None
    for output in buildozer_output:
        if "iPhone Developer" in output:
            iphone_dev_id = output[output.index('"iPhone'):]
    return iphone_dev_id


def dylib_m_converter(m_files, flag_dict):
    for file in m_files:
        os.system("CLANG -Os -isysroot %s %s %s -dynamiclib %s -o %s_ios.dylib" %
                  (flag_dict['iossdk'],
                   flag_dict['frameworks'],
                   flag_dict['archs_ios'],
                   file,
                   file[:-2]))
        print("Compiling With %s on %s" %
              (flag_dict['clang'], flag_dict['iossimsdk']))
        os.system("CLANG -Os -isysroot %s %s %s -dynamiclib %s -o %s_sim.dylib" %
                  (flag_dict['iossimsdk'],
                   flag_dict['frameworks'],
                   flag_dict['archs_sim'],
                   file,
                   file[:-2]))
        os.system('codesign -f -s %s %s_ios.dylib' %
                  (flag_dict['iphone_dev_id'],
                   file[:-2]))
        os.system('codesign -f -s %s %s_sim.dylib' %
                  (flag_dict['iphone_dev_id'],
                   file[:-2]))
        os.system('lipo %s_ios.dylib %s_sim.dylib -output Uni%s.dylib -create' %
                  (file[:-2], file[:-2], file[:-2]))
        os.system('codesign -f -s %s Uni%s.dylib' %
                  (flag_dict['iphone_dev_id'],
                   file[:-2]))


m_file_list = [file for file in os.listdir('./')
               if file.endswith('.m')]
print(".M files to build", m_file_list)

iphone_dev_id = iphone_dev_id_finder()
clang = os.popen('xcrun --sdk iphoneos --find clang').read().strip()
iossdk = os.popen('xcrun --sdk iphoneos --show-sdk-path').read().strip()
iossimsdk = os.popen('xcrun --sdk iphonesimulator --show-sdk-path').read().strip()
frameworks = "-framework Foundation -framework UserNotifications"
archs_ios = "-arch armv7 -arch armv7s -arch arm64 -mios-version-min=10.0"
archs_sim = "-arch i386 -arch x86_64 -mios-version-min=10.0"

sh_dict = {
    'iphone_dev_id': iphone_dev_id,
    'clang': clang,
    'iossdk': iossdk,
    'iossimsdk': iossimsdk,
    'frameworks': frameworks,
    'archs_ios': archs_ios,
    'archs_sim': archs_sim

}

print("Compiling With %s on %s" % (clang, iossdk))
print()
print("Making iOS Product With Options", frameworks, archs_ios)
print()
dylib_m_converter(m_file_list, sh_dict)
os.system('cp *.dylib ../')
os.system('rm *.dylib')
