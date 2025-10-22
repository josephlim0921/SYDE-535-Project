# Air Track Aviation Modelling

<p align="center">
  <img src="https://github.com/josephlim0921/SYDE-535-Project/blob/main/images/logo.png" alt="logo"/>
</p>


Using agent-based simulation, we model airline delay at Canada's three busiest airports (Montreal [YUL], Toronto [YYZ] and Vancouver[YVR). We examine the impacts of delay arising from 4 major sources
 Weather, Maintenance, Ground procedures, Congestion, and cascading delays. Our metric for quantifying delay was Cumulative Passenger-delay minutes across the 3 major airports, representing the Cumulative time lost due to the delays. We have two main agents, the airport agent and the airplane agent, each with specfic attributes and behaviours. For example, airplace agents record attributes such as  status, origin, destination, and behaviours such as identifying maintanance, "circle" at airport and simulation flight times. 


 We look at 3 main scenarios and 5 ablations for the project: 
     1. **Baseline scenario**, which simulated current procedures
     2. **Operation Management Scenarios** : 
         2.1    **Implementing Traffic management forecasting**:
         2.2     **Ground Delay Program**:
     3.  **Capital Investment Scenarios**:
         * **Increasing bridging (gate) capacity at the airport**
         * **Expanding the runways and number of control operators**
         * **Improving build quality of aircraft** : 

# Images

## Modelling Workflow
![workflow](https://github.com/josephlim0921/SYDE-535-Project/blob/main/images/workflow.png  "workflow")

## Example Cumulative Delay Plot when a Ground Delay Program is Implemented
![ground_delay_sample](https://github.com/josephlim0921/SYDE-535-Project/blob/main/images/ground_delay_sample.png "ground delay sample")


# files
### flight_times.csv
Flight times between various destinations

### ground_delay.py
Code for delay caused by ground services

### max_capabilities.py
Capacities of airline flights and percentage of each aircraft

### max_capacity - YUL_capacity.csv
Hourly passenger variation for YUL airport

### max_capacity - YVR_capacity.csv
Hourly passenger variation for YVR airport

### max_capacity - YYZ_capacity.csv
Hourly passenger variation for YYZ airport

### simulation_final_fixed.ipynb
Main code with classes for airplane and airport agents and to run the realizations

### weather_delay.py
Code for delay caused by weather types


