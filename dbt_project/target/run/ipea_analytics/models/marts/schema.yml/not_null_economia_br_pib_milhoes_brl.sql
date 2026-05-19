
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select pib_milhoes_brl
from "ipea_macro"."main_analytics"."economia_br"
where pib_milhoes_brl is null



  
  
      
    ) dbt_internal_test