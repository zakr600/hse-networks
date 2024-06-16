Лабораторная работа 1. Выполнил Кравчук Захар

В папке configs лежат выводы с устройств, описывающие их конфигурацию.
В папке logs лежат выводы с устройств, подтверждающие работоспособность системы.
На изображении "img.png" можно ознакомиться со схемой сети, это снимок экрана в программе "eve-ng"
И файл "lab.unl" содержит экспорт сети из "eve-ng"


Для настройки использовал команды:
1. На клиентах назначил командой "ip [address]/[mask] [gateway]" назначил им нужные ip-адреса и шлюзы
2. Для настройки VLAN на Switch-ах использовал команды
interface [тип_порта][номер_порта]
switchport mode access
switchport access vlan [номер_vlan]
exit
write mem
3. Для настройки статического trunk на Switch-ах:
interface [тип_порта][номер_порта]
switchport mode trunk
switchport trunk encapsulation dot1q
exit
write mem
4. Для настройки STP:
Spanning-tree vlan [номер_vlan] root primary
