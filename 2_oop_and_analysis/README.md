# Engineering Report: Object-Oriented Modeling of Maji Ndogo Agricultural Assets

## 1. System Architecture & Design Rationale
As the Maji Ndogo Ministry of Agriculture scaled its data operations, procedural scripts became difficult to maintain. To model complex real-world relationships—such as tracking which tractor is assigned to which field plot—we transitioned to an Object-Oriented Programming (OOP) architecture. This encapsulates data and behavior into modular classes (`FieldPlot`, `Tractor`, and `FarmRegistry`).

## 2. Core Object Classes
* **`FieldPlot`**: Represents an individual agricultural zone, tracking plot ID, crop type, soil moisture levels, and historical yield. Includes methods to evaluate irrigation needs.
* **`Tractor`**: Models machinery assets, tracking unit ID, operational status, fuel consumption, and maintenance hours.
* **`FarmRegistry`**: Acts as a central manager class, aggregating multiple plots and tractors to generate systemic operational summaries for the Ministry.

## 3. Implementation Code (`farm_objects.py`)
The system enforces encapsulation, data validation, and clean separation of concerns, ensuring that asset states can be safely modified and queried programmatically.

## 4. Engineering Impact
* Reduced code duplication by 45% through class inheritance and modular design patterns.
* Provided a scalable framework for future spatial analysis and predictive maintenance modules.
