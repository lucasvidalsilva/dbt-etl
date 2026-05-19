

WITH raw_data AS (
    SELECT * FROM "ipea_macro"."main"."raw_pib"
)

SELECT
    DATE_TRUNC('month', CAST("DATE" AS DATE)) AS mes_referencia,
    CAST("VALUE (R$)" AS FLOAT) AS pib_milhoes_brl,
    'PIB_Mensal' AS indicador_origem
FROM raw_data
WHERE "VALUE (R$)" IS NOT NULL