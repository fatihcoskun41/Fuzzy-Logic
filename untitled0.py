import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

x_speed = ctrl.Antecedent(np.arange(0, 101, 1), 'Hız')
x_amount_water = ctrl.Antecedent(np.arange(0,101,1), 'Water')
y_wipe = ctrl.Consequent(np.arange(0, 11, 0.001), 'Wipe')



x_speed['not-run'] = fuzz.trimf(x_speed.universe,[0, 0, 0])
x_speed['low'] = fuzz.trimf(x_speed.universe,[1, 20, 40])
x_speed['normal'] = fuzz.trimf(x_speed.universe, [35, 50, 60])
x_speed['hig'] = fuzz.trimf(x_speed.universe, [50, 100, 100])

x_amount_water['not-run'] = fuzz.trimf(x_amount_water.universe,[0, 0, 0])
x_amount_water['low'] = fuzz.trimf(x_amount_water.universe,[1,20,40])
x_amount_water['normal'] = fuzz.trimf(x_amount_water.universe,[35,50,60])
x_amount_water['hig'] = fuzz.trimf(x_amount_water.universe,[50,100,100])

y_wipe['not-run'] = fuzz.trimf(y_wipe.universe, [0, 0, 0])
y_wipe['poor'] = fuzz.trimf(y_wipe.universe, [0.1, 3, 5])
y_wipe['normal'] = fuzz.trimf(y_wipe.universe, [4, 6, 8])
y_wipe['strong'] = fuzz.trimf(y_wipe.universe, [5, 10, 10])


x_speed.view()
plt.title('Hız')
plt.show()

x_amount_water.view()
plt.title('Su miktarı (ml)')
plt.show()

y_wipe.view()
plt.title('Silecek Gücü')
plt.show()


#Set rules in system
rule1 = ctrl.Rule(x_speed['hig'] & x_amount_water['hig'], y_wipe['strong'])
rule2 = ctrl.Rule(x_speed['normal'] & x_amount_water['normal'], y_wipe['normal'])
rule3 = ctrl.Rule(x_speed['low'] & x_amount_water['hig'], y_wipe['normal'])
rule4 = ctrl.Rule(x_speed['hig'] & x_amount_water['low'], y_wipe['poor'])
rule5 = ctrl.Rule(x_speed['low'] & x_amount_water['low'], y_wipe['poor'])
rule6 = ctrl.Rule(x_speed['normal'] & x_amount_water['hig'], y_wipe['strong'])
rule7 = ctrl.Rule(x_speed['hig'] & x_amount_water['normal'], y_wipe['normal'])
rule8 = ctrl.Rule(x_speed['not-run'] & x_amount_water['not-run'], y_wipe['not-run'])
rule9 = ctrl.Rule(x_speed['not-run'] & x_amount_water['normal'], y_wipe['not-run'])
rule10 = ctrl.Rule(x_speed['not-run'] & x_amount_water['low'], y_wipe['not-run'])
rule11 = ctrl.Rule(x_speed['not-run'] & x_amount_water['hig'], y_wipe['not-run'])
rule12 = ctrl.Rule(x_speed['low'] & x_amount_water['not-run'], y_wipe['not-run'])
rule13 = ctrl.Rule(x_speed['normal'] & x_amount_water['not-run'], y_wipe['not-run'])
rule14 = ctrl.Rule(x_speed['hig'] & x_amount_water['not-run'], y_wipe['not-run'])








suggestion_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4,rule5,rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14])

suggestion = ctrl.ControlSystemSimulation(suggestion_ctrl)


suggestion.input['Hız'] = int(input("Hız değeri giriniz:"))
suggestion.input['Water'] =int(input("Su miktarını giriniz:"))

suggestion.compute()

print(suggestion.output['Wipe'])

y_wipe.view(sim=suggestion)
plt.title('Power of Wiper')
plt.show()
