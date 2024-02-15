import tkinter as tk
from tkinter
import messagebox
import numpy as np
from bankers
import bankers_algorithm
def bankers_algorithm(available, maximum, allocation, need): 
  n_processes, n_resources = allocation.shape
work = np.copy(available)
finish = np.zeros(n_processes, dtype = bool)
safe_sequence = []
while np.any(finish == False):
  found = False
for i in range(n_processes):
  if not finish[i] and np.all(need[i,: ] <= work): 
    work += allocation[i,: ]
finish[i] = True safe_sequence.append(i) 
found = True
if not found: 
  break
if np.all(finish):
  return True, safe_sequence
else:
  return False, safe_sequence
def run_bankers_algorithm():
  try:
available_resources = np.array(list(map(int, available_entry.get().strip().split()))) 
n_processes = int(processes_entry.get())
n_resources = int(resources_entry.get())
maximum_resources = np.zeros((n_processes, n_resources), dtype = int) 
allocation = np.zeros((n_processes, n_resources), dtype = int)
for i in range(n_processes):
  maximum_resources[i] = np.array(list(map(int, maximum_entries[i].get().strip().split())))
allocation[i] = np.array(list(map(int, allocation_entries[i].get().strip().split())))
need = maximum_resources - allocation
safe_state, safe_sequence = bankers_algorithm(available_resources, maximum_resources, allocation, need)
if safe_state:
  messagebox.showinfo("Result", f "System is in safe state. Safe sequence: {safe_sequence}")
else:
  messagebox.showerror("Result", "System is in an unsafe state. Deadlock detected.")
except ValueError:
  messagebox.showerror("Error", "Please enter valid input.")
root = tk.Tk() root.title("Banker's Algorithm")
top_frame = tk.Frame(root) top_frame.pack(pady = 10)
available_label = tk.Label(top_frame, text = "Available Resources:") available_label.grid(row = 0, column = 0, padx = 5, pady = 5) available_entry = tk.Entry(top_frame)
available_entry.grid(row = 0, column = 1, padx = 5, pady = 5)
processes_label = tk.Label(top_frame, text = "Number of Processes:") processes_label.grid(row = 1, column = 0, padx = 5, pady = 5) processes_entry = tk.Entry(top_frame)
processes_entry.grid(row = 1, column = 1, padx = 5, pady = 5)
resources_label = tk.Label(top_frame, text = "Number of Resources:") resources_label.grid(row = 2, column = 0, padx = 5, pady = 5) resources_entry = tk.Entry(top_frame)
resources_entry.grid(row = 2, column = 1, padx = 5, pady = 5)
maximum_labels = [] maximum_entries = []

allocation_labels = [] allocation_entries = []
middle_frame = tk.Frame(root) middle_frame.pack(pady = 10)
def on_process_change( * args):
  try:
  n = int(processes_entry.get())
for i in range(len(maximum_labels)): 
  maximum_labels[i].grid_forget() 
  maximum_entries[i].grid_forget() 
  allocation_labels[i].grid_forget() 
  allocation_entries[i].grid_forget() 
  maximum_labels.clear() 
  maximum_entries.clear()
  allocation_labels.clear() 
  allocation_entries.clear()
for i in range(n):
  label = tk.Label(middle_frame, text = f "Maximum Resources for Process {i}:") 
  label.grid(row = i, column = 0, padx = 5, pady = 5)
maximum_labels.append(label)
entry = tk.Entry(middle_frame) 
entry.grid(row = i, column = 1, padx = 5, pady = 5) 
maximum_entries.append(entry)
label = tk.Label(middle_frame, text = f "Allocation for Process {i}:") 
label.grid(row = i, column = 2, padx = 5, pady = 5) 
allocation_labels.append(label)
entry = tk.Entry(middle_frame) 
entry.grid(row = i, column = 3, padx = 5, pady = 5) 
allocation_entries.append(entry)
except ValueError:
  pass
processes_entry.bind("<FocusOut>", on_process_change) 
bottom_frame = tk.Frame(root)
bottom_frame.pack(pady = 10)
run_button = tk.Button(bottom_frame, text = "Run Banker's Algorithm", command = run_bankers_algorithm)
run_button.pack()
root.mainloop()
