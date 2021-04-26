import matplotlib.pyplot as plt

filename = "jumper1_1619187460.684719_LOG_Myoware_Muscle_Sensor.txt"
data = []
df = {"value": [], "time": []}
with open(filename,"r") as file:
    for line in file:
        data.append(line)
for item in data:
    df["value"].append(item[:2])
    df["time"].append(item.split("=")[1][:-1])

print(df["time"])

plt.plot(df["time"][:100],df["value"][:100])
plt.show()