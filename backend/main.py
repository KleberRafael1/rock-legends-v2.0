from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import glob

# Inicializa a aplicação FastAPI
app = FastAPI()

# Configura o middleware CORS para permitir requisições de qualquer origem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define os caminhos absolutos para a pasta de imagens ("figurinhas")
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# Lista com as 30 figurinhas do álbum
# Figurinhas cujas imagens não existem começadas com o ID correspondente são comentadas
figurinhas = [
    {"id": 1, "nome": "Chuck Berry", "categoria": "PIONEIROS", "imagem_url": "/figurinhas/1/imagem"},
    {"id": 2, "nome": "Elvis Presley", "categoria": "PIONEIROS", "imagem_url": "/figurinhas/2/imagem"},
    {"id": 3, "nome": "Jimi Hendrix", "categoria": "PIONEIROS", "imagem_url": "/figurinhas/3/imagem"},
    {"id": 4, "nome": "Janis Joplin", "categoria": "PIONEIROS", "imagem_url": "/figurinhas/4/imagem"},
    {"id": 5, "nome": "Little Richard", "categoria": "PIONEIROS", "imagem_url": "/figurinhas/5/imagem"},
    {"id": 6, "nome": "Ozzy Osbourne", "categoria": "METAL & HARD", "imagem_url": "/figurinhas/6/imagem"},
    {"id": 7, "nome": "Robert Plant", "categoria": "METAL & HARD", "imagem_url": "/figurinhas/7/imagem"},
    {"id": 8, "nome": "Bruce Dickinson", "categoria": "METAL & HARD", "imagem_url": "/figurinhas/8/imagem"},
    {"id": 9, "nome": "Angus Young", "categoria": "METAL & HARD", "imagem_url": "/figurinhas/9/imagem"},
    {"id": 10, "nome": "James Hetfield", "categoria": "METAL & HARD", "imagem_url": "/figurinhas/10/imagem"},
    {"id": 11, "nome": "Kurt Cobain", "categoria": "PUNK & GRUNGE", "imagem_url": "/figurinhas/11/imagem"},
    {"id": 12, "nome": "Sid Vicious", "categoria": "PUNK & GRUNGE", "imagem_url": "/figurinhas/12/imagem"},
    {"id": 13, "nome": "Chris Cornell", "categoria": "PUNK & GRUNGE", "imagem_url": "/figurinhas/13/imagem"},
    {"id": 14, "nome": "Joey Ramone", "categoria": "PUNK & GRUNGE", "imagem_url": "/figurinhas/14/imagem"},
    {"id": 15, "nome": "Eddie Vedder", "categoria": "PUNK & GRUNGE", "imagem_url": "/figurinhas/15/imagem"},
    {"id": 16, "nome": "Freddie Mercury", "categoria": "PROG & GLAM", "imagem_url": "/figurinhas/16/imagem"},
    {"id": 17, "nome": "David Bowie", "categoria": "PROG & GLAM", "imagem_url": "/figurinhas/17/imagem"},
    {"id": 18, "nome": "David Gilmour", "categoria": "PROG & GLAM", "imagem_url": "/figurinhas/18/imagem"},
    {"id": 19, "nome": "Geddy Lee", "categoria": "PROG & GLAM", "imagem_url": "/figurinhas/19/imagem"},
    {"id": 20, "nome": "Axl Rose", "categoria": "PROG & GLAM", "imagem_url": "/figurinhas/20/imagem"},
    {"id": 21, "nome": "Raul Seixas", "categoria": "BRASIL ROCK", "imagem_url": "/figurinhas/21/imagem"},
    {"id": 22, "nome": "Rita Lee", "categoria": "BRASIL ROCK", "imagem_url": "/figurinhas/22/imagem"},
    {"id": 23, "nome": "Cazuza", "categoria": "BRASIL ROCK", "imagem_url": "/figurinhas/23/imagem"},
    {"id": 24, "nome": "Renato Russo", "categoria": "BRASIL ROCK", "imagem_url": "/figurinhas/24/imagem"},
    {"id": 25, "nome": "Tim Maia", "categoria": "BRASIL ROCK", "imagem_url": "/figurinhas/25/imagem"},
    {"id": 26, "nome": "Max Cavalera", "categoria": "BRASIL METAL", "imagem_url": "/figurinhas/26/imagem"},
    {"id": 27, "nome": "Andre Matos", "categoria": "BRASIL METAL", "imagem_url": "/figurinhas/27/imagem"},
    {"id": 28, "nome": "Pitty", "categoria": "BRASIL METAL", "imagem_url": "/figurinhas/28/imagem"},
    {"id": 29, "nome": "Chorão", "categoria": "BRASIL METAL", "imagem_url": "/figurinhas/29/imagem"},
    {"id": 30, "nome": "Kleber Rafael", "categoria": "BRASIL METAL", "imagem_url": "/figurinhas/30/imagem"},
]

# Endpoint GET "/figurinhas" para listar todas as figurinhas ativas
@app.get("/figurinhas")
def listar_figurinhas():
    # Retorna a lista contendo as figurinhas cadastradas e ativas
    return figurinhas

# Endpoint GET "/figurinhas/{id}/imagem" para retornar a imagem correspondente à figurinha
@app.get("/figurinhas/{id}/imagem")
def obter_imagem_figurinha(id: int):
    # Formata o id recebido com 2 dígitos decimais (ex: 1 -> "01")
    id_formatado = f"{id:02d}"
    
    # Constrói o padrão glob para buscar arquivos na pasta figurinhas/
    # O padrão f"{id_formatado}[!0-9]*" garante que buscará pelo prefixo numérico exato seguido de um caractere não numérico
    padrao_glob = os.path.join(PASTA_IMAGENS, f"{id_formatado}[!0-9]*")
    
    # Realiza a busca no sistema de arquivos
    arquivos_encontrados = glob.glob(padrao_glob)
    
    # Se nenhuma correspondência for encontrada, levanta uma exceção HTTP 404
    if not arquivos_encontrados:
        raise HTTPException(status_code=404, detail="Imagem não encontrada")
    
    # Retorna a primeira imagem encontrada como uma resposta de arquivo (FileResponse)
    return FileResponse(arquivos_encontrados[0])
