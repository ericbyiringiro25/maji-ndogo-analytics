"""
Maji Ndogo Ministry of Agriculture
Module 1: Python Foundations - Procedural Harvest Data Cleaner
"""

def clean_and_aggregate_yields(raw_data):
    """Cleans raw harvest logs and aggregates total production by crop type."""
    aggregated_yields = {}
    
    for row in raw_data:
        # Extract and clean fields
        crop = row.get("crop", "Unknown").strip().capitalize()
        try:
            yield_tons = float(row.get("yield_tons", 0.0))
        except ValueError:
            yield_tons = 0.0  # Handle corrupted numeric entries
            
        if yield_tons < 0:
            continue  # Skip invalid negative records
            
        # Aggregate totals
        if crop not in aggregated_yields:
            aggregated_yields[crop] = 0.0
        aggregated_yields[crop] += yield_tons
        
    return aggregated_yields

if __name__ == "__main__":
    # Sample raw log ingestion simulation
    sample_logs = [
        {"plot_id": "P1", "crop": "maize", "yield_tons": "45.2"},
        {"plot_id": "P2", "crop": "sorghum", "yield_tons": "28.4"},
        {"plot_id": "P3", "crop": "Maize ", "yield_tons": "12.5"},
        {"plot_id": "P4", "crop": "unknown", "yield_tons": "invalid_data"}
    ]
    
    print("Running Python Foundations Data Pipeline...")
    results = clean_and_aggregate_yields(sample_logs)
    
    print("\nAggregated Harvest Results:")
    for crop, total in results.items():
        print(f" • {crop}: {total:.2f} metric tons")
