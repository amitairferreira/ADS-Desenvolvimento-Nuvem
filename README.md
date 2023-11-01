# ADS-Desenvolvimento-Nuvem
## Aplicação na nuvem IaaS
Crie uma aplicação em docker-compose na nuvem consistindo em dois serviços. 

* O primeiro serviço é uma aplicação web. A rota padrão dessa aplicação deve ter uma função que faz uma consulta a um banco de dados e mostra o resultado na tela.  

* O segundo serviço é um banco de dados que precisa ter pelo menos uma tabela. Essa tabela precisa ter pelo menos três linhas de dados.
## Arquitetura da aplicação
```
📁 
  |
  |- 📁 app
  |   |- 📑 Dockerfile
  |   |- 📑 app.py
  |   |- 📑 requirements.txt
  |         
  |- 📁 db
  |   |- 📑 init.sql
  |
  |- 📑 docker-compose.yml

```
