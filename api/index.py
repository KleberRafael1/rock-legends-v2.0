import glob
import json
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = Path(__file__).resolve().parent.parent

print("BASE_DIR =", BASE_DIR)

PASTA_IMAGENS = BASE_DIR / "assets" / "figurinhas"
ARQUIVO_FIGURINHAS = BASE_DIR / "data" / "figurinhas.json"

print("JSON =", ARQUIVO_FIGURINHAS)
print("IMAGENS =", PASTA_IMAGENS)

with open(ARQUIVO_FIGURINHAS, encoding="utf-8") as arquivo:
    FIGURINHAS = json.load(arquivo)

print(f"Figurinhas carregadas: {len(FIGURINHAS)}")


@app.get("/figurinhas")
def listar_figurinhas():
    print("Entrou em /figurinhas")
    return FIGURINHAS


@app.get("/figurinhas/{id}/imagem")
def obter_imagem_figurinha(id: int):
    print(f"Imagem {id}")

    id_formatado = f"{id:02d}"
    padrao = str(PASTA_IMAGENS / f"{id_formatado}[!0-9]*")

    arquivos = glob.glob(padrao)

    print("Encontrados:", arquivos)

    if not arquivos:
        raise HTTPException(status_code=404, detail="Imagem não encontrada")

    return FileResponse(arquivos[0])