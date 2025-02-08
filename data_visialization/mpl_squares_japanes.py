import matplotlib.pyplot as plt
from matplotlib import rcParams

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use("seaborn-v0_8")
rcParams["font.family"] = "Yu Gothic"
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

ax.set_title("平方数", fontsize=24)
ax.set_xlabel("値", fontsize=14)
ax.set_ylabel("2乗した値", fontsize=14)

ax.tick_params(labelsize=14)
ax.axis((0, 1100, 0, 1_100_000))
ax.ticklabel_format(style="plain")
plt.show()
