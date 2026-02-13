#!/bin/bash
while true; do date +"%H:%M:%S"; curl -o /dev/null -s -w "code=%{http_code} time=%{time_total}s\n" https://music.yandex.ru/; sleep 1; done