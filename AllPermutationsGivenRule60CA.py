#This code allows you to check all permutations of a given L and fixed occupation number

import numpy as np
from sympy.utilities.iterables import multiset_permutations

L = 5 #Total number of sites
occupation = 4 #total number of intially occupied sites

steps = 20 #total number of steps/ iterations you want to preform on each state.

state = np.concatenate((np.ones(occupation, dtype=int),np.zeros(L-occupation, dtype=int))) #creates an array with the correct number of sites, all unoccupied

state_perms= [] #initialize an empty list to hold all permutations

for p in multiset_permutations(state):
  state_perms.append(p) #generates and stores all possible permutations of your input state

iter = 0 #initializes a counter to keep track of completion

evolution = np.empty(shape=(len(state_perms),steps,L), dtype=int) #initializes an array to hold the evolution of the system

neighbor = np.empty(L, dtype=int) #initializes an array to hold neighbors

for i in range(len(state_perms)):
  initial_state = state_perms[i] #selects a permutation from the list, assigns one array to hold it for checking, and manipulates the other array as the input state
  state = state_perms[i]

  for k in range(steps):
    evolution[i][k] =state #writes each state to the evolution array as above
    for j in range(L-1):
      neighbor[j] = state[j+1]
      neighbor[-1] = state[0] #see comments in code cell above, this block is the same
      newstate = np.bitwise_xor(neighbor, state)
    state=newstate
    if np.array_equal(initial_state,state)== True:
      iter+=1 #counts number of permutations that return to their initial state
      if k+1 != 15: #set a threshold for the period you're interested in to filter interesting initial states and get the index number where they are stored
        print('Permutation',i,'returns to initial state after',k+1,'steps')
        iter-=1 #removes the printed permutation from the final count output
      break

print(iter,'Permutations return to the initial state in',steps-1,'steps')

#you can print permutations of interest using print(state_perms[j]) where j is the index number of the permutation (which will be printed here if the period is less than the step value you've chosen)
#you can see the full evolution of the state using print(evolution[j][0:k] where j is the index number of the permutation, and k is the total number of steps it takes
