#!/usr/bin/evn python
# -*- coding: utf-8 -*-

import subprocess as sp
import optparse as oe
import re




def get_arguments():
   parser = oe.OptionParser()
   parser.add_option("-i", "--interface", dest="interface", help = "Interface to change its MAC parser.add option")
   parser.add_option("-m", "--mac", dest="new_mac", help="New Mac address")
   (options, arguments) = parser.parse_args()
   if not options.interface:
       parser.error("[-] Пожалуйста, укажите интерфейс, используйте --help для получения дополнительной информации.")
   elif not options.new_mac:
       parser.error("[-] Пожалуйста, укажите новый MAC-адрес, пользователя --help для получения дополнительной информации.")
   return options


def change_mac(interface, new_mac):
  print("[+] Меняем Mac-адрес  " + interface + "  на  " + new_mac)
  sp.call(["ifconfig", interface, "down"])
  sp.call(["ifconfig", interface, "hw", "ether", new_mac ])
  sp.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifcofig_result = sp.check_output(["ifconfig", interface])
    mac_address_search_resolt = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifcofig_result)

    if mac_address_search_resolt:
        return mac_address_search_resolt.group(0)
    else:
        print("[-] Извините,мы не можем прoчитать ваш MAC-aдрес")



options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Текущий Mac-адрес: "+str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC-адрес был успешно изменён на: "+current_mac)
else:
    print("[-] MAC-адрес не был изменён.")

    
