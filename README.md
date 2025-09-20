### Sistema de matrícula (CRUD ALUNOS)

Projeto em Django para cadastro, listagem, edição, exclusão e visualização de alunos.

### Passos para a instalação: 

1. *Clone o repositório*
```bash
https://github.com/ruanhs91/sistema_matricula.git
cd sistema_matricula
```

2. *Crie um ambiente virtual*
```bash 
python -m venv venv 
```

3. *Ative o ambiente virtual*
```bash 
.\venv\Scripts\activate
```

4. *Instale as dependências*
```bash 
pip install -r requirements.txt 
```

5. *Rodar as migrações*
```bash
python manage.py makemigrations
python manage.py migrate
```
6. *Criar superusuário*
```bash
python manage.py createsuperuser 
```

7. *Inicie o servidor*
```bash
python manage.py runserver 
```
