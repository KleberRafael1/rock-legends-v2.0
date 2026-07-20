# 🤘 Rock Legends - Álbum de Figurinhas

> Um álbum de figurinhas digital inspirado nos clássicos álbuns colecionáveis, desenvolvido com **HTML, CSS, JavaScript e FastAPI**, proporcionando uma experiência interativa com animações 3D, efeitos sonoros e carregamento dinâmico das figurinhas.

![Status](https://img.shields.io/badge/status-concluído-success)
![HTML5](https://img.shields.io/badge/HTML-5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS-3-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-F7DF1E?logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?logo=fastapi&logoColor=white)

---

# 📖 Sobre o projeto

O **Rock Legends** é uma aplicação web que recria a experiência clássica de colecionar um álbum de figurinhas, agora em formato digital.

Inspirado nos tradicionais álbuns físicos, o projeto reúne **30 grandes nomes da história do Rock e Heavy Metal**, organizados em categorias temáticas. As páginas podem ser folheadas com animações tridimensionais realistas, acompanhadas por efeitos sonoros sintetizados utilizando a Web Audio API.

Além da experiência visual, o projeto possui um backend desenvolvido em **FastAPI**, responsável por fornecer os dados das figurinhas e disponibilizar as imagens dinamicamente através de uma API REST.

O resultado é uma aplicação moderna que une frontend interativo, backend em Python e uma interface inspirada na estética do Rock.

---

# ✨ Funcionalidades

- 📖 Álbum digital com efeito realista de virada de páginas
- 🎵 Som de páginas utilizando Web Audio API
- 🖼️ Carregamento dinâmico das figurinhas através de API REST
- 🎨 Interface inspirada na estética do Rock e Heavy Metal
- ⚡ Efeito Glitch na capa
- 🌑 Layout Dark Theme
- 💻 Interface responsiva
- ⌨️ Navegação pelo teclado
- 🖱️ Arraste manual das páginas
- 📱 Compatível com dispositivos móveis
- 🚀 Backend desenvolvido com FastAPI

---

# 🎸 Categorias do Álbum

O álbum está dividido em seis categorias:

| Categoria | Conteúdo |
|------------|----------|
| 🎸 PIONEIROS | Chuck Berry, Elvis Presley, Jimi Hendrix, Janis Joplin e Little Richard |
| 🤘 METAL & HARD | Ozzy Osbourne, Robert Plant, Bruce Dickinson, Angus Young e James Hetfield |
| 🔥 PUNK & GRUNGE | Kurt Cobain, Sid Vicious, Chris Cornell, Joey Ramone e Eddie Vedder |
| 🎭 PROG & GLAM | Freddie Mercury, David Bowie, David Gilmour, Geddy Lee e Axl Rose |
| 🇧🇷 BRASIL ROCK | Raul Seixas, Rita Lee, Cazuza, Renato Russo e Tim Maia |
| ⚡ BRASIL METAL | Max Cavalera, Andre Matos, Pitty, Chorão e Kleber Rafael |

Total de **30 figurinhas**.

---

# 🛠️ Tecnologias Utilizadas

## Frontend

- HTML5
- CSS3
- JavaScript (ES6)
- St.PageFlip
- Web Audio API
- Google Fonts

## Backend

- Python
- FastAPI
- Uvicorn
- CORS Middleware

---

# 📂 Estrutura do Projeto

```text
Rock-Legends/
│
├── index.html
├── style.css
├── app.js
├── README.md
│
└── backend/
    │
    ├── main.py
    ├── figurinhas/
    │
    ├── .venv/
    └── __pycache__/
```

---

# ⚙️ Como Executar

## 1️⃣ Clone o repositório

```bash
git clone https://github.com/seu-usuario/rock-legends.git
```

Entre na pasta do projeto.

---

## 2️⃣ Backend

Entre na pasta do backend:

```bash
cd backend
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual.

### Windows

```powershell
.\.venv\Scripts\Activate.ps1
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install fastapi uvicorn
```

Execute o servidor:

```bash
python -m uvicorn main:app --reload
```

O backend ficará disponível em:

```
http://localhost:8000
```

---

## 3️⃣ Frontend

Abra o arquivo `index.html` diretamente no navegador ou utilize uma extensão como **Live Server** no Visual Studio Code.

---

# 🔌 Endpoints da API

## Listar todas as figurinhas

```http
GET /figurinhas
```

Exemplo de resposta:

```json
[
    {
        "id":1,
        "nome":"Chuck Berry",
        "categoria":"PIONEIROS",
        "imagem_url":"/figurinhas/1/imagem"
    }
]
```

---

## Obter imagem de uma figurinha

```http
GET /figurinhas/{id}/imagem
```

Exemplo:

```http
GET /figurinhas/1/imagem
```

---

# 🎨 Recursos Visuais

O projeto foi desenvolvido buscando reproduzir a sensação de um álbum físico.

Entre os principais efeitos implementados estão:

- Efeito Glitch na capa
- Perspectiva 3D
- Sombras dinâmicas
- Página com dobra realista
- Som sintetizado de papel
- Efeito de colagem das figurinhas
- Hover interativo
- Tipografia inspirada no Rock
- Paleta de cores Dark Metal

---

# 🔊 Som

O efeito sonoro das páginas **não utiliza arquivos de áudio**.

O som é sintetizado em tempo real através da **Web Audio API**, utilizando:

- White Noise
- Envelope ADSR
- Band-pass Filter
- Low-pass Filter

O resultado é uma simulação do ruído produzido por páginas sendo folheadas.

---

# 📱 Responsividade

O projeto adapta automaticamente o layout para diferentes resoluções.

- Desktop
- Notebook
- Tablet
- Smartphone

Em dispositivos móveis o álbum passa automaticamente para visualização de página única.

---

# 🚀 Próximas Melhorias

- [ ] Banco de dados para persistência da coleção
- [ ] Login de usuários
- [ ] Sistema de troca de figurinhas
- [ ] Figurinhas raras
- [ ] Sistema de progresso do álbum
- [ ] Compartilhamento em redes sociais
- [ ] Deploy da API
- [ ] Deploy do Frontend
- [ ] Painel administrativo para cadastro de artistas

---

# 📚 Aprendizados

Durante o desenvolvimento deste projeto foram praticados conceitos como:

- Estruturação de aplicações Frontend
- Consumo de APIs REST
- Desenvolvimento Backend com FastAPI
- Manipulação do DOM
- Programação assíncrona com Fetch API
- Eventos de Mouse e Touch
- CSS Grid
- CSS Animations
- Web Audio API
- Organização de projetos Full Stack

---

# 👨‍💻 Autor

**Kleber Rafael Silva**

Analista Fiscal Tech • Desenvolvedor Full Stack • Especialista em Inteligência Artificial

### GitHub

https://github.com/seu-usuario

### LinkedIn

https://linkedin.com/in/seu-perfil

---

## ⭐ Se este projeto foi interessante para você

Considere deixar uma **estrela** no repositório.

Ela ajuda o projeto a alcançar mais pessoas da comunidade.