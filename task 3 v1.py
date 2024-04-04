import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define input and output variables
m = ctrl.Antecedent(np.arange(0, 1.1, 0.01), 'm')
p = ctrl.Antecedent(np.arange(0, 1.1, 0.01), 'p')
s = ctrl.Antecedent(np.arange(0, 1.1, 0.01), 's')

n = ctrl.Consequent(np.arange(0, 1.1, 0.01), 'n')  

# Define membership functions
m['VS'] = fuzz.trapmf(m.universe, [0, 0, 0.15, 0.35])
m['S'] = fuzz.trimf(m.universe, [0.1, 0.3, 0.5])
m['M'] = fuzz.trimf(m.universe, [0.4, 0.55, 0.7])

s['S'] = fuzz.trimf(s.universe, [0, 0, 0.35])
s['RS'] = fuzz.trimf(s.universe, [0.15 , 0.3 , 0.45])
s['M'] = fuzz.trimf(s.universe, [0.30, 0.5, 0.70])
s['L'] = fuzz.trimf(s.universe, [0.60, 0.8, 1])
s['RL'] = fuzz.trimf(s.universe,[0.55 , 0.7 , 0.85])

p['L'] = fuzz.trimf(p.universe, [0, 0, 0.6])
p['M'] = fuzz.trimf(p.universe, [0.4, 0.6, 0.8])
p['H'] = fuzz.trimf(p.universe, [0.6, 0.8, 1])

n['VS'] = fuzz.trimf(n.universe, [0, 0, 0.30])
n['S'] = fuzz.trimf(n.universe, [0, 0.30, 0.40])
n['RS'] = fuzz.trimf(n.universe, [0.25, 0.35, 0.45])
n['M'] = fuzz.trimf(n.universe, [0.30, 0.5, 0.70])
n['RL'] = fuzz.trimf(n.universe, [0.55, 0.65, 0.75])
n['L'] = fuzz.trimf(n.universe, [0.60, 0.80, 1])
n['VL'] = fuzz.trimf(n.universe, [0.70, 0.85, 1])

# Define rules
rules3 = [
    ctrl.Rule((m['VS'] & s['S'] & p['L']), n['VS']),
    ctrl.Rule((m['S'] & s['S'] & p['L']), n['VS']),
    ctrl.Rule((m['M'] & s['S'] & p['L']), n['VS']),
    ctrl.Rule((m['VS'] & s['RS'] & p['L']), n['VS']),
    ctrl.Rule((m['S'] & s['RS'] & p['L']), n['VS']),
    ctrl.Rule((m['M'] & s['RS'] & p['L']), n['VS']),
    ctrl.Rule((m['VS'] & s['M'] & p['L']), n['VS']),
    ctrl.Rule((m['S'] & s['M'] & p['L']), n['VS']),
    ctrl.Rule((m['M'] & s['M'] & p['L']), n['VS']),
    ctrl.Rule((m['VS'] & s['RL'] & p['L']), n['S']),
    ctrl.Rule((m['S'] & s['RL'] & p['L']), n['S']),
    ctrl.Rule((m['M'] & s['RL'] & p['L']), n['VS']),
    ctrl.Rule((m['VS'] & s['L'] & p['L']), n['S']),
    ctrl.Rule((m['S'] & s['L'] & p['L']), n['S']),
    ctrl.Rule((m['M'] & s['L'] & p['L']), n['VS']),
    ctrl.Rule((m['VS'] & s['S'] & p['M']), n['S']),
    ctrl.Rule((m['S'] & s['S'] & p['M']), n['VS']),
    ctrl.Rule((m['M'] & s['S'] & p['M']), n['VS']),
    ctrl.Rule((m['VS'] & s['RS'] & p['M']), n['S']),
    ctrl.Rule((m['S'] & s['RS'] & p['M']), n['VS']),
    ctrl.Rule((m['M'] & s['RS'] & p['M']), n['VS']),
    ctrl.Rule((m['VS'] & s['M'] & p['M']), n['RS']),
    ctrl.Rule((m['S'] & s['M'] & p['M']), n['S']),
    ctrl.Rule((m['M'] & s['M'] & p['M']), n['VS']),
    ctrl.Rule((m['VS'] & s['RL'] & p['M']), n['M']),
    ctrl.Rule((m['S'] & s['RL'] & p['M']), n['RS']),
    ctrl.Rule((m['M'] & s['RL'] & p['M']), n['S']),
    ctrl.Rule((m['VS'] & s['L'] & p['M']), n['M']),
    ctrl.Rule((m['S'] & s['L'] & p['M']), n['RS']),
    ctrl.Rule((m['M'] & s['L'] & p['M']), n['S']),
    ctrl.Rule((m['VS'] & s['S'] & p['H']), n['VL']),
    ctrl.Rule((m['S'] & s['S'] & p['H']), n['L']),
    ctrl.Rule((m['M'] & s['S'] & p['H']), n['M']),
    ctrl.Rule((m['VS'] & s['RS'] & p['H']), n['VL']),
    ctrl.Rule((m['S'] & s['RS'] & p['H']), n['RL']),
    ctrl.Rule((m['M'] & s['RS'] & p['H']), n['RS']),
    ctrl.Rule((m['VS'] & s['M'] & p['H']), n['M']),
    ctrl.Rule((m['S'] & s['M'] & p['H']), n['M']),
    ctrl.Rule((m['M'] & s['M'] & p['H']), n['S']),
    ctrl.Rule((m['VS'] & s['RL'] & p['H']), n['RL']),
    ctrl.Rule((m['S'] & s['RL'] & p['H']), n['M']),
    ctrl.Rule((m['M'] & s['RL'] & p['H']), n['RS']),
    ctrl.Rule((m['VS'] & s['L'] & p['H']), n['L']),
    ctrl.Rule((m['S'] & s['L'] & p['H']), n['M']),
    ctrl.Rule((m['M'] & s['L'] & p['H']), n['RS'])
]



# Create the control system
spare_system_ctrl = ctrl.ControlSystem(rules3)
spare_system = ctrl.ControlSystemSimulation(spare_system_ctrl)

m_values = np.arange(0, 0.7, 0.01)  
s_values = np.arange(0, 1.0, 0.01)  
p_value = 0.5
M, S = np.meshgrid(m_values, s_values)
N = np.zeros_like(M)

# Compute the output for each combination of m and s
for i in range(M.shape[0]):
    for j in range(M.shape[1]):
        spare_system.input['p'] = p_value
        spare_system.input['m'] = M[i, j]
        spare_system.input['s'] = S[i, j]
        
        try:
            spare_system.compute()
            N[i, j] = spare_system.output['n']
        except ValueError:
            print("du fucka opp simen")
        
        


fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(M, S, N, cmap='viridis', edgecolor='none')
ax.set_xlabel('m')
ax.set_ylabel('s')
ax.set_zlabel('n')
fig.colorbar(surf, shrink=0.5, aspect=5, label='Output (n)')
plt.title('Fuzzy System Output (n) for varying m and s with p=0.5')

plt.show()


# Viewing the result
n.view(sim=spare_system)
spare_system.input['m'] = 0.5
spare_system.input['s'] = 0.2
spare_system.input['p'] = 0.8
spare_system.compute()
print(spare_system.output['n'])
