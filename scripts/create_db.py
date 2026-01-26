from __future__ import annotations

import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DB_PATH = BASE_DIR / "data" / "surtos_dengue.db"

ROWS = [
    {
        "municipio": "Sao Paulo",
        "estado": "SP",
        "data_inicio": "2024-01-10",
        "data_fim": "2024-02-05",
        "casos_confirmados": 5200,
        "obitos": 8,
        "sorotipo": "DENV-2",
        "faixa_etaria_mais_afetada": "20-39",
        "nivel_risco": "alto",
        "populacao_estimada": 12300000,
    },
    {
        "municipio": "Rio de Janeiro",
        "estado": "RJ",
        "data_inicio": "2024-03-01",
        "data_fim": "2024-03-28",
        "casos_confirmados": 4100,
        "obitos": 6,
        "sorotipo": "DENV-1",
        "faixa_etaria_mais_afetada": "20-39",
        "nivel_risco": "alto",
        "populacao_estimada": 6740000,
    },
    {
        "municipio": "Belo Horizonte",
        "estado": "MG",
        "data_inicio": "2024-02-12",
        "data_fim": "2024-03-08",
        "casos_confirmados": 2600,
        "obitos": 4,
        "sorotipo": "DENV-2",
        "faixa_etaria_mais_afetada": "40-59",
        "nivel_risco": "alto",
        "populacao_estimada": 2530000,
    },
    {
        "municipio": "Salvador",
        "estado": "BA",
        "data_inicio": "2023-11-05",
        "data_fim": "2023-12-02",
        "casos_confirmados": 1800,
        "obitos": 3,
        "sorotipo": "DENV-3",
        "faixa_etaria_mais_afetada": "10-19",
        "nivel_risco": "medio",
        "populacao_estimada": 2900000,
    },
    {
        "municipio": "Recife",
        "estado": "PE",
        "data_inicio": "2024-04-10",
        "data_fim": "2024-05-03",
        "casos_confirmados": 1500,
        "obitos": 2,
        "sorotipo": "DENV-1",
        "faixa_etaria_mais_afetada": "20-39",
        "nivel_risco": "medio",
        "populacao_estimada": 1650000,
    },
    {
        "municipio": "Fortaleza",
        "estado": "CE",
        "data_inicio": "2024-02-20",
        "data_fim": "2024-03-18",
        "casos_confirmados": 2100,
        "obitos": 3,
        "sorotipo": "DENV-2",
        "faixa_etaria_mais_afetada": "20-39",
        "nivel_risco": "alto",
        "populacao_estimada": 2700000,
    },
    {
        "municipio": "Manaus",
        "estado": "AM",
        "data_inicio": "2024-05-12",
        "data_fim": "2024-06-07",
        "casos_confirmados": 1300,
        "obitos": 1,
        "sorotipo": "DENV-4",
        "faixa_etaria_mais_afetada": "0-9",
        "nivel_risco": "medio",
        "populacao_estimada": 2250000,
    },
    {
        "municipio": "Belem",
        "estado": "PA",
        "data_inicio": "2023-12-15",
        "data_fim": "2024-01-12",
        "casos_confirmados": 900,
        "obitos": 1,
        "sorotipo": "DENV-1",
        "faixa_etaria_mais_afetada": "20-39",
        "nivel_risco": "baixo",
        "populacao_estimada": 1500000,
    },
    {
        "municipio": "Brasilia",
        "estado": "DF",
        "data_inicio": "2024-09-03",
        "data_fim": "2024-09-29",
        "casos_confirmados": 1100,
        "obitos": 1,
        "sorotipo": "DENV-2",
        "faixa_etaria_mais_afetada": "20-39",
        "nivel_risco": "medio",
        "populacao_estimada": 3050000,
    },
    {
        "municipio": "Curitiba",
        "estado": "PR",
        "data_inicio": "2024-01-18",
        "data_fim": "2024-02-14",
        "casos_confirmados": 950,
        "obitos": 1,
        "sorotipo": "DENV-1",
        "faixa_etaria_mais_afetada": "40-59",
        "nivel_risco": "baixo",
        "populacao_estimada": 1960000,
    },
    {
        "municipio": "Florianopolis",
        "estado": "SC",
        "data_inicio": "2024-02-05",
        "data_fim": "2024-03-03",
        "casos_confirmados": 620,
        "obitos": 0,
        "sorotipo": "DENV-1",
        "faixa_etaria_mais_afetada": "20-39",
        "nivel_risco": "baixo",
        "populacao_estimada": 540000,
    },
    {
        "municipio": "Porto Alegre",
        "estado": "RS",
        "data_inicio": "2023-10-08",
        "data_fim": "2023-11-01",
        "casos_confirmados": 700,
        "obitos": 1,
        "sorotipo": "DENV-2",
        "faixa_etaria_mais_afetada": "40-59",
        "nivel_risco": "baixo",
        "populacao_estimada": 1490000,
    },
    {
        "municipio": "Goiania",
        "estado": "GO",
        "data_inicio": "2024-03-22",
        "data_fim": "2024-04-16",
        "casos_confirmados": 1450,
        "obitos": 2,
        "sorotipo": "DENV-3",
        "faixa_etaria_mais_afetada": "20-39",
        "nivel_risco": "medio",
        "populacao_estimada": 1550000,
    },
    {
        "municipio": "Cuiaba",
        "estado": "MT",
        "data_inicio": "2024-02-01",
        "data_fim": "2024-02-26",
        "casos_confirmados": 1200,
        "obitos": 2,
        "sorotipo": "DENV-2",
        "faixa_etaria_mais_afetada": "20-39",
        "nivel_risco": "medio",
        "populacao_estimada": 650000,
    },
    {
        "municipio": "Campo Grande",
        "estado": "MS",
        "data_inicio": "2024-01-25",
        "data_fim": "2024-02-18",
        "casos_confirmados": 800,
        "obitos": 1,
        "sorotipo": "DENV-1",
        "faixa_etaria_mais_afetada": "20-39",
        "nivel_risco": "baixo",
        "populacao_estimada": 930000,
    },
    {
        "municipio": "Sao Luis",
        "estado": "MA",
        "data_inicio": "2024-06-03",
        "data_fim": "2024-06-29",
        "casos_confirmados": 980,
        "obitos": 1,
        "sorotipo": "DENV-4",
        "faixa_etaria_mais_afetada": "10-19",
        "nivel_risco": "medio",
        "populacao_estimada": 1110000,
    },
    {
        "municipio": "Teresina",
        "estado": "PI",
        "data_inicio": "2024-07-12",
        "data_fim": "2024-08-07",
        "casos_confirmados": 760,
        "obitos": 1,
        "sorotipo": "DENV-1",
        "faixa_etaria_mais_afetada": "10-19",
        "nivel_risco": "baixo",
        "populacao_estimada": 870000,
    },
    {
        "municipio": "Natal",
        "estado": "RN",
        "data_inicio": "2024-05-02",
        "data_fim": "2024-05-27",
        "casos_confirmados": 640,
        "obitos": 0,
        "sorotipo": "DENV-2",
        "faixa_etaria_mais_afetada": "20-39",
        "nivel_risco": "baixo",
        "populacao_estimada": 890000,
    },
    {
        "municipio": "Uberlandia",
        "estado": "MG",
        "data_inicio": "2024-03-05",
        "data_fim": "2024-03-30",
        "casos_confirmados": 1150,
        "obitos": 2,
        "sorotipo": "DENV-2",
        "faixa_etaria_mais_afetada": "20-39",
        "nivel_risco": "medio",
        "populacao_estimada": 720000,
    },
    {
        "municipio": "Joinville",
        "estado": "SC",
        "data_inicio": "2023-12-01",
        "data_fim": "2023-12-26",
        "casos_confirmados": 540,
        "obitos": 0,
        "sorotipo": "DENV-1",
        "faixa_etaria_mais_afetada": "40-59",
        "nivel_risco": "baixo",
        "populacao_estimada": 600000,
    },
    {
        "municipio": "Aracaju",
        "estado": "SE",
        "data_inicio": "2024-04-02",
        "data_fim": "2024-04-26",
        "casos_confirmados": 690,
        "obitos": 1,
        "sorotipo": "DENV-3",
        "faixa_etaria_mais_afetada": "20-39",
        "nivel_risco": "baixo",
        "populacao_estimada": 680000,
    },
]


