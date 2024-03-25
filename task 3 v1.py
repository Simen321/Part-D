import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Define linguistic variables
mean_delay = ctrl.Antecedent(np.arange(0, 1.01, 0.01), 'mean_delay')
number_of_servers = ctrl.Antecedent(np.arange(0, 1.01, 0.01), 'number_of_servers')
utilisation_factor = ctrl.Antecedent(np.arange(0, 1.01, 0.01), 'utilisation_factor')
number_of_spares = ctrl.Consequent(np.arange(0, 1.01, 0.01), 'number_of_spares')

# Define linguistic values for mean_delay
mean_delay['very_short'] = fuzz.trimf(mean_delay.universe, [0, 0, 0.3])
mean_delay['short'] = fuzz.trimf(mean_delay.universe, [0.1, 0.5, 0.5])
mean_delay['medium'] = fuzz.trimf(mean_delay.universe, [0.4, 0.7, 0.7])

# Define linguistic values for number_of_servers
number_of_servers['small'] = fuzz.trimf(number_of_servers.universe, [0, 0.35, 0.35])
number_of_servers['medium'] = fuzz.trimf(number_of_servers.universe, [0.30, 0.70, 0.70])
number_of_servers['large'] = fuzz.trimf(number_of_servers.universe, [0.60, 1, 1])

# Define linguistic values for utilisation_factor
utilisation_factor['low'] = fuzz.trimf(utilisation_factor.universe, [0, 0.6, 0.6])
utilisation_factor['medium'] = fuzz.trimf(utilisation_factor.universe, [0.4, 0.8, 0.8])
utilisation_factor['high'] = fuzz.trimf(utilisation_factor.universe, [0.6, 1, 1])

# Define linguistic values for number_of_spares
number_of_spares['very_small'] = fuzz.trimf(number_of_spares.universe, [0, 0.30, 0.30])
number_of_spares['small'] = fuzz.trimf(number_of_spares.universe, [0, 0.40, 0.40])
number_of_spares['rather_small'] = fuzz.trimf(number_of_spares.universe, [0.25, 0.45, 0.45])
number_of_spares['medium'] = fuzz.trimf(number_of_spares.universe, [0.30, 0.70, 0.70])
number_of_spares['rather_large'] = fuzz.trimf(number_of_spares.universe, [0.55, 0.75, 0.75])
number_of_spares['large'] = fuzz.trimf(number_of_spares.universe, [0.60, 1, 1])
number_of_spares['very_large'] = fuzz.trimf(number_of_spares.universe, [0.70, 1, 1])

# Define rules based on the extended rule base 3
rule1 = ctrl.Rule(utilisation_factor['low'], number_of_spares['small'])
rule2 = ctrl.Rule(utilisation_factor['medium'], number_of_spares['medium'])
rule3 = ctrl.Rule(utilisation_factor['high'], number_of_spares['large'])

# Create the control system
system = ctrl.ControlSystem([rule1, rule2, rule3])

# Create a simulation
simulation = ctrl.ControlSystemSimulation(system)

# Pass inputs to the system and compute the output
simulation.input['utilisation_factor'] = 0.7  # Example value for utilisation_factor
simulation.compute()

# Print the output
print("Number of spares:", simulation.output['number_of_spares'])

# View the system
number_of_spares.view(sim=simulation)
plt.show()
