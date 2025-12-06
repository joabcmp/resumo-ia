# Resumo IA – Text Summarizer (Django + React)

Aplicação web que permite ao usuário registrar-se, fazer login e gerar resumos automáticos de textos usando um modelo de IA local (HuggingFace Transformers).

Este é o **Projeto 1** de uma série de 3 aplicações com stack Python + React + IA, com níveis crescentes de complexidade.

---

## Stack

- **Backend**
  - Python 3.11
  - Django 5
  - Django REST Framework
  - djangorestframework-simplejwt (JWT)
  - django-cors-headers
  - transformers (modelo de sumarização, ex.: `facebook/bart-large-cnn`)

- **Frontend**
  - React + Vite
  - TypeScript
  - Fetch/axios para consumo da API

---

## Arquitetura

- `backend/`
  - `core/` – configuração principal do Django (`settings.py`, `urls.py` etc.)
  - `api/` – app com endpoints de registro, login e resumo
  - `manage.py`
- `frontend/`
  - app React responsável pela interface (login, formulário de texto, exibição do resumo)

Comunicação entre front e back via **API REST**:

- Backend em `http://localhost:8000`
- Frontend em `http://localhost:5173` (Vite)
- Autenticação via **JWT** (header `Authorization: Bearer <token>`)

---

## Como rodar o projeto

### Backend (Django)

cd backend
# criar e ativar o venv (apenas na primeira vez)
python -m venv venv
source venv/Scripts/activate  # Windows + Git Bash

# instalar dependências
python -m pip install -r requirements.txt

# aplicar migrações
python manage.py migrate

# rodar o servidor
python manage.py runserver
O backend ficará disponível em: http://127.0.0.1:8000/

Frontend (React)

Copiar código
cd frontend
npm install
npm run dev
Frontend em: http://localhost:5173/.
