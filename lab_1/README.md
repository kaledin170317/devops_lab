# Лабораторная 1

Два компонента: `backend/` (Flask, счётчик посещений) и `db/` (PostgreSQL). У каждого свой Dockerfile. `compose.yaml` собирает и запускает контейнеры, данные БД хранит в volume. `deploy.yml` через Ansible устанавливает Docker, Compose и Git, доставляет приложение и запускает его.

Нужны Ansible на вашей машине, SSH-доступ к серверу Debian 13 или Ubuntu 24.04. Адрес и пользователь указаны в `inventory.ini`.

Из папки `lab_1` запустите один из вариантов:

```bash
# Скопировать файлы с текущей машины
ansible-playbook -i inventory.ini deploy.yml -e deploy_from_local=true

# Клонировать опубликованный репозиторий (ветка main) на сервер
ansible-playbook -i inventory.ini deploy.yml -e "git_repo=https://github.com/USER/devops_lab.git"
```

Результат: http://77.91.90.36:8000 — счётчик растёт при обновлении страницы. Перед запуском из Git сохраните `lab_1` в коммите и отправьте ветку `main` в удалённый репозиторий.
