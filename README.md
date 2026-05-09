# Русская тема для WiFi Pineapple Pager

Полностью переведённая на русский язык тема wargames для WiFi Pineapple Pager от Hak5.

## Что переведено

- Все пункты меню (Dashboard, Recon, PineAP, Settings, Payloads)
- Диалоги (подтверждения, ошибки, ввод данных)
- Подсказки и описания
- Настройки (яркость, громкость, рингтоны, сеть, система)
- Мастер первоначальной настройки
- Обучающие экраны (Tutorial)
- Bluetooth-конфиги
- Payload-скрипты (отчёты, логи)

## Установка

### 1. Скачайте тему
git clone https://github.com/ВАШ_ЛОГИН/wifi-pineapple-pager-russian-theme.git
cd wifi-pineapple-pager-russian-theme

### 2. Загрузите тему на Пейджер
scp -r wargames root@172.16.52.1:/lib/pager/themes/

### 3. Настройте автозагрузку темы (один раз)
ssh root@172.16.52.1
cat > /etc/rc.local << 'EOF'
mount --bind /lib/pager/themes/wargames /rom/lib/pager/themes/wargames
/pineapple/pineapple &
EOF
chmod +x /etc/rc.local

### 4. Перезапустите интерфейс
killall -9 pineapple
sleep 2
/pineapple/pineapple &

## Примечания
- Тема адаптирована под размеры экрана (уменьшены шрифты).
- Некоторые технические надписи (GPS, SSH, FCC ID) оставлены без перевода.
- После перезагрузки тема автоматически восстанавливается через /etc/rc.local
- Перевод осуществлён не полный, ожидайте возможно скоро выкочу обновления и технические исправления.
- Тесты проведены на 1.09 прошивке!!!