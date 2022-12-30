# test analysis : Here we analyse any indicator and tune the parameters for the indicator, outliers and the scores.

# define indicator functions

# quantitative indicators

def credit_score(x):
    if x.crediting_system_rating >= 250:
        return x.crediting_system_rating
    else:
        return 530

def equity_value(x):
    if x.equity >= 0:
        return x.equity
    else:
        return 0

def operational_income(x):
    if x.operating_income >= 0:
        return x.operating_income
    else:
        return 0

def current_ratio(x):
    if (x.current_assets >= 0) & (x.current_debt > 0):
        return x.current_assets / x.current_debt
    else:
        return 0

def activity_ratio(x):
    if (x.operating_income >=0) & (x.total_assets > 0):
        return x.operating_income / x.total_assets
    else:
        return 0

def equity_ratio(x):
    if (x.equity >= 0) & (x.total_assets > 0):
        return x.equity / x.total_assets
    else:
        return 0

def profitability_ratio(x):
    if (x.total_assets > 0)  & (pd.isna(x.net_profit) == False) & (type(x.net_profit) in [int,float]):
        return x.net_profit / x.total_assets
    else:
        return 0

def human_insurance(x):
    if (x.number_insurance >= 0) & (x.number_of_employees > 0):
        return x.number_insurance / x.number_of_employees
    else:
        return 0

def asset_insurance(x):
    if (x.insured_assets >= 0) & (x.total_assets > 0):
        return x.insured_assets / x.total_assets
    else:
        return 0

def employee_efficiency(x):
    if (x.operating_income >= 0) & (x.manpower_costs > 0):
        return x.operating_income / x.manpower_costs
    else:
        return 0
    
def income_per_capita(x):
    if (x.operating_income >= 0) & (x.number_of_employees > 0):
        return x.operating_income / x.number_of_employees
    else:
        return 0

def employee_count(x):
    if x.number_of_employees >= 0:
        return x.number_of_employees
    else:
        return 0
    
def state_gdp_share(x):
    if (x.operating_income >= 0) & (x.scale_production_per_million > 0):
        return x.operating_income / x.scale_production_per_million
    else:
        return 0

def state_area_income_share(x):
    if (x.operating_income >= 0) & (x.income_province > 0):
        return x.operating_income / x.income_province
    else:
        return 0
    
def export_total_value(x):
    if x.export_value >= 0:
        return x.export_value
    else:
        return 0

def export_items(x):
    if x.number_export_items >= 0:
        return x.number_export_items
    else:
        return 0

def export_power(x):
    if (x.export_value >=0) & (x.operating_income > 0):
        return x.export_value / x.operating_income
    else:
        return 0
    
def export_per_capita(x):
    if (x.export_value >= 0) & (x.number_of_employees > 0):
        return x.export_value / x.number_of_employees
    else:
        return 0

def export_items_share(x):
    if (x.number_export_items >= 0) & (x.number_produced_items > 0):
        return x.number_export_items / x.number_produced_items
    else:
        return 0

def reputation(x):
    if (x.current_year > 0) & (x.established_year > 0):
        return x.current_year - x.established_year
    else:
        return 0

def last_reg_equity(x):
    if x.last_registered_capital >= 0:
        return x.last_registered_capital
    else:
        return 0

def employee_skill(x):
    if (x.number_skill_certificates >= 0) & (x.number_of_employees > 0):
        return x.number_skill_certificates / x.number_of_employees
    else:
        return 0

def employee_mean_income(x):
    if (x.manpower_costs >= 0) & (x.number_of_employees > 0):
        return x.manpower_costs / x.number_of_employees
    else:
        return 0

def pattent_count(x):
    if x.number_of_patents >= 0:
        return x.number_of_patents
    else:
        return 0

def knowledge_base(x):
    if x.knowledge_base_company == 1:
        return 1
    else:
        return 0

def cti(x):
    if x.indicator_CTI >= 0:
        return x.indicator_CTI
    else:
        return 0

def member_share(x):
    if (x.number_cooperative_members >= 0) & (x.average_cooperative_members > 0):
        return x.number_cooperative_members / x.average_cooperative_members
    else:
        return 0

def meeting_attendance(x):
    if (x.number_members_present_last_year >= 0) & (x.number_cooperative_members > 0):
        return x.number_members_present_last_year / x.number_cooperative_members
    else:
        return 0

def legal_reserve_adequacy(x):
    if (x.legal_reserve_reserves >= 0) & (x.capital_last_3_years > 0):
        if x.legal_reserve_reserves >= 0.25 * x.capital_last_3_years:
            return 1
        else:
            return 0
    else:
        return 0
    
def union_membership(x):
    if x.join_related_union == 1:
        return 1
    else:
        return 0

def deprived_areas_asset(x):
    if (x.assets_deprived_areas >= 0) & (x.total_assets > 0):
        return x.assets_deprived_areas / x.total_assets
    else:
        return 0

def base_location(x):
    if x.located_deprived_areas == 1:
        return 1
    else:
        return 0
    
def tax_debt(x):
    if x.tax_debt_5_years > 0:
        return -x.tax_debt_5_years
    else:
        return 0

