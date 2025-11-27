
# 🛍️ Aurora Joias & Semijoias

![Django](https://img.shields.io/badge/Django-5.2-green?style=for-the-badge&logo=django)
![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)

Plataforma completa de e-commerce para joias e semijoias desenvolvida em **Django**, com design elegante, responsivo e experiência premium. O sistema oferece catálogo de produtos, controle de estoque, autenticação de usuários, pedidos e área de contato integrada.

🌐 **[Acessar demo](https://kalebemenezes.pythonanywhere.com)**

---

## ✨ Características Principais

### 🎨 Interface Moderna
- Layout **totalmente responsivo**
- Navegação fluida com **scroll suave**
- Menu mobile com animação
- Paleta dourada premium (`#D4AF37`)
- Tipografia refinada (Cormorant Garamond + Montserrat)
- Botão "voltar ao topo"
- Cards de produtos com hover animado

### 👤 Autenticação de Usuários
- Cadastro e login com validação
- Login seguro com CSRF protection
- Nome do usuário exibido no menu
- Página de **perfil** com histórico de pedidos
- Logout seguro

### 🛍️ Catálogo de Produtos
- Exibição elegante de cards com:
  - Imagem
  - Descrição
  - Preço
  - Botão “Comprar”
- Sistema de pedidos integrado
- Atualização automática de estoque
- Página de compra individual com cálculo do total

### 📩 Contato e Suporte
- Formulário de contato estilizado
- Informações de endereço, WhatsApp e e-mail
- Ícones SVG responsivos

---

## 🏗️ Tecnologias Utilizadas

### **Backend**
- Django 5.2  
- Python 3.11+  
- SQLite  
- Pillow  
- django-crispy-forms  
- crispy-bootstrap5  

### **Frontend**
- HTML5  
- CSS3  
  - Flexbox  
  - Media Queries  
  - Animações  
  - Variáveis CSS  
- JavaScript ES6+  
  - Menu mobile  
  - Smooth scroll  
  - Form validation  

### **Design**
- Google Fonts  
- SVG Icons  
- Paleta:
  - Dourado `#D4AF37`
  - Preto `#1A1A1A`
  - Off-white `#F5F5F0`

---

## 📁 Estrutura do Projeto

```
Aurora-Joias-e-semijoias/
│
├── app/
│   ├── migrations/
│   ├── templates/
│   │   ├── comprar.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── perfil.html
│   │   ├── pedido_finalizado.html
│   │   └── salvar-usuario.html
│   ├── static/
│   │   └── styles/
│   │       └── style.css
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── projeto/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── media/
├── staticfiles/
├── requirements.txt
├── README.md
├── db.sqlite3
└── manage.py
```

---

## ⚙️ Instalação e Execução

### 1️⃣ Clonar repositório

```bash
git clone https://github.com/KalebeMenezesMj/Aurora-Joias-e-semijoias.git
cd Aurora-Joias-e-semijoias
```

### 2️⃣ Criar ambiente virtual

**Linux/Mac**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Preparar banco de dados

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Criar superusuário

```bash
python manage.py createsuperuser
```

### 6️⃣ Coletar arquivos estáticos

```bash
python manage.py collectstatic --noinput
```

### 7️⃣ Rodar servidor

```bash
python manage.py runserver
```

Acesse:  
- **Site:** http://127.0.0.1:8000  
- **Admin:** http://127.0.0.1:8000/admin  

---

## 📝 Dependências (requirements.txt)

```txt
Django==5.2.8
Pillow==11.0.0
django-crispy-forms==2.1
crispy-bootstrap5==0.7
requests==2.31.0
```

---

## 👨‍💻 Autor

**Kalebe Menezes**  
📌 GitHub: https://github.com/KalebeMenezesMj  
📌 LinkedIn: https://www.linkedin.com/in/kalebemenezes  

<div align="center">

💎 **Aurora Joias — Desenvolvido por Kalebe Menezes**  
⭐ Se este projeto foi útil, deixe uma estrela!

</div>
