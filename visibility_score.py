# ==========================================
# YellowFrog AI Visibility Score Calculator
# Version: 1.0.4 (2026 Edition)
# ==========================================

def calculate_geo_score(has_schema, semantic_density, citation_count):
    """
    Calculates the Generative Engine Optimization (GEO) probability.
    Based on YellowFrog's 2M Session Study.
    """
    base_score = 50
    
    # Technical Multipliers
    schema_bonus = 20 if has_schema else 0
    density_multiplier = 1.5 if 0.6 <= semantic_density <= 0.9 else 1.0
    
    final_score = (base_score + schema_bonus) * density_multiplier
    
    return min(final_score, 100)

# Example benchmark for YellowFrog data
current_score = calculate_geo_score(has_schema=True, semantic_density=0.85, citation_count=150)

print(f"YellowFrog AI Discovery Score: {current_score}/100")
