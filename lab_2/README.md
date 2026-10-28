# Лабораторная 2

Terraform создаёт контейнеры nginx и Redis в одной Docker-сети. Нужны установленные Docker и [Terraform](https://developer.hashicorp.com/terraform/install#linux).

Из папки `lab_2`:

```bash
export PATH="$HOME/.local/bin:$PATH" # если Terraform установлен в ~/.local/bin
terraform init
terraform apply
docker exec terraform-nginx sh -c 'printf "PING\r\n" | nc -w 2 terraform-redis 6379'
```

Ответ `+PONG` означает, что nginx видит Redis по сети. nginx: http://localhost:8080. Удалить контейнеры: `terraform destroy`.
