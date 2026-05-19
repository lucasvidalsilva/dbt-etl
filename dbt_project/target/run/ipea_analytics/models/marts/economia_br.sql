
  
    
    

    create  table
      "ipea_macro"."main_analytics"."economia_br__dbt_tmp"
  
    as (
      

WITH ipca AS (
    SELECT * FROM "ipea_macro"."main_staging"."stg_ipca"
),

pib AS (
    SELECT * FROM "ipea_macro"."main_staging"."stg_pib"
)

SELECT
    ipca.mes_referencia,
    ipca.ipca_indice,
    pib.pib_milhoes_brl,
    ROUND(
        ((ipca.ipca_indice / LAG(ipca.ipca_indice) OVER(ORDER BY ipca.mes_referencia)) - 1) * 100, 
        2
    ) AS ipca_variacao_mensal_pct
FROM ipca
INNER JOIN pib 
    ON ipca.mes_referencia = pib.mes_referencia
ORDER BY ipca.mes_referencia DESC
    );
  
  