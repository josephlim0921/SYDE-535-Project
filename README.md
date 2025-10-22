# Air Track Aviation Modelling

<p align="center">
  <img src="https://github.com/josephlim0921/SYDE-535-Project/blob/main/images/logo.png" alt="logo"/>
</p>


Using agent-based simulation, we model airline delay at Canada's three busiest airports (Montreal [YUL], Toronto [YYZ] and Vancouver[YVR). We examine the impacts of delay arising from 5 major sources:
**Weather, Maintenance, Ground procedures, Congestion,** and **Cascading delays**. Our metric for quantifying delay was the Cumulative Passenger-delay minutes across the 3 major airports, representing the Cumulative time lost for passengers due to the delays. We have two main types of agents, the airport agent and the airplane agent, each of which has specfic attributes and behaviours. For example, airplace agents record **attributes** such as status, origin, destination, and **behaviours** such as identifying maintanance, "circling" at airport and simulated flight times. 



 We look at 3 main scenarios and 6 ablations for the project: 
 
* The **1. Baseline scenario**, which simulates current procedures.
* **2. Operation Management Scenarios**: which simulate scenarios which improve airport organization and  do not involve infrastructure investment.
    * **2.1 Implementing traffic management forecasting**: This helps forecast future demand in advance to plan staffing and equipment needs. 
    * **2.2 Ground Delay Program**: grounds planes at an origin airport when an adverse event occurs.
*  **3. Capital Investment Scenarios**: which simulate scenarios where high levels ofinfrastructure investment/ugrades occur.
    * **3.1 Increasing bridging (gate) capacity at the airport**, this helps to incrase overall airport capacity.
    * **3.2 Expanding the runways and number of control operators**, this is another way to uncrease airport capacity.
    * **3.3 Improving build quality of aircraft** : a hyptheical scenario where the reliability of planes improves, resulting in fewer maintanance needs.
           

# Images

## Modelling Workflow
![workflow](https://github.com/josephlim0921/SYDE-535-Project/blob/main/images/workflow.png  "workflow")

## Example Cumulative Delay Plot when a Ground Delay Program is Implemented
![ground_delay_sample](https://github.com/josephlim0921/SYDE-535-Project/blob/main/images/ground_delay_sample.png "ground delay sample")


# Project Files


  *  **scenario_1,scenario_2,scenario_3,scenario_4,scenario_6** : Cumulative delay at each airport for each scenario respectively.
  *  **milestone2_simulation_results, milestone2_simulation_results_scenario1** : Preliminary results, please ignore.

  
  *  **final_presentation.pdf** : 15 minute presentation summarizing our main findings.
  *  **final_report.pdf** : 31 page report summarizing simiulation conceptualization, and our findings. 
  *  **images** :Sample images for illustration.


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