def financial_audit(x):
    if x.audited_financial_statements == 1:
        return 1
    else:
        return 0

def intime_general_meeting(x):
    if (~np.isnan(x.date_general_meeting_year)) & (~np.isnan(x.end_of_fiscal_year)):
        if (int(str(x.date_general_meeting_year)[:4]) == int(str(x.end_of_fiscal_year)[:4]) + 1) & (12 - abs(int(str(x.date_general_meeting_year)[4:6]) - int(str(x.end_of_fiscal_year)[4:6])) <= 4):
            return 1
        else:
            return 0
    else:
        return 0

def intime_board_meeting(x):
    if (~np.isnan(x.date_general_meeting_management)) & (~np.isnan(x.end_of_fiscal_year)):
        if (int(str(x.date_general_meeting_management)[:4]) >= int(str(x.end_of_fiscal_year)[:4]) - 1) & (int(str(x.date_general_meeting_management)[:4]) <= int(str(x.end_of_fiscal_year)[:4]) + 1):
            return 1
        else:
            return 0
    else:
        return 0
    
# qualitative indicators
    
def rd_unit(x):
    if x.research_and_development == 1:
        return 1
    else:
        return 0

def production_diversity_growth(x):
    if x.increase_in_diversity_compared_to_5_years > 0:
        return x.increase_in_diversity_compared_to_5_years
    else:
        return 0

def strategic_program(x):
    if x.preparation_5year_strategic_plan == 1:
        return 1
    else:
        return 0

def operational_program(x):
    if x.annual_program_for_the_last_5years == 1:
        return 1
    else:
        return 0
    
def online_sales(x):
    if x.using_virtual_sales == 1:
        return 1
    else:
        return 0
        
def standards(x):
    if x.count_received_standard >= 0:
        return x.count_received_standard
    else:
        return 0

def beneficial_adcost(x):
    if x.cost_leads_increase_operational_sales > 0:
        return -x.cost_leads_increase_operational_sales
    else:
        return 0
    
def awards(x):
    if x.number_national_awards_10years >= 0:
        return x.number_national_awards_10years
    else:
        return 0
    
def brand(x):
    if x.having_registered_trademark == 1:
        return 1
    else:
        return 0
    
def branch_count(x):
    if x.count_branch_and_buy_representation >= 0:
        return x.count_branch_and_buy_representation
    else:
        return 0
    
def marketing_unit(x):
    if x.having_research_marketing_unit == 1:
        return 1
    else:
        return 0
    
def knowledgebase_brand(x):
    if x.knowledge_cooperative_brand == 1:
        return 1
    else:
        return 0
    
def knowledgebase_product(x):
    if x.presentation_distrib_knowledge_products == 1:
        return 1
    else:
        return 0
    
def knowledgebase_export(x):
    if x.export_technical_knowledge_products == 1:
        return 1
    else:
        return 0
    
def environment_to_cost(x):
    if x.funds_spent_environmental_issues_total >= 0:
        return x.funds_spent_environmental_issues_total
    else:
        return 0
    
def environment_standard(x):
    if x.having_environmental_standards == 1:
        return 1
    else:
        return 0
    
def energy_to_income(x):
    if x.cooperative_energy_relative_operating_income > 0:
        return -x.cooperative_energy_relative_operating_income
    else:
        return 0

def nonprofit_to_cost(x):
    if x.spending_public_benefit_matters_total >= 0:
        return x.spending_public_benefit_matters_total
    else:
        return 0
    
def social(x):
    if x.is_nature_cooperative_type_social == 1:
        return 1
    else:
        return 0
    
def priority_partnership(x):
    if x.cooperative_participation_priority_projects > 0:
        return x.cooperative_participation_priority_projects
    else:
        return 0
    
def social_concern(x):
    if x.attention_to_social_issues > 0:
        return x.attention_to_social_issues
    else:
        return 0

def member_growth(x):
    if x.average_percentage_increase_number_cooperative >= 0:
        return x.average_percentage_increase_number_cooperative
    else:
        return 0
    
def member_satisfaction(x):
    if x.avg_quality_score_from_org > 0:
        return x.avg_quality_score_from_org
    else:
        return 0
    
def customer_satisfaction(x):
    if x.avg_score_from_org_by_buyers > 0:
        return x.avg_score_from_org_by_buyers
    else:
        return 0
    
def supplier_satisfaction(x):
    if x.avg_quality_ok_score_from_supporter_org > 0:
        return x.avg_quality_ok_score_from_supporter_org
    else:
        return 0
    
def relative_price(x):
    if x.expert_comment_for_avg_product_price >= 0:
        return -x.expert_comment_for_avg_product_price
    else:
        return 0
    
def meeting_participation(x):
    if (x.number_members_present_last_year >= 0) & (x.number_cooperative_members > 0):
        return x.number_members_present_last_year / x.number_cooperative_members
    else:
        return 0
    
def hightech_product(x):
    if x.producing_products_providing_in_direction == 1:
        return 1
    else:
        return 0
    
def product_growth(x):
    if x.growth_provision_products_direction >= 0:
        return x.growth_provision_products_direction
    else:
        return 0
