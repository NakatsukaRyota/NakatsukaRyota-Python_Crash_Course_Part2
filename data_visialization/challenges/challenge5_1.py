import csv
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt

path = Path("weather_data/sitka_weather_2021_full.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

dates, precipitations = [], []
for row in reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    try:
        precipitation = float(row[5])
    except ValueError:
        print(f"{current_date}のデータがありません")
    else:
        dates.append(current_date)
        precipitations.append(precipitation)

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(dates, precipitations, color="red")

ax.set_title("Daily Precipitation, 2021\nSitka", fontsize=24)
ax.set_xlabel("", fontsize=20)
fig.autofmt_xdate()
ax.set_ylabel("Precipitation", fontsize=16)
ax.tick_params(labelsize=16)
plt.show()
