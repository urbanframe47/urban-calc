def adjust_rent(original_rent, median_income, local_vacancy_rate):
    safe_ratio = 0.3  # 30% of income standard
    income_cap = (median_income / 12) * safe_ratio
    adjustment_factor = 1 - (local_vacancy_rate * 0.1)

    if original_rent > income_cap:
        suggested_rent = income_cap * adjustment_factor
    else:
        suggested_rent = original_rent * adjustment_factor

    return round(suggested_rent, 2)
