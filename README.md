# detectlock_master
By incorporating state-of-the-art detection algorithms, real-time monitoring, and insightful visualizations, the project empowers administrators and developers to proactively manage deadlocks that can paralyse computer systems.


The core algorithm employed in this application for deadlock detection is the Banker's Algorithm. It is used to determine whether the system is in a safe state or if a potential deadlock exists. The algorithm considers the allocation matrix, max demand matrix, and available resources to assess system safety.

Input: The application takes the following inputs:
- Number of processes: The user specifies the total number of processes in the
system.
- Number of resource types: The user specifies the number of resource types in
the system.
- Allocation Matrix: The user enters the allocation matrix, where rows represent
processes, and columns represent resource types. These values indicate the
resources currently allocated to each process.
- Max Demand Matrix: The user enters the max demand matrix, similar in
structure to the allocation matrix. It represents the maximum resources each
process may request.
- Available Resources: The user specifies the available resources for each resource
type.

Output:
The application provides the following output:
- Deadlock Detection Result: After processing the input data using the Banker's
Algorithm, the application displays the result, indicating whether a deadlock is detected or not. It shows "No deadlock detected" if the system is in a safe state and "Deadlock detected" if a potential deadlock exists.


The core programming language used to develop the Deadlock Detection App.
