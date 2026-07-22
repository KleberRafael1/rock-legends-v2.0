# 🤘 Rock Legends v2.0 — Digital Sticker Album

> Um álbum de figurinhas digital inspirado nos clássicos álbuns colecionáveis, desenvolvido com **HTML, CSS, JavaScript e FastAPI**, utilizando arquitetura Full Stack e preparado para deploy serverless na Vercel.


![Status](https://img.shields.io/badge/status-concluído-success)
![Deploy](https://img.shields.io/badge/Deploy-Vercel-black?logo=vercel)
![HTML5](https://img.shields.io/badge/HTML-5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS-3-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-F7DF1E?logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?logo=fastapi&logoColor=white)

---

# 📖 Sobre o projeto

O Rock Legends v2.0 é uma aplicação web que recria a experiência nostálgica de colecionar um álbum de figurinhas, trazendo grandes nomes da história do Rock para uma experiência digital interativa.

O projeto reúne 30 lendas do Rock e Heavy Metal, organizadas em categorias temáticas, apresentadas em um álbum virtual com animações tridimensionais de páginas, efeitos sonoros e uma interface inspirada na estética Rock.

A versão 2.0 evoluiu para uma aplicação Full Stack, separando o frontend da camada de dados e utilizando uma API REST desenvolvida com FastAPI para carregar dinamicamente informações e imagens das figurinhas.

A aplicação também foi preparada para execução em produção utilizando deploy serverless através da Vercel.

---

# ✨ Funcionalidades

- 📖 Álbum digital com efeito realista de virada de páginas
- 🎸 Interface inspirada em Rock e Heavy Metal
- 🖼️ Carregamento dinâmico das figurinhas através de API REST
- ⚡ Efeito Glitch na capa
- 🌑 Tema Dark Rock
- 🔊 Som de páginas utilizando Web Audio API
- 🖱️ Navegação por arraste manual
- ⌨️ Controle através do teclado
- 📱 Layout responsivo
- 🚀 Backend desenvolvido com FastAPI
- ☁️ Deploy preparado para Vercel

---


# 🏗️ Arquitetura

A aplicação segue uma arquitetura Full Stack desacoplada.

```text
Frontend (HTML/CSS/JavaScript)
            │
            │ Fetch API
            ▼
 FastAPI (API REST)
            │
            ▼
figurinhas.json
            │
            ▼
assets/figurinhas

```


O frontend consome os dados através de uma API REST, responsável por fornecer tanto os metadados das figurinhas quanto as imagens dinamicamente. Essa arquitetura facilita a manutenção, escalabilidade e o deploy utilizando Serverless Functions na Vercel.


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

## Deploy

- Vercel
- Serverless Functions
- JSON como fonte de dados

---

# 📂 Estrutura do Projeto

```text
Rock-Legends-v2.0/
│
├── api/
│   └── index.py
│
├── assets/
│   └── figurinhas/
│
├── data/
│   └── figurinhas.json
│
├── public/
│   ├── index.html
│   ├── style.css
│   └── app.js
│
├── .gitignore
├── README.md
├── requirements.txt
└── vercel.json

```

---

# ⚙️ Como Executar

## 1️⃣ Clone o repositório

```bash
git clone https://github.com/seu-usuario/rock-legends.git
```

Entre na pasta do projeto.

---


## 2️⃣ Ambiente Python

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
pip install -r requirements.txt
```

Execute o servidor:

```bash
python -m uvicorn api.index:app --reload
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

- [ ] Sistema de autenticação
- [ ] Banco de dados
- [ ] Área administrativa
- [ ] Figurinhas raras
- [ ] Sistema de coleção do usuário
- [ ] Busca por artista
- [ ] Favoritos
- [ ] Modo offline (PWA)

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
- Arquitetura Serverless
- Organização de APIs para Deploy na Vercel

---

# 👨‍💻 Autor

**Kleber Rafael Silva**


**Analista Fiscal Tech | Desenvolvedor Full Stack | Especialista em Inteligência Artificial**


### GitHub

https://github.com/KleberRafael1

### LinkedIn

https://www.linkedin.com/in/kleber-rafael-silva

---

## ⭐ Se este projeto foi interessante para você

Considere deixar uma **estrela** no repositório.

Ela ajuda o projeto a alcançar mais pessoas da comunidade.