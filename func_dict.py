# define function dictionary

function_dict = {
             # quantitative indicators
    
             "credit_score":credit_score,
             "equity_value":equity_value,
             "operational_income":operational_income,
             "current_ratio":current_ratio,
             "activity_ratio":activity_ratio,
             "equity_ratio":equity_ratio,
             "profitability_ratio":profitability_ratio,
             "human_insurance":human_insurance,
             "asset_insurance":asset_insurance,
             "income_per_capita":income_per_capita,
             "employee_efficiency":employee_efficiency,
             "employee_count":employee_count,
             "state_gdp_share":state_gdp_share,
             "state_area_income_share":state_area_income_share,
             "export_total_value":export_total_value,
             "export_items":export_items,
             "export_power":export_power,
             "export_per_capita":export_per_capita,
             "export_items_share":export_items_share,
             "reputation":reputation,
             "last_reg_equity":last_reg_equity,
             "employee_skill":employee_skill,
             "employee_mean_income":employee_mean_income,
             "pattent_count":pattent_count,
             "knowledge_base":knowledge_base,
             "cti":cti,
             "member_share":member_share,
             "meeting_attendance":meeting_attendance,
             "legal_reserve_adequacy":legal_reserve_adequacy,
             "union_membership":union_membership,
             "deprived_areas_asset":deprived_areas_asset,
             "base_location":base_location,
             "tax_debt":tax_debt,
             "financial_audit":financial_audit,
             "intime_general_meeting":intime_general_meeting,
             "intime_board_meeting":intime_board_meeting,
              
             # qualitative indicators
    
             "rd_unit":rd_unit,
             "production_diversity_growth":production_diversity_growth,
             "strategic_program":strategic_program,
             "operational_program":operational_program,
             "online_sales":online_sales,
             "standards":standards,
             "beneficial_adcost":beneficial_adcost,
             "awards":awards,
             "brand":brand,
             "branch_count":branch_count,
             "marketing_unit":marketing_unit,
             "knowledgebase_brand":knowledgebase_brand,
             "knowledgebase_product":knowledgebase_product,
             "knowledgebase_export":knowledgebase_export,
             "environment_to_cost":environment_to_cost,
             "environment_standard":environment_standard,
             "energy_to_income":energy_to_income,
             "nonprofit_to_cost":nonprofit_to_cost,
             "social":social,
             "priority_partnership":priority_partnership,
             "social_concern":social_concern,
             "member_growth":member_growth,
             "member_satisfaction":member_satisfaction,
             "customer_satisfaction":customer_satisfaction,
             "supplier_satisfaction":supplier_satisfaction,
             "relative_price":relative_price,
             "meeting_participation":meeting_participation,
             "hightech_product":hightech_product,
             "product_growth":product_growth
}

# define indicator function selector

def indicator(my_ind,x):
#     try:
    return function_dict[my_ind](x)
#     except:
#         raise Exception("indicator function error: indicator not in list")
