# mine_detecter_ai
This machine learning model uses a DecisionTree to detect mines via a FLC sensor that detects magnetic distortion



**Inputs are:**
1:Voltage Given by FLC Sensor(0v-1v).
2:Height Of FLC Sensor from ground(0m to 1m).
3:Soil Type:
  1=Dry and Sandy
  2=Dry and Humus
  3=Dry and Limy
  4=Humid and Sandy
  5=Humid and Humus
  6=Humid and Limy


**Output:**
1:Mine Existance:0 for no mine and 1 for mine
