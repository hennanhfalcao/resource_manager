# Resource Manager - API REST

## 📌 Sobre o Projeto
O **Resource Manager** é uma API REST desenvolvida em **Django** e **Django Rest Framework (DRF)** para gerenciamento de cursos e avaliações. O sistema permite CRUD completo para cursos e suas respectivas avaliações, garantindo uma estrutura bem organizada e flexível para futuras expansões.

## 🛠 Tecnologias Utilizadas
- **Django 4.2**
- **Django Rest Framework**
- **SQLite**
- **Django Filters**
- **Token Authentication**

## 🚀 Como Executar o Projeto

### 📂 Clonar o Repositório
```bash
# Clone o repositório para sua máquina
https://github.com/seu-usuario/resource-manager.git

cd resource-manager
```

### 📦 Criar e Ativar um Ambiente Virtual
```bash
# Criar ambiente virtual
python -m venv .venv

# Ativar no Windows
.venv\\Scripts\\activate

# Ativar no Linux/Mac
source .venv/bin/activate
```

### 📥 Instalar Dependências

```bash
pip install -r requirements.txt
```

### 🔧 Aplicar Migrações no Banco de Dados

```bash
python manage.py makemigrations
python manage.py migrate
```

### 🛡 Criar Superusuário

```bash
python manage.py createsuperuser
```

### 🔑 Gerar Token de Autenticação
 1. Acesse o Django Admin: http://127.0.0.1:8000/admin/
 2. Faça login com o superusuário criado.
 3. Vá até a seção Tokens e adicione um novo token para um usuário existente na lista.
 4. Copie o token gerado, ele será usado para autenticação nas requisições.


### 🌱 Executar o Seeding de Dados

```bash
python manage.py seed
```

### ▶️ Rodar o Servidor

```bash
python manage.py runserver
```

O servidor será iniciado em http://127.0.0.1:8000/

---

| ROTAS | MÉTODO | DESCRIÇÃO |
| --- | --- | --- |
| /api/v2/cursos/ | GET | Lista todos os cursos |
| /api/v2/cursos/ | POST | Cria um novo curso |
| /api/v2/cursos/{id} | GET | Obtém detalhes de um curso pelo ID |
| /api/v2/cursos/{id} | PUT | Aualiza um curso pelo ID |
| /api/v2/cursos/{id} | DELETE | Apaga um curso pelo ID |
| /api/v2/cursos/{id}/avaliacoes/ | GET | Lista todas as avaliações de um curso |
| /api/v2/cursos/{id}/avaliacoes/{id} | GET | Obtém detalhes de uma avaliação específica de um curso pelo ID |
| /api/v2/avaliacoes/ | GET | Lista todas as avaliações |
| /api/v2/avaliacoes/{id} | GET | Obtém detalhes de uma avaliação pelo ID |
| /api/v2/avaliacoes/ | POST | Cria uma nova avaliação |
| /api/v2/avaliacoes/{id} | PUT | Atualiza uma avaliação pelo ID |
| /api/v2/avaliacoes/{id} | DELETE | Apaga uma avaliação pelo ID |

### 🔎 Exemplo de Uso de Query Params

```bash
# Filtrar cursos por título
GET /api/v2/cursos/?search=django

# Ordenar cursos por data de publicação
GET /api/v2/cursos/?ordering=publication
```

### 📌 Exemplos de Requisições CRUD
#### 📍 Criar um Curso

```bash
POST /api/v2/cursos/
Content-Type: application/json
{
  "title": "Curso de Django",
  "url": "https://example.com/django"
}
```

#### 📍 Obter Detalhes de um Curso
```bash
GET /api/v2/cursos/1/
```

#### 📍 Atualiza um curso

```bash
PUT /api/v2/cursos/1/
Content-Type: application/json
{
  "title": "Curso de Django Avançado",
  "url": "https://example.com/django-advanced"
}
```

#### 📍 Deletar um curso

```bash
DELETE /api/v2/cursos/1/
```

#### 📍 Criar uma Avaliação

```bash
POST /api/v1/avaliacoes/
Content-Type: application/json
{
  "course": 1,
  "name": "João Silva",
  "email": "joao@example.com",
  "comment": "Ótimo curso!",
  "rating": 5
}
```

#### 📍 Obter todas as Avaliações
```bash
GET /api/v2/avaliacoes/
```