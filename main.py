import json
from colorama import Back, Style, Fore

with open('config.json', 'r') as file:
    config = json.load(file)

LicenseWeaponNT = config['LicenseWeaponNT']
LicenseFishNT = config['LicenseFishNT']
LicenseBisNT = config['LicenseBisNT']
LicenseHuntNT = config['LicenseHuntNT']
LicenseWeaponWT = config['LicenseWeaponWT']
LicenseFishWT = config['LicenseFishWT']
LicenseBisWT = config['LicenseBisWT']
LicenseHuntWT = config['LicenseHuntWT']

print(Fore.BLACK + Back.WHITE + "--------------------------------------" + Style.RESET_ALL)
print(Fore.BLACK + Back.WHITE + '----------------BySIYG----------------' + Style.RESET_ALL)
print(Fore.BLACK + Back.WHITE + "--------------------------------------" + Style.RESET_ALL)

num1 = int(input(Fore.BLACK + Back.WHITE + "Лицензии на оружие в не рабочее время:" + Style.RESET_ALL))
num2 = int(input(Fore.BLACK + Back.WHITE + "Лицензии на рыбалку в не рабочее время:" + Style.RESET_ALL))
num3 = int(input(Fore.BLACK + Back.WHITE + "Лицензии на бизнес в не рабочее время:" + Style.RESET_ALL))
num4 = int(input(Fore.BLACK + Back.WHITE + "Лицензии на охоту в не рабочее время:" + Style.RESET_ALL))
num5 = int(input(Fore.BLACK + Back.WHITE + "Лицензии на оружие в рабочее время:" + Style.RESET_ALL))
num6 = int(input(Fore.BLACK + Back.WHITE + "Лицензии на рыбалку в рабочее время:" + Style.RESET_ALL))
num7 = int(input(Fore.BLACK + Back.WHITE + "Лицензии на бизнес в рабочее время:" + Style.RESET_ALL))
num8 = int(input(Fore.BLACK + Back.WHITE + "Лицензии на охоту в рабочее время:" + Style.RESET_ALL))

res1 = LicenseWeaponNT * num1
res2 = LicenseFishNT * num2
res3 = LicenseBisNT * num3
res4 = LicenseHuntNT * num4
res5 = LicenseWeaponWT * num5
res6 = LicenseFishWT * num6
res7 = LicenseBisWT * num7
res8 = LicenseHuntWT * num8

result = res1 + res2 + res3 + res4 + res5 + res6 + res7 + res8

print(Fore.BLACK + Back.WHITE + "Вам необходимо заплатить:", result, "$" + Style.RESET_ALL)