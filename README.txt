📋 Полная инструкция для публикации
Вот весь путь от начала до конца — можете выкладывать в интернет как готовый гайд.

Шаг 1: Получить файлы темы с устройства
powershell
scp -r root@172.16.52.1:/lib/pager/themes/wargames C:\Users\Vilka\Desktop\wargames
Шаг 2: Запустить перевод (Python-скрипт)
Сохранить скрипт fof.py (прилагается отдельно) в C:\Users\Vilka\Desktop\

Запустить:

powershell
cd C:\Users\Vilka\Desktop
python fof.py wargames\components
Скрипт переведёт все английские строки в JSON-файлах на русский.

Шаг 3: Загрузить тему обратно на устройство
powershell
scp -r C:\Users\Vilka\Desktop\wargames root@172.16.52.1:/lib/pager/themes/
Шаг 4: Подменить тему через bind mount (обход read-only /rom)
По SSH на устройстве:

bash
mount --bind /lib/pager/themes/wargames /rom/lib/pager/themes/wargames
Шаг 5: Запустить интерфейс
bash
killall -9 pineapple
sleep 2
/pineapple/pineapple &
Шаг 6: Закрепить автозагрузку (чтобы тема не сбрасывалась после перезагрузки)
bash
cat > /etc/rc.local << 'EOF'
mount --bind /lib/pager/themes/wargames /rom/lib/pager/themes/wargames
exit 0
EOF
chmod +x /etc/rc.local
Шаг 7: Если после перезагрузки интерфейс зависает (порт 1471 занят)
bash
/etc/init.d/pineapplepager stop
killall -9 pineapple
sleep 2
/pineapple/pineapple &
⚠️ Известные ограничения
Некоторые длинные русские слова могут не умещаться на экране — требуется ручная подгонка шрифтов или сокращение.

После полной перезагрузки устройства настройки (пароль, яркость) могут сбрасываться из-за проблем с JFFS2 — предложено решение через сохранение на SD-карту.