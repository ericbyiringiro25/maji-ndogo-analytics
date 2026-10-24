"""
Maji Ndogo Ministry of Agriculture & Water
Module 2: Object-Oriented System for Farm Fleet & Yield Management

This module models physical agricultural assets (tractors, fields) 
and administrative systems (farm registries) as robust Python objects.
"""

from typing import List, Tuple, Dict, Optional


class FieldPlot:
    """Represents an individual agricultural field plot."""

    def __init__(self, plot_id: str, area_hectares: float, crop_type: str):
        self.plot_id = plot_id
        self.area_hectares = area_hectares
        self.crop_type = crop_type
        self.harvest_records: List[float] = []  # Yield in metric tons

    def add_harvest(self, yield_tons: float) -> None:
        """Record a harvest yield for this plot."""
        if yield_tons < 0:
            raise ValueError("Harvest yield cannot be negative.")
        self.harvest_records.append(yield_tons)

    def total_yield(self) -> float:
        """Calculate total yield produced across all recorded harvests."""
        return sum(self.harvest_records)

    def average_yield_per_hectare(self) -> float:
        """Calculate average yield per hectare."""
        if self.area_hectares <= 0:
            return 0.0
        return self.total_yield() / self.area_hectares

    def __repr__(self) -> str:
        return f"FieldPlot(id='{self.plot_id}', crop='{self.crop_type}', area={self.area_hectares}ha)"


class Tractor:
    """Models a field tractor, tracking position, fuel state, and operation log."""

    def __init__(self, tractor_id: str, fuel_capacity_liters: float, fuel_consumption_per_km: float = 1.5):
        self.tractor_id = tractor_id
        self.fuel_capacity = fuel_capacity_liters
        self.current_fuel = fuel_capacity_liters
        self.position: Tuple[int, int] = (0, 0)
        self.fuel_consumption_rate = fuel_consumption_per_km
        self.maintenance_needed: bool = False

    def drive_to(self, target_coords: Tuple[int, int]) -> bool:
        """
        Calculates Manhattan distance to target coordinates, verifies fuel capacity,
        and updates position and fuel levels.
        """
        dx = abs(target_coords[0] - self.position[0])
        dy = abs(target_coords[1] - self.position[1])
        distance_km = dx + dy

        required_fuel = distance_km * self.fuel_consumption_rate

        if required_fuel > self.current_fuel:
            print(f"⚠️ [Tractor {self.tractor_id}] Insufficient fuel to reach {target_coords}. Needed: {required_fuel:.1f}L, Available: {self.current_fuel:.1f}L.")
            return False

        self.current_fuel -= required_fuel
        self.position = target_coords
        print(f"🚜 [Tractor {self.tractor_id}] Moved to {target_coords}. Fuel used: {required_fuel:.1f}L | Fuel remaining: {self.current_fuel:.1f}L.")

        if self.current_fuel < (self.fuel_capacity * 0.15):
            self.maintenance_needed = True
            print(f"⛽ [ALERT] Tractor {self.tractor_id} fuel low (<15%). Refuel required.")

        return True

    def refuel(self, liters: Optional[float] = None) -> None:
        """Refuels the tractor up to capacity."""
        if liters is None or (self.current_fuel + liters) > self.fuel_capacity:
            self.current_fuel = self.fuel_capacity
        else:
            self.current_fuel += liters
        self.maintenance_needed = False
        print(f"⛽ [Tractor {self.tractor_id}] Refueling complete. Current fuel: {self.current_fuel:.1f}L.")

    def __repr__(self) -> str:
        return f"Tractor(id='{self.tractor_id}', pos={self.position}, fuel={self.current_fuel:.1f}/{self.fuel_capacity}L)"


class FarmRegistry:
    """Central registry class to manage regional plots and tractor fleets."""

    def __init__(self, region_name: str):
        self.region_name = region_name
        self.plots: Dict[str, FieldPlot] = {}
        self.fleet: Dict[str, Tractor] = {}

    def register_plot(self, plot: FieldPlot) -> None:
        """Registers a new field plot."""
        self.plots[plot.plot_id] = plot

    def register_tractor(self, tractor: Tractor) -> None:
        """Registers a new tractor in the fleet."""
        self.fleet[tractor.tractor_id] = tractor

    def generate_regional_summary(self) -> Dict[str, float]:
        """Generates aggregate yield metrics across all registered plots."""
        total_regional_yield = sum(p.total_yield() for p in self.plots.values())
        total_regional_area = sum(p.area_hectares for p in self.plots.values())

        return {
            "total_plots": len(self.plots),
            "total_fleet_size": len(self.fleet),
            "total_area_hectares": total_regional_area,
            "total_yield_tons": total_regional_yield,
            "regional_avg_yield_per_ha": (total_regional_yield / total_regional_area) if total_regional_area > 0 else 0.0
        }


# --- Execution Pipeline & Testing ---
if __name__ == "__main__":
    print("==================================================")
    print("  MAJI NDOGO MINISTRY OF AGRICULTURE - REGIONAL OOP SYSTEM  ")
    print("==================================================\n")

    # 1. Initialize Regional Registry
    registry = FarmRegistry("Maji Ndogo North")

    # 2. Add Field Plots
    p1 = FieldPlot(plot_id="PLOT-101", area_hectares=12.5, crop_type="Maize")
    p2 = FieldPlot(plot_id="PLOT-102", area_hectares=8.0, crop_type="Sorghum")

    p1.add_harvest(45.2)
    p1.add_harvest(50.1)
    p2.add_harvest(28.4)

    registry.register_plot(p1)
    registry.register_plot(p2)

    # 3. Add Tractors
    t1 = Tractor(tractor_id="TRAC-01", fuel_capacity_liters=100.0)
    registry.register_tractor(t1)

    # 4. Simulate Operations
    print("--- Tractor Movement Simulation ---")
    t1.drive_to((10, 15))
    t1.drive_to((30, 40))  # Long distance run to test low-fuel alert
    t1.refuel()

    print("\n--- Regional Summary Report ---")
    summary = registry.generate_regional_summary()
    for key, value in summary.items():
        print(f" • {key.replace('_', ' ').title()}: {value:.2f}" if isinstance(value, float) else f" • {key.replace('_', ' ').title()}: {value}")
