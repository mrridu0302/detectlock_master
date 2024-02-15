import numpy as np
def bankers_algorithm(available, maximum, allocation, need):
  n_processes, n_resources = allocation.shape
# Initialize work and finish arrays
work = np.copy(available)
finish = np.zeros(n_processes, dtype = bool)
# Initialize safe sequence list
safe_sequence = []
# Loop until all processes are finished or no safe sequence is possible
while np.any(finish == False):
  found = False
for i in range(n_processes):
  if not finish[i] and np.all(need[i,: ] <= work): 
    work += allocation[i,: ]
finish[i] = True safe_sequence.append(i) found = True
if not found: 
  break
if np.all(finish):
  return True, safe_sequence
else:
  return False, safe_sequence
# User input for the number of processes and resources
n_processes = int(input("Enter the number of processes: ")) 
n_resources = int(input("Enter the number of resources: "))
# User input for the available resources
available_resources = np.array(list(map(int, input("Enter the available resources: ").strip().split())))
# User input for the maximum resources
maximum_resources = np.zeros((n_processes, n_resources), dtype = int)
for i in range(n_processes):
  maximum_resources[i] = np.array(list(map(int, input(f "Enter the maximum resources for process {i}: ").strip().split())))
# User input for the allocated resources
allocation = np.zeros((n_processes, n_resources), dtype = int)
for i in range(n_processes):
  allocation[i] = np.array(list(map(int, input(f "Enter the allocated resources for process {i}: ").strip().split())))
# Calculate the need matrix
need = maximum_resources - allocation
# Run the Banker 's algorithm
safe_state, safe_sequence = bankers_algorithm(available_resources, maximum_resources, allocation, need)
# Print the result
if safe_state:
  print("System is in safe state. Safe sequence: ", safe_sequence)
else:
  print("System is in an unsafe state. Deadlock detected.")
