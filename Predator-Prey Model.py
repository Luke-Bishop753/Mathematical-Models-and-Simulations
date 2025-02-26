#imports
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np
#defining the equations, where p is the population of the prey, and q is the population of the predators.
#solve_ivp requires a function that takes t (time), and a list y, containing all of the dependent variables
#(p and q, predator and prey populations).
#The function then returns the derivatives of p and q with respect to time.
#Gamma is made positive, ensuring that the number of predators declines as the prey population drops, instead of growing
#indefinitely.
def equations(t, y):
    alpha = 1.0   #prey growth rate
    beta = 0.01   #predation rate
    gamma = 1.0   #predator death rate
    delta = 0.02  #predator growth rate

    p, q = y
    dp_dt = (alpha * p) - (beta * p * q)
    dq_dt = (delta * p * q) - (gamma * q)
    print(dp_dt, dq_dt)
    return [dp_dt, dq_dt]

#generate 1000 points, evenly spaced between 0 and 100, to ensure smoothness of the curves when plotted.
t_eval = np.linspace(0, 100, 1000)
#Using solve_ivp to solve for p and q.
solutions = solve_ivp(equations, (0, 100), [50, 2], t_eval=t_eval, method="LSODA")


#plotting the results. Predators and Prey plotted on the same axis.
#Legend added

plt.plot(solutions.t, solutions.y[0], label="Prey")
plt.plot(solutions.t, solutions.y[1], label="Predators")
plt.xlabel("Time")
plt.ylabel("Population")
plt.title("Lotka-Volterra Simulation")
plt.legend()
plt.show()