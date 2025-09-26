# Projeto MapaUESC

---

## Estrutura do Repositório

- main: Branch principal, contém a versão estável do projeto.  
- develop: Branch de integração, onde todas as features são testadas antes de irem para a main.  
- feature/nome-do-colaborador: Branchs individuais para cada desenvolvedor trabalhar em suas funcionalidades sem interferir no trabalho dos outros.

Exemplos de branches individuais já criadas:  
- feature/ryan  
- feature/sara  
- feature/lucas  
- feature/daniel  
- feature/maria-eduarda  
- feature/joao-fidelis

---

## Como Acessar o Próprio Branch

1. Clone o repositório caso ainda não tenha feito:

bash
git clone https://github.com/jmfsantos-sys/mapauesc.git
cd mapauesc


2. Verifique todas as branches disponíveis:

bash
git fetch --all
git branch -a


3. Acesse sua branch (substitua joao-fidelis pelo seu nome):

bash
git checkout feature/joao-fidelis


4. Confirme que está na branch correta:

bash
git branch


> A branch que estiver com  é a branch ativa.

---

## Como Trabalhar na Sua Branch

 Faça commits regularmente:

bash
git add .
git commit -m "Descreva a mudança feita"


 Envie suas alterações para o repositório remoto:

bash
git push origin feature/joao-fidelis


---

## Integração com Develop

Quando sua feature estiver pronta:

1. Certifique-se de que sua branch está atualizada com a develop:

bash
git checkout develop
git pull origin develop
git checkout feature/joao-fidelis
git merge develop


2. Resolva qualquer conflito e faça o push.

3. Crie um Pull Request para integrar sua branch na develop.

---

## Instalação e Rodando o Projeto

- 1. Certifique-se de ter Python 3.13+ e pip instalados.

- 2. Crie um ambiente virtual:

bash
python -m venv venv


- 3. Ative o ambiente virtual:

- Windows:

bash
venv\Scripts\activate


- Linux/macOS:

bash
source venv/bin/activate


- 4. Instale as dependências do projeto:

bash
pip install -r requirements.txt


- 5. Rode as migrações do Django:

bash
python manage.py migrate


- 6. Crie um superusuário para acessar o admin (opcional):

bash
python manage.py createsuperuser


- 7. Execute o servidor local:

bash
python manage.py runserver


- 8. Acesse o projeto no navegador:


http://127.0.0.1:8000/

---



