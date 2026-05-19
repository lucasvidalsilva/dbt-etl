
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    

select
    mes_referencia as unique_field,
    count(*) as n_records

from "ipea_macro"."main_analytics"."economia_br"
where mes_referencia is not null
group by mes_referencia
having count(*) > 1



  
  
      
    ) dbt_internal_test