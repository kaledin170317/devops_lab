# Лабораторная 1

- `backend/` — Flask-приложение со счётчиком.
- `db/` — PostgreSQL, хранит счётчик.
- `Dockerfile` в каждой папке — сборка образа компонента.
- `compose.yaml` — запуск контейнеров.
- `deploy.yml` — установка Docker и Compose, загрузка проекта из Git и запуск на сервере.

Запуск с машины, где установлен Ansible и есть SSH-доступ к серверу Debian 13 (из папки `lab_1`):

```bash
ansible-playbook -i inventory.ini deploy.yml
```

Приложение: http://77.91.90.36:8000
