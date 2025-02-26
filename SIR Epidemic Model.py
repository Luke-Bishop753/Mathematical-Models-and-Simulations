#imports
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

#-----------------------------------------------------------------------------
#beta = infection rate
#gamma = recovery rate
#s = susceptible population, i = infected population, r = recovered population
#v = vaccination rate. No loss of immunity is assumed.
#w = "waning immunity" factor, the rate of which a recovered individual loses
#their immunity, and thus moves back into the susceptible population.
#d = death rate, as a fraction of the infected population die each time step.
#q = quarantine rate
#-----------------------------------------------------------------------------

#beta(t) allows beta, the infection rate parameter, to oscillate periodically,
#to simulate seasonal changes in the disease behaviour.
def beta(t):
    base_beta = 1.0
    beta_amplitude = 0.5
    period = 365
    beta = base_beta * (1 + (beta_amplitude * math.sin(((2*math.pi) / period) * t)))
    return beta

#similar for the recovery rate, gamma.
def gamma(t):
    base_gamma = 0.05
    gamma_amplitude = 0.02
    period = 365
    gamma = base_gamma * (1 + (gamma_amplitude * math.sin(((2*math.pi) / period) * t)))
    return gamma
v = 0.05
w = 1 / 365
d = 0.05
q = 0.5
def system(t, y):
    s, i, r, Q = y
    ds_dt = (-beta(t) * s * i) - (v * s) + (w * r)
    di_dt = (beta(t) * s * i) - (gamma(t) * i) - (d * i) - (q * i)
    dr_dt = (gamma(t) * i) + (v * s) - (w * r)
    dq_dt = (q * i) - (gamma(t) * Q) - (d * Q)
    return [ds_dt, di_dt, dr_dt, dq_dt]

#solve the system of equations
t_eval = np.linspace(0, 365, 5000)
solutions = solve_ivp(system, (0, 365), [0.99, 0.01, 0, 0.001], t_eval=t_eval)

#plot the results
plt.plot(solutions.t, solutions.y[0], label="susceptible")
plt.plot(solutions.t, solutions.y[1], label="infected")
plt.plot(solutions.t, solutions.y[2], label="recovered")
plt.plot(solutions.t, solutions.y[3], label="Quarantined")
plt.xlabel("Time")
plt.ylabel("Populations")
plt.title("SIR Model Projection")
plt.legend()
plt.show()

#plot s v i -> susceptible population against infected population
plt.figure()
plt.plot(solutions.y[0], solutions.y[1])
plt.xlabel("Susceptible")
plt.ylabel("Infected")
plt.title("Phase Space - Susceptible against Infected")
plt.show()