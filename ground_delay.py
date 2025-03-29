import pandas as pd
import numpy as np

def ground_service():
  num_tasks = 4
  data = {
      "task_name": ["Deboarding", "Cabin cleaning", "Catering","Boarding"],
      "task_length": [10, 10,20,21],  # In minutes
      "buffer_before": np.random.randint(0, 4, num_tasks),  # Random between 0 and 3
      "buffer_after": np.random.randint(0, 4, num_tasks),
      "next_task_starting_time": [13, 10, 0,10],  # Example starting times
  }

  # data = {
  #     "task_name": ["Deboarding", "Cabin cleaning", "Catering","Boarding"],
  #     "task_length": [10, 10,20,21],  # In minutes
  #     "buffer_before": [0,0,0,0],  # Random between 0 and 3
  #     "buffer_after": [0,0,0,0],
  #     "next_task_starting_time": [13, 10, 0,10],  # Example starting times
  # }

  #https://www.researchgate.net/figure/Turnaround-Gantt-chart-for-a-typical-single-aisle-aircraft-Source-inspired-and-adapted_fig3_367317346
  #https://www.researchgate.net/publication/367317346_Reduction_in_Ground_Times_in_Passenger_Air_Transport_A_First_Approach_to_Evaluate_Mechanisms_and_Challenges
  df = pd.DataFrame(data)

  # Calculate task process times
  df["total_time"] = (
      df["task_length"] + df["buffer_before"] + df["buffer_after"]
  )

  #______
  # Initialize a list to store absolute starting times
  absolute_starting_times = [0]  # First task always starts at 0

  # Calculate the absolute starting time for each task
  for i in range(1, len(df)):
      absolute_starting_times.append(
          absolute_starting_times[i - 1] + df["next_task_starting_time"].iloc[i]
      )

  # Add the calculated values as a new column
  df["absolute_task_starting_time"] = absolute_starting_times

  # Print the updated DataFrame
  # print(df)
  #________

  # Calculate the total length of the process
  total_process_length = df["absolute_task_starting_time"].iloc[-1] + df["total_time"].iloc[-1]

  # Display results
  # print("DataFrame")
  # print(df)
  # print(f"\n Total process length: {total_process_length} minutes")

  net_delay = total_process_length-41
  return net_delay