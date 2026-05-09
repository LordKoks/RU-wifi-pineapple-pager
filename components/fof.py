#!/usr/bin/env python3
import json, os, sys

TRANSLATIONS = {
    "ALERTS": "ОПОВЕЩЕНИЯ",
    "RECON": "РАЗВЕДКА",
    "PINEAP": "PINEAP",
    "SETTINGS": "НАСТРОЙКИ",
    "PAYLOADS": "ПОЛЕЗНЫЕ НАГРУЗКИ",
    "About": "О программе",
    "Add Allowed Client": "Добавить разрешённого клиента",
    "Add Allowed Network": "Добавить разрешённую сеть",
    "Add Denied Client": "Добавить запрещённого клиента",
    "Add Denied Network": "Добавить запрещённую сеть",
    "Add Network": "Добавить сеть",
    "Add SSID to Filters": "Добавить SSID в фильтры",
    "Add SSID to Pool": "Добавить SSID в пул",
    "Add to Allow Filter": "Добавить в белый список",
    "Add to Deny Filter": "Добавить в чёрный список",
    "Advertise Networks": "Рекламировать сети",
    "Alert": "Оповещение",
    "Alerts": "Оповещения",
    "Allow": "Разрешить",
    "Allowed Client List": "Список разрешённых клиентов",
    "Allowed Network List": "Список разрешённых сетей",
    "Audio Mode:": "Режим звука:",
    "Audio Source:": "Источник звука:",
    "Author:": "Автор:",
    "BSSID Override": "Подмена BSSID",
    "Background Audio": "Фоновый звук",
    "Background Changes": "Смена фона",
    "Battery Critical": "Батарея критически низкая",
    "Battery Low": "Батарея низкая",
    "Battery:": "Батарея:",
    "Battery: ...": "Батарея: ...",
    "Baud Rate": "Скорость передачи",
    "Bluetooth": "Bluetooth",
    "Boot": "Загрузка",
    "Brightness": "Яркость",
    "Cache Debug Log": "Кэш отладочного лога",
    "Cancel": "Отмена",
    "Channel:": "Канал:",
    "Check for Updates": "Проверить обновления",
    "Clear": "Очистить",
    "Clear Networks": "Очистить сети",
    "Client": "Клиент",
    "Client Filter:": "Фильтр клиентов:",
    "Client Mode": "Режим клиента",
    "Client Mode Setup": "Настройка режима клиента",
    "Clients": "Клиенты",
    "Clients:": "Клиенты:",
    "Clock": "Часы",
    "Collect Handshakes": "Сбор хендшейков",
    "Collect Probes": "Сбор проб",
    "Configuration": "Конфигурация",
    "Congratulations!": "Поздравляем!",
    "Connected Clients": "Подключённые клиенты",
    "Continue to Dashboard": "Перейти к панели",
    "Current Version:": "Текущая версия:",
    "D-Pad LED": "Подсветка D-Pad",
    "Data Debug Log": "Лог данных отладки",
    "Day": "День",
    "Deauth All Clients": "Деаутентификация всех",
    "Deauth Client": "Деаутентификация клиента",
    "Deauth Flood Detected": "Обнаружен деаут-флуд",
    "Denied Client List": "Список запрещённых клиентов",
    "Denied Network List": "Список запрещённых сетей",
    "Deny": "Запретить",
    "Depth:": "Глубина:",
    "Dim Brightness": "Тусклая яркость",
    "Dim Timeout": "Таймаут затемнения",
    "Display": "Дисплей",
    "Edit": "Изменить",
    "Encryption Type": "Тип шифрования",
    "Encryption:": "Шифрование:",
    "Error": "Ошибка",
    "Event Debug Log": "Лог событий отладки",
    "Evil WPA": "Злая WPA",
    "Evil WPA AP": "Злая WPA точка",
    "Evil WPA Setup": "Настройка злой WPA",
    "Factory Reset": "Сброс до заводских",
    "Filters": "Фильтры",
    "Flip Screen": "Переворот экрана",
    "Free Disk Space:": "Свободно на диске:",
    "Free Disk Space: ...": "Свободно на диске: ...",
    "Frequency:": "Частота:",
    "GPS": "GPS",
    "General": "Основное",
    "Handshake Captured": "Хендшейк захвачен",
    "Handshakes:": "Хендшейки:",
    "Help": "Справка",
    "Hidden": "Скрытый",
    "Hostname": "Имя хоста",
    "Hour": "Час",
    "I accept the License Agreement": "Принимаю соглашение",
    "Isolated Error Log": "Изолированный лог ошибок",
    "Keep Screen Awake": "Не выключать экран",
    "Lat:": "Широта:",
    "Lat: ....": "Широта: ....",
    "Launch": "Запустить",
    "License": "Лицензия",
    "License Agreement": "Лицензионное соглашение",
    "Lock Buttons": "Блокировка кнопок",
    "Lock Screen": "Блокировка экрана",
    "Lon:": "Долгота:",
    "Lon: ....": "Долгота: ....",
    "Loot:": "Добыча:",
    "Management AP": "Точка управления",
    "Management AP Setup": "Настройка точки управления",
    "Mimic Open Networks": "Имитация открытых сетей",
    "Minute": "Минута",
    "Month": "Месяц",
    "Nerd Stats": "Статистика",
    "Network": "Сеть",
    "Network Filter:": "Фильтр сети:",
    "Network Name": "Имя сети",
    "Network Time (NTP)": "Сетевое время (NTP)",
    "New Client Connected": "Новый клиент подключён",
    "Notices": "Уведомления",
    "Open AP": "Открытая точка",
    "Open Source Licenses": "Лицензии открытого ПО",
    "PIN Code": "PIN-код",
    "PIN Setup": "Настройка PIN",
    "Payloads": "Полезные нагрузки",
    "PineAP": "PineAP",
    "Power": "Питание",
    "Probes:": "Пробы:",
    "Reboot": "Перезагрузка",
    "Recon": "Разведка",
    "Ringtone": "Рингтон",
    "SSID Pool": "Пул SSID",
    "Scan": "Сканирование",
    "Settings": "Настройки",
    "Setup Wizard": "Мастер настройки",
    "Shutdown": "Выключение",
    "Signal:": "Сигнал:",
    "Size:": "Размер:",
    "Start": "Старт",
    "Stop": "Стоп",
    "System": "Система",
    "Theme": "Тема",
    "Time": "Время",
    "Timezone": "Часовой пояс",
    "Updates": "Обновления",
    "Version:": "Версия:",
    "WiFi": "WiFi",
    "Year": "Год",
    "Passphrase": "Парольная фраза",
    "Save": "Сохранить",
    "Evil AP Auth Captured": "Перехвачена аутентификация злой точки",
    "Randomize Address": "Случайный адрес",
    "Click to view\n\nconnected clients": "Нажмите для просмотра\n\nподключённых клиентов",
    "Volume": "Громкость",
    "Vibrate": "Вибрация",
    "Vibrate w/ Ringtone": "Вибрация при звонке",
    "Screen Timeout": "Таймаут экрана",
    "Power Connected": "Питание подключено",
    "Virtual Pager": "Виртуальный пейджер",
    "Root Password": "Пароль root",
    "SSH": "SSH",
    "Serial Device": "Последовательное устройство",
    "Restart GPSd": "Перезапуск GPSd",
    "Tutorial": "Обучение",
    "Sleep Screen": "Спящий экран",
    "Press 'A'\nto unlock": "Нажмите 'A'\nдля разблокировки",
    "UI Debug Log": "Лог отладки интерфейса",
    "Render Debug Log": "Лог отладки рендеринга",
    "Stats Debug Log": "Лог отладки статистики",
    "Service Debug Log": "Лог отладки сервиса",
    "Trace ": "Трассировка ",
    "Write logs to disk": "Записывать логи на диск",
    "Restart Server": "Перезапустить сервер",
    "Restart PineAPd": "Перезапустить PineAPd",
    "Restart Networking": "Перезапустить сеть",
    "Restart Device": "Перезапустить устройство",
    "Targeted Payload": "Целевая полезная нагрузка",
    "Recon Audio": "Звук разведки",
    "Radio Settings": "Настройки радио",
    "Save to Recon DB": "Сохранить в БД разведки",
    "Record PCAP": "Запись PCAP",
    "Wigle Mode": "Режим Wigle",
    "Access Point Data": "Данные точки доступа",
    "Packets:": "Пакеты:",
    "Second": "Секунда",
    "Uptime:": "Время работы:",
    "Uptime: ...": "Время работы: ...",
    "Temperature:": "Температура:",
    "Temperature: ...": "Температура: ...",
    "WAN IP:": "WAN IP:",
    "WAN IP: ...": "WAN IP: ...",
    "Packages:": "Пакеты:",
    "Current theme missing LIST_PICKER component": "В текущей теме отсутствует компонент LIST_PICKER",
    "Welcome": "Добро пожаловать",
    "Password": "Пароль",
    "WELCOME, HACKER": "ДОБРО ПОЖАЛОВАТЬ, ХАКЕР",
    "To the WiFi Pineapple Pager.\n\nLet's get started by going\n\nover a few important notices\n\nand configuring your device.":
        "Добро пожаловать в WiFi Pineapple Pager.\n\nДавайте начнём с ознакомления\n\nс важными уведомлениями\n\nи настройки устройства.",
    "Press down to continue.": "Нажмите вниз для продолжения.",
    "NOTICE: Firmware": "УВЕДОМЛЕНИЕ: Прошивка",
    "Welcome to the cutting edge.\n\nNew features are released\n\noften. Please give feedback\n\nand join the community at\n\nhttps://hak5.org/pager":
        "Добро пожаловать на передовую.\n\nНовые функции выходят\n\nчасто. Оставляйте отзывы\n\nи присоединяйтесь к сообществу:\n\nhttps://hak5.org/pager",
    "NOTICE: Thermals": "УВЕДОМЛЕНИЕ: Температура",
    "Ensure adequate airflow.\n\nDO NOT block cooling vents.\n\n\nThe screen will be HOT to\n\nthe touch with extended use.":
        "Обеспечьте достаточную вентиляцию.\n\nНЕ блокируйте вентиляционные\n\nотверстия. Экран будет ГОРЯЧИМ\n\nпри длительном использовании.",
    "NOTICE: Charging": "УВЕДОМЛЕНИЕ: Зарядка",
    "Fully charge before each use\n\nusing a compatible charger.\n\n‎‎‎USB-C smartphone chargers\n\n‎‎‎Most computer USB-C ports\n\nLearn more at hak5.org/pager":
        "Полностью заряжайте перед каждым\n\nиспользованием совместимым\n\nзарядным устройством.\n\nUSB-C зарядки смартфонов\n\nБольшинство USB-C портов ПК\n\nУзнайте больше: hak5.org/pager",
    "PIN CODE": "PIN-КОД",
    "You may set a PIN Code for\n\nuse when locking the screen.":
        "Вы можете установить PIN-код\n\nдля блокировки экрана.",
    "Set PIN Code": "Установить PIN-код",
    "Press the green 'A' button to set a PIN,\nor press down to skip this for now.":
        "Нажмите зелёную кнопку 'A' для установки PIN,\nили нажмите вниз, чтобы пока пропустить.",
    "ROOT PASSWORD": "ПАРОЛЬ ROOT",
    "Set a root password for SSH\n\nand Virtual Pager access.":
        "Установите пароль root для SSH\n\nи доступа к Virtual Pager.",
    "Set Password": "Установить пароль",
    "Press the green 'A' button to set the\npassword, then press down to continue.":
        "Нажмите зелёную кнопку 'A' для установки\nпароля, затем нажмите вниз для продолжения.",
    "SET TIMEZONE": "УСТАНОВКА ЧАСОВОГО ПОЯСА",
    "Set your timezone now to\n\nenable over-the-air updates.":
        "Установите часовой пояс сейчас,\n\nчтобы включить обновления по воздуху.",
    "Set Timezone": "Установить часовой пояс",
    "Press the green 'A' button to set the\ntimezone, then press down to continue.":
        "Нажмите зелёную кнопку 'A' для установки\nчасового пояса, затем вниз для продолжения.",
    "This pentest tool is intended for \nauthorized auditing & security analysis \nonly where permitted. Subject to local\nand international laws where applicable.\nUsers solely responsible for compliance.\n\nHak5 LLC claims no responsibility for\nunauthorized or unlawful use.":
        "Этот инструмент для пентеста предназначен\nтолько для авторизованного аудита и\nанализа безопасности, где это разрешено.\nСогласно местным и международным законам.\nПользователи несут полную ответственность\nза соблюдение требований.\n\nHak5 LLC не несёт ответственности за\nнесанкционированное или незаконное использование.",
    "Full terms: https://hak5.org/license": "Полные условия: https://hak5.org/license",
    "Your WiFi Pineapple Pager\nis now ready to use.":
        "Ваш WiFi Pineapple Pager\nтеперь готов к использованию.",
    "Power Disconnected": "Питание отключено",
    "Payload Complete": "Полезная нагрузка завершена",
    "Double-tap the power button to open\nthe quick access menu. From here you\ncan perform actions at any time like\nlocking the screen or shutting down\nthe Pager. Press the B or power\nbutton again to dismiss it.":
        "Дважды нажмите кнопку питания, чтобы\nоткрыть меню быстрого доступа. Отсюда\nможно в любое время заблокировать экран\nили выключить Pager. Нажмите B или\nкнопку питания ещё раз, чтобы закрыть.",
    "The 'A' button (Green) is typically\nused to interact with the selected\nelement.\n\nThe 'B' button (Red) is usually used\nto return to the previous screen.":
        "Кнопка 'A' (зелёная) обычно используется\nдля взаимодействия с выбранным элементом.\n\nКнопка 'B' (красная) обычно служит\nдля возврата к предыдущему экрану.",
    "The direction buttons (D-Pad) allow\nyou to select on screen elements and\nnavigate menus. Their LED colors can\nbe controlled by payloads or from\nthe Settings > General > D-Pad LED\noptions menu.":
        "Кнопки направления (D-Pad) позволяют\nвыбирать элементы на экране и переме-\nщаться по меню. Цвет их светодиодов\nможно настраивать через полезные\nнагрузки или в меню Настройки >\nОсновное > Подсветка D-Pad.",
    "The status bar displays the time, as\nwell as the battery state, volume,\nbrightness and vibration status.\n\nFrom Recon, the status bar will show\nGPS, database, PCAP and frequency.":
        "Строка состояния показывает время,\nуровень заряда, громкость, яркость\nи статус вибрации.\n\nВ режиме Разведка строка состояния\nотображает GPS, базу данных, PCAP\nи частоту.",
    "The Pager has three main components:\nPineAP, Recon, and Payloads.\n\nIf you have experience with the WiFi\nPineapple or Hak5 gear, these should\nsound familiar. Let's break 'em down":
        "У Pager три основных компонента:\nPineAP, Разведка и Полезные нагрузки.\n\nЕсли вы знакомы с WiFi Pineapple или\nустройствами Hak5, это покажется\nзнакомым. Давайте разберёмся.",
    "PineAP is the engine that allows you\nto perform WiFi attacks. In addition\nto handshake captures, you may mimic\nopen and WPA networks while staying\nwithin the scope of engagement using\nClient and Network filtering.":
        "PineAP — это движок, позволяющий\nпроводить WiFi-атаки. Помимо захвата\nхендшейков, можно имитировать\nоткрытые и WPA-сети, оставаясь в\nрамках задания, используя фильтрацию\nклиентов и сетей.",
    "Recon displays the wireless airspace\nat a glance with graphics, sounds\nand actionable data. Wardrive, save\npacket captures and interact with\nthe WiFi environment using payloads.\nSpeaking of payloads...":
        "Разведка показывает радиоэфир\nнаглядно с графикой, звуками и\nполезными данными. Проводите\nwardriving, сохраняйте захваты\nпакетов и взаимодействуйте с\nWiFi-средой через полезные нагрузки.\nКстати о нагрузках...",
    "Payloads are simple scripts written\nin Bash and DuckyScript that let you\nwield the Linux power of the Pager.\n\nThere are three kinds of payloads:\nAlert, User and Recon.":
        "Полезные нагрузки — это простые\nскрипты на Bash и DuckyScript,\nпозволяющие использовать мощь Linux\nна Pager.\n\nСуществует три вида нагрузок:\nОповещения, Пользовательские и\nРазведка.",
    "Alert payloads automatically trigger\nwhen events occur in the airspace --\nsuch as detecting deauth floods, new\nhandshakes being captured or clients\nconnecting to your WiFi Pineapple\nPager's rogue access point.":
        "Оповещающие нагрузки автоматически\nзапускаются при событиях в эфире —\nнапример, при обнаружении деаут-\nфлуда, захвате новых хендшейков\nили подключении клиентов к ложной\nточке доступа WiFi Pineapple Pager.",
    "User payloads can be run anytime\nfrom the main Dashboard > Payloads\nmenu. You'll find a repository of\ncommunity developed payloads, as\nwell as documentation to write your\nown at https://hak5.org/pager\n":
        "Пользовательские нагрузки можно\nзапускать в любое время из меню\nПанель > Полезные нагрузки. Там\nвы найдёте репозиторий нагрузок,\nсозданных сообществом, а также\nдокументацию по написанию собственных\nна https://hak5.org/pager\n",
    "Recon payloads are a special type\nof payload which execute against a\ntarget observed from within Recon.\n\nUsing Recon payloads, you can easily\ninteract with the WiFi environment.":
        "Нагрузки Разведки — особый тип,\nкоторые выполняются против цели,\nнаблюдаемой в Разведке.\n\nС помощью них можно легко\nвзаимодействовать с WiFi-средой.",
    "Settings is home to many features,\nlike 'Virtual Pager'. It lets you\ninteract with the Pager, access its\nterminal, download loot and more\nfrom a web browser via USB-C or WiFi\nvia the Management Access Point.":
        "В Настройках находится множество\nфункций, например, «Виртуальный\nPager». Он позволяет взаимодейство-\nвать с Pager, получать доступ к\nтерминалу, скачивать добычу и\nмногое другое через браузер по\nUSB-C или WiFi через Точку доступа\nуправления.",
    "The Management Access Point is your\nWiFi Pineapple Pager's private WiFi\nnetwork. It's intended for you, the\noperator, to access the Pager's SSH\nand Virtual Pager interfaces. Set\nit up from the Settings > Network.":
        "Точка доступа управления — это\nчастная WiFi-сеть вашего WiFi\nPineapple Pager. Она предназначена\nдля доступа оператора к интерфейсам\nSSH и Virtual Pager. Настройте её\nв разделе Настройки > Сеть.",
    "You can connect your Pager to the \nInternet from the Network section of\nthe Settings menu. Scroll down to \nClient Mode Setup and follow the \nwizard. Then enable using the Client\nMode toggle switch anytime.\n":
        "Вы можете подключить Pager к\nИнтернету из раздела Сеть в меню\nНастройки. Прокрутите вниз до\nНастройки режима клиента и\nследуйте мастеру. Затем включите\nс помощью переключателя «Режим\nклиента» в любое время.\n",
    "Once connected to the Internet via\nWiFi Client Mode, you're encouraged\nto check for firmware updates from\nthe Settings > Updates menu. Be sure\nto set your Timezone, date and time\nfor a reliable network connection.":
        "После подключения к Интернету через\nрежим WiFi-клиента рекомендуется\nпроверить обновления прошивки в\nменю Настройки > Обновления.\nУбедитесь, что установлен часовой\nпояс, дата и время для стабильного\nсетевого соединения.",
    "That's the gist - now go exploring.\nFind the full documentation, library\nof payloads, ringtones, themes and\nWiFi Pineapple Pager community at:\n\nhttps://hak5.org/pager":
        "Это основа — теперь исследуйте.\nПолная документация, библиотека\nнагрузок, рингтонов, тем и\nсообщество WiFi Pineapple Pager:\n\nhttps://hak5.org/pager",
}

def translate_value(val):
    if isinstance(val, str):
        return TRANSLATIONS.get(val, val)
    elif isinstance(val, dict):
        return {k: translate_value(v) for k, v in val.items()}
    elif isinstance(val, list):
        return [translate_value(item) for item in val]
    return val

def translate_json_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    translated = translate_value(data)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(translated, f, ensure_ascii=False, indent=2)

def main():
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    changed = 0
    for root, dirs, files in os.walk(target_dir):
        for f in files:
            if f.endswith('.json'):
                full_path = os.path.join(root, f)
                try:
                    translate_json_file(full_path)
                    print(f"OK: {full_path}")
                    changed += 1
                except Exception as e:
                    print(f"ERR: {full_path} - {e}")
    print(f"\nFiles processed: {changed}")

if __name__ == '__main__':
    main()