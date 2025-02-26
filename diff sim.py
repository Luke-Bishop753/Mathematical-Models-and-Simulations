#imports
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

#defining a function "equation", which models logistic growth. Takes in time, t,
#population, p, with a rate of change r. Then it returns the derivative of p with respect to t, accounting for the
#carrying capacity, k, that limits the growth.
def equation (t, p):
    r = 0.2
    k = 4000
    dp_dt = (r * p) * (1 - (p / k))
    return dp_dt

#solve the differential equation. Takes the arguments "equation" (dp_dt), a time range and the initial population as a
#one-dimensional array, accounting for the possibility of multiple equations needed to be solved using solve_ivp.
solution = solve_ivp(equation, (0, 100), [200])

#plot and show how the population evolves over time
plt.plot(solution.t, solution.y[0])
plt.xlabel("Time")
plt.ylabel("Population")
plt.title("Logistic Growth")
plt.show()
