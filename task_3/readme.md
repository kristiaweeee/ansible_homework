#Создать 3 виртуалки rrobin, web1, web2
На серверах rrobin, web1, web2 установить nginx.
На серверах web1, web2 Nginx должен работать по порту 8080 и отдавать кастомную страницу, зайдя на которую можно понять на каком сервере вы находитесь.
На сервере rrobin Nginx должен обеспечить балансировку нагрузки серверов web1 и web2 в режиме round-robin. Вес каждого сервера одинаковый.
Установка и настройка всего ПО должна быть обеспечена Ansible-сценарием.
Все файлы по этому заданию выложить в Github и написать ReadMe со скринами работоспособности и инструкцию по запуску вашего Ansible-сценария

https://docs.ansible.com/projects/ansible/latest/dev_guide/index.html
Полезные команды для ansible:
• ansible -C (проверка конфигурации без применения)
• ansible-playbook -D показывает diff
• ansible-playbook —list-hosts хосты на которых будет выполнятся команды
• ansible-galay role init nginx шаблонизация 

Примеры конфигураций для ansible:
• https://github.com/bob4inski/ansible/blob/main/lab4/nginx_serv/tasks/main.yml
• https://github.com/bob4inski/admin-starterpack/tree/main/full-course/week-1/ansible
