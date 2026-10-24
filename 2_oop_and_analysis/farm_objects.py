"""
Maji Ndogo Ministry of Agriculture
Module 2: OOP & Analysis - Agricultural Asset Modeling
"""

class FieldPlot:
    def __init__(self, plot_id: str, crop_type: str, area_hectares: float, soil_moisture: float):
        self.plot_id = plot_id
        self.crop_type = crop_type
        self.area_hectares = area_hectares
        self.soil_moisture = soil_moisture  # Percentage (0-100)

    def assess_irrigation_needs(self) -> str:
        """Determines if the plot requires immediate irrigation."""
        if self.soil_moisture < 30.0:
            return "CRITICAL: Immediate irrigation required."
        elif self.soil_moisture < 50.0:
            return "WARNING: Moderate moisture levels. Monitor closely."
        return "OPTIMAL: Sufficient soil moisture."

    def __str__(self):
        return f"Plot {self.plot_id} ({self.crop_type}): {self.area_hectares} ha, {self.soil_moisture}% moisture"


class Tractor:
    def __init__(self, tractor_id: str, model: str, fuel_level_pct: float):
        self.tractor_id = tractor_id
        self.model = model
        self.fuel_level_pct = fuel_level_pct
        self.is_active = True

    def operate(self, hours: int):
        """Simulates tractor operation and fuel consumption."""
        fuel_consumed = hours * 4.5  # Assume 4.5% fuel usage per hour
        self.fuel_level_pct = max(0.0, self.fuel_level_pct - fuel_consumed)
        if self.fuel_level_pct == 0:
            self.is_active = False
        return f"Tractor {self.tractor_id} operated for {hours}h. Remaining fuel: {self.fuel_level_pct}%"

    def __str__(self):
        status = "Active" if self.is_active else "Out of Fuel / Inactive"
        return f"Tractor {self.tractor_id} [{self.model}] - Status: {status} ({self.fuel_level_pct}% fuel)"


class FarmRegistry:
    def __init__(self, region_name: str):
        self.region_name = region_name
        self.plots = []
        self.tractors = []

    def add_plot(self, plot: FieldPlot):
        self.plots.append(plot)

    def add_tractor(self, tractor: Tractor):
        self.tractors.append(tractor)

    def generate_regional_summary(self):
        print(f"\n--- Regional Status Report: {self.region_name} ---")
        print(f"Total Managed Plots: {len(self.plots)}")
        print(f"Total Fleet Tractors: {len(self.tractors)}")
        
        print("\nPlot Irrigation Audit:")
        for plot in self.plots:
            print(f" • {plot.plot_id}: {plot.assess_irrigation_needs()}")


if __name__ == "__main__":
    # Initialize Registry
    maji_registry = FarmRegistry("Maji Ndogo Central District")

    # Add Field Plots
    maji_registry.add_plot(FieldPlot("P-101", "Maize", 15.5, 24.5))
    maji_registry.add_plot(FieldPlot("P-102", "Sorghum", 22.0, 55.0))
    
    # Add Tractors
    maji_registry.add_tractor(Tractor("T-01", "John Deere 5075E", 85.0))
    maji_registry.add_tractor(Tractor("T-02", "New Holland T4", 15.0))

    # Run Summary Audit
    maji_registry.generate_regional_summary()
