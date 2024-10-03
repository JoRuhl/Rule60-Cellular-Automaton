#This code generates a random state with even occupation for a given L
#and prints the time evolution for the Rule 60 cellular automaton on a ring.
#It then animates the result

import numpy as np

L = 5 #number of sites on the ring. 
steps = 16 #total number of steps you want calculated

state = np.zeros(L, dtype=int) #initializes a vector of zeros at the desired length
evolution = np.empty([steps,L], dtype=int) #initializes an array to hold the evolution of the system

initial_occupation = np.random.randint(0,L+1) #generates a random number of occupied sites

while initial_occupation%2 !=0 or initial_occupation ==0:
  initial_occupation = np.random.randint(0,L+1) #ensures number of occupied sites is even but not the trivial solution

sites = np.random.randint(0,L, size=initial_occupation) #randomly determine occupied sites

while len(np.unique(sites)) < len(sites): #make sure occupied sites are unique so occupation stays even
  m =len(sites) - len(np.unique(sites))
  allsites = np.unique(sites)
  sites = np.append(allsites, np.random.randint(0,L, size=m))

for i in range(len(sites)):
  state[sites[i]] =1 #set occupied sites to 1

neighbor = np.empty(L, dtype=int)#this initializes an empty vector to hold the starting state shifted by one site to make neighbor xor computationally easier
initial_state = state #this stores a copy of the initial state for comparison as the system evolves

print('starting state',state)
for k in range(steps):
  evolution[k] =state #writes the current state to a row in the initialized evolution array
  for j in range(L-1):
    neighbor[j] = state[j+1]
    neighbor[-1] = state[0]
    newstate = np.bitwise_xor(neighbor, state) #computes the new state by preforming xor on neighboring pairs
  state=newstate  #updates the current state to the newly calculated evolution
  if np.array_equal(initial_state,state)== True: #checks to see if the new state evolution is the same as the initial state
    print('Returns to initial state after',k+1,'steps') #Python indexing begins at 0, so k+1 gives the natural counting number of steps

print(evolution)

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import colors

fig = plt.figure()
ax = fig.add_subplot(projection='polar') #sets visualization parameters
ax.set_ylim(0,0.55)
ax.set_yticklabels([])
ax.set_xticklabels([])

cmap = colors.ListedColormap(['white','purple']) #set colors for unoccupied, occupied sites
bounds = [-0.5,0.5,1.5] #defines color map
norm = colors.BoundaryNorm(bounds, cmap.N)

colorings = np.empty(L,dtype=int)

def animate(i): #define the animate function, define what is plotted at each step
  for j in range(L):
    colorings[j] = evolution[i][j] 
  return ax.scatter(2*np.pi/L*np.arange(L), 0.5*np.ones(L), s=100,marker = '^',c=colorings,cmap=cmap, norm=norm,edgecolors='black')

#create and display the animation

anim = animation.FuncAnimation(fig, animate, frames= steps, interval=1000, repeat = False)
from IPython.display import HTML
HTML(anim.to_jshtml())
plt.show()