def main() -> None:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    if DB_PATH.exists():
        DB_PATH.unlink()

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute(
        """
        CREATE TABLE surtos_dengue (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            municipio TEXT NOT NULL,
            estado TEXT NOT NULL,
            data_inicio TEXT NOT NULL,
            data_fim TEXT NOT NULL,
            casos_confirmados INTEGER NOT NULL,
            obitos INTEGER NOT NULL,
            sorotipo TEXT NOT NULL,
            faixa_etaria_mais_afetada TEXT NOT NULL,
            nivel_risco TEXT NOT NULL,
            populacao_estimada INTEGER NOT NULL,
            incidencia_por_100k REAL NOT NULL
        );
        """
    )

    insert_sql = """
        INSERT INTO surtos_dengue (
            municipio,
            estado,
            data_inicio,
            data_fim,
            casos_confirmados,
            obitos,
            sorotipo,
            faixa_etaria_mais_afetada,
            nivel_risco,
            populacao_estimada,
            incidencia_por_100k
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """

    for row in ROWS:
        incidencia = round(
            (row["casos_confirmados"] / row["populacao_estimada"]) * 100000, 1
        )
        cur.execute(
            insert_sql,
            (
                row["municipio"],
                row["estado"],
                row["data_inicio"],
                row["data_fim"],
                row["casos_confirmados"],
                row["obitos"],
                row["sorotipo"],
                row["faixa_etaria_mais_afetada"],
                row["nivel_risco"],
                row["populacao_estimada"],
                incidencia,
            ),
        )

    conn.commit()
    conn.close()
    print(f"Banco criado em {DB_PATH}")


if __name__ == "__main__":
    main()
