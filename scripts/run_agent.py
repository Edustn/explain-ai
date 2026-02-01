from __future__ import annotations

import argparse
import os
import logging
from pathlib import Path

from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.sql import SQLTools


def build_agent(db_path: Path) -> Agent:
    logging.info("Montando agente com banco em %s", db_path)
    db_url = f"sqlite:///{db_path}"
    model_id = os.getenv("GEMINI_MODEL", "gemini-2.0-flash-001")
    logging.info("Modelo configurado: %s", model_id)

    return Agent(
        model=Gemini(id=model_id),
        tools=[SQLTools(db_url=db_url)],
        instructions=[
            "Voce e um analista de saude publica.",
            "Sempre execute a consulta: SELECT * FROM surtos_dengue;",
            "Depois explique os resultados em portugues simples e direto.",
            "Inclua totais (surtos, casos, obitos), municipios com mais casos,",
            "maiores incidencias por 100k, distribuicao por sorotipo e nivel de risco.",
            "Use apenas os dados retornados pelo SQL.",
        ],
        show_tool_calls=True,
        markdown=True,
    )


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )
    logging.info("Iniciando script do agente")
    load_dotenv()

    if not os.getenv("GOOGLE_API_KEY"):
        logging.error("GOOGLE_API_KEY nao configurada")
        raise EnvironmentError(
            "GOOGLE_API_KEY nao configurada. Preencha o arquivo .env "
            "ou exporte a variavel de ambiente."
        )

    parser = argparse.ArgumentParser(
        description="Agente Agno para consultar o SQLite e explicar os resultados."
    )
    parser.add_argument(
        "--question",
        default="Analise todos os dados e gere um resumo explicativo.",
        help="Pergunta ou instrucao para o agente.",
    )
    args = parser.parse_args()
    logging.info("Pergunta recebida: %s", args.question)

    base_dir = Path(__file__).resolve().parents[1]
    db_path = base_dir / "data" / "surtos_dengue.db"
    logging.info("Caminho do banco: %s", db_path)

    if not db_path.exists():
        logging.error("Banco nao encontrado em %s", db_path)
        raise FileNotFoundError(
            "Banco nao encontrado. Rode: python scripts/create_db.py"
        )

    agent = build_agent(db_path)
    logging.info("Executando agente")
    agent.print_response(args.question)
    logging.info("Finalizado")


if __name__ == "__main__":
    main()
