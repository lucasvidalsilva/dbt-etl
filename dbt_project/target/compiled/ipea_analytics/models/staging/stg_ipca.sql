

WITH raw_data AS (
    SELECT * FROM "ipea_macro"."main"."raw_ipca"
)

SELECT
    DATE_TRUNC('month', CAST("DATE" AS DATE)) AS mes_referencia,
    CAST("VALUE (-)" AS FLOAT) AS ipca_indice,
    'IPCA' AS indicador_origem
FROM raw_data
WHERE "VALUE (-)" IS NOT NULL