import matplotlib.pyplot as plt
from matplotlib import rcParams

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use("seaborn-v0_8")
rcParams["font.family"] = "Yu Gothic"
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

ax.set_title("立方数", fontsize=24)
ax.set_xlabel("値", fontsize=14)
ax.set_ylabel("3乗した値", fontsize=14)

ax.tick_params(axis="both", labelsize=14)
ax.ticklabel_format(style="plain")
plt.show()
