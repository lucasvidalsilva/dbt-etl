import ipeadatapy as ipea
import duckdb
import os

def ingest_ipea_data():
    print("Conectando à API do IPEA...")

    # PRECOS12_IPCA12: IPCA
    # BM12_PIB12: PIB mensal
    series_map = {
        "raw_ipca": "PRECOS12_IPCA12",
        "raw_pib": "BM12_PIB12"
    }

    os.makedirs("data", exist_ok=True)
    con = duckdb.connect("data/ipea_macro.duckdb")

    for table_name, series_code in series_map.items():
        print(f"Baixando série {series_code} para a tabela {table_name}...")
        
        try:
            df = ipea.timeseries(series_code)
            
            df = df.reset_index()
            
            con.execute(f"DROP TABLE IF EXISTS {table_name}")
            con.execute(f"CREATE TABLE {table_name} AS SELECT * FROM df")
            
            print(f"{len(df)} registros salvos em {table_name}.")
            
        except Exception as e:
            print(f"Erro ao baixar a série {series_code}: {e}")

    con.close()
    print("Ingestão finalizada. Camada RAW pronta para o dbt.")

if __name__ == "__main__":
    ingest_ipea_data()