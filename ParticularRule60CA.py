#This code allows you to investigate the evolution of a particular initial state of interest
#under the Rule 60 time evolution rule. It will terminate after the first smallest fundamental
#period is completed.

import numpy as np

state = np.array([0, 1, 1, 1, 1], dtype=int) #enter your desired initial state in 1-s (occupied site) and 0-s (unoccupied site) between the []. Separate each term by commas
steps = 65  #enter an integer value for the maximum number of steps you would like to calculate

evolution = np.empty([steps,len(state)], dtype=int) #initializes an array to hold the evolution of the system, which will be printed at the end

neighbor = np.empty(len(state), dtype=int) #this initializes an empty vector to hold the starting state shifted by one site to make neighbor xor computationally easier
initial_state = state #this stores a copy of the initial state for comparison as the system evolves

for k in range(steps):
  evolution[k] =state #writes the current state to a row in the initialized evolution array
  for j in range(len(state)-1):
    neighbor[j] = state[j+1] #this loop populates the neighbor vector with the current state shifted by one index
    neighbor[-1] = state[0]
    newstate = np.bitwise_xor(neighbor, state) #computes the new state by preforming xor on neighboring pairs
  state=newstate #updates the current state to the newly calculated evolution
  if np.array_equal(initial_state,state)== True: #checks to see if the new state evolution is the same as the initial state
    print('Returns to initial state after',k+1,'steps') #Python indexing begins at 0, so k+1 gives the natural counting number of steps
    break 

print(evolution[:k]) #displays the full evolution array showing the state at each step.

#You can later print a specific step from the evolution using print(evolution[j]) where j is replaced by the integer index of the state you want
#When viewing the evolution printout, the 0th step (initial state) is at the top, and the index increments by +1 each row.
