# Projeto: Agente SQLite para Surtos de Dengue

## Objetivo
Este projeto demonstra um fluxo simples de analise de dados com SQLite e um agente Agno. Ele cria um banco de dados de exemplo com surtos de dengue (dados ficticios), executa consultas SQL para recuperar todos os registros e, em seguida, gera uma explicacao automatizada dos resultados.

A ideia e mostrar como:
- Modelar um dataset de surtos em SQLite.
- Usar um agente com ferramentas SQL para buscar os dados.
- Transformar os dados brutos em um resumo interpretavel.

## Estrutura
- `scripts/create_db.py`: cria o banco SQLite e popula com dados de exemplo.
- `scripts/run_agent.py`: agente Agno que executa a consulta e explica os resultados.
- `data/surtos_dengue.db`: arquivo do banco gerado pelo script.
- `.env.example`: exemplo de variaveis de ambiente.

## Como rodar
1) Crie e ative um ambiente virtual:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

2) Instale as dependencias:
```bash
pip install -r requirements.txt
```

3) Configure a chave da API (Gemini):
```bash
cp .env.example .env
# edite o arquivo .env e preencha GOOGLE_API_KEY
```

4) Crie o banco de dados:
```bash
python3 scripts/create_db.py
```

5) Rode o agente:
```bash
python3 scripts/run_agent.py
```

Opcional: envie uma pergunta personalizada:
```bash
python3 scripts/run_agent.py --question "Liste os municipios com mais casos e explique o padrao geral."
```

## Observações
- Os dados sao ficticios e servem apenas para exemplo.
- O agente executa a consulta `SELECT * FROM surtos_dengue;` antes de gerar a explicacao.
- Voce pode trocar o modelo definindo `GEMINI_MODEL` no `.env`.
