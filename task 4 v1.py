import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Define input variables
temp = ctrl.Antecedent(np.arange(-20, 21, 1), 'temp')
flow = ctrl.Antecedent(np.arange(-1, 1.01, 0.01), 'flow')

# Define output variables
cold = ctrl.Consequent(np.arange(-1, 1.01, 0.01), 'cold')
hot = ctrl.Consequent(np.arange(-1, 1.01, 0.01), 'hot')

# Define membership functions for inputs and outputs
temp['cold'] = fuzz.trapmf(temp.universe, [-30, -30, -15, 0])
temp['good'] = fuzz.trimf(temp.universe, [-10, 0, 10])
temp['hot'] = fuzz.trapmf(temp.universe, [0, 15, 30, 30])

flow['soft'] = fuzz.trapmf(flow.universe, [-3, -3, -0.8, 0])
flow['good'] = fuzz.trimf(flow.universe, [-0.4, 0, 0.4])
flow['hard'] = fuzz.trapmf(flow.universe, [0, 0.8, 3, 3])

cold['closeFast'] = fuzz.trimf(cold.universe, [-1, -0.6, -0.3])
cold['closeSlow'] = fuzz.trimf(cold.universe, [-0.6, -0.3, 0])
cold['steady'] = fuzz.trimf(cold.universe, [-0.3, 0, 0.3])
cold['openSlow'] = fuzz.trimf(cold.universe, [0, 0.3, 0.6])
cold['openFast'] = fuzz.trimf(cold.universe, [0.3, 0.6, 1])

hot['closeFast'] = fuzz.trimf(hot.universe, [-1, -0.6, -0.3])
hot['closeSlow'] = fuzz.trimf(hot.universe, [-0.6, -0.3, 0])
hot['steady'] = fuzz.trimf(hot.universe, [-0.3, 0, 0.3])
hot['openSlow'] = fuzz.trimf(hot.universe, [0, 0.3, 0.6])
hot['openFast'] = fuzz.trimf(hot.universe, [0.3, 0.6, 1])

# Plot membership functions
fig, axs = plt.subplots(2, 2, figsize=(12, 12))

axs[0, 0].plot(temp.universe, fuzz.trapmf(temp.universe, [-30, -30, -15, 0]), label='cold')
axs[0, 0].plot(temp.universe, fuzz.trimf(temp.universe, [-10, 0, 10]), label='good')
axs[0, 0].plot(temp.universe, fuzz.trapmf(temp.universe, [0, 15, 30, 30]), label='hot')
axs[0, 0].set_title('Temperature Membership Functions')
axs[0, 0].legend()

axs[0, 1].plot(flow.universe, fuzz.trapmf(flow.universe, [-3, -3, -0.8, 0]), label='soft')
axs[0, 1].plot(flow.universe, fuzz.trimf(flow.universe, [-0.4, 0, 0.4]), label='good')
axs[0, 1].plot(flow.universe, fuzz.trapmf(flow.universe, [0, 0.8, 3, 3]), label='hard')
axs[0, 1].set_title('Flow Membership Functions')
axs[0, 1].legend()

axs[1, 0].plot(cold.universe, fuzz.trimf(cold.universe, [-1, -0.6, -0.3]), label='closeFast')
axs[1, 0].plot(cold.universe, fuzz.trimf(cold.universe, [-0.6, -0.3, 0]), label='closeSlow')
axs[1, 0].plot(cold.universe, fuzz.trimf(cold.universe, [-0.3, 0, 0.3]), label='steady')
axs[1, 0].plot(cold.universe, fuzz.trimf(cold.universe, [0, 0.3, 0.6]), label='openSlow')
axs[1, 0].plot(cold.universe, fuzz.trimf(cold.universe, [0.3, 0.6, 1]), label='openFast')
axs[1, 0].set_title('Cold Water Valve Membership Functions')
axs[1, 0].legend()

axs[1, 1].plot(hot.universe, fuzz.trimf(hot.universe, [-1, -0.6, -0.3]), label='closeFast')
axs[1, 1].plot(hot.universe, fuzz.trimf(hot.universe, [-0.6, -0.3, 0]), label='closeSlow')
axs[1, 1].plot(hot.universe, fuzz.trimf(hot.universe, [-0.3, 0, 0.3]), label='steady')
axs[1, 1].plot(hot.universe, fuzz.trimf(hot.universe, [0, 0.3, 0.6]), label='openSlow')
axs[1, 1].plot(hot.universe, fuzz.trimf(hot.universe, [0.3, 0.6, 1]), label='openFast')
axs[1, 1].set_title('Hot Water Valve Membership Functions')
axs[1, 1].legend()

plt.tight_layout()
plt.show()
