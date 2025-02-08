import csv
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt

# シトカの気温を描写
path = Path("weather_data/death_valley_2021_simple.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f"{current_date}のデータがありません")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(dates, highs, color="red")
ax.plot(dates, lows, color="blue")
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.6)

# デスバレーの気温を描写
path = Path("weather_data/sitka_weather_2021_simple.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    high = int(row[4])
    low = int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

ax.plot(dates, highs, color="red")
ax.plot(dates, lows, color="blue")
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.3)


ax.set_title(
    "Daily High and Low Temperatures, 2021\nDeath Valley, CA and Sitka", fontsize=24
)
ax.set_xlabel("", fontsize=20)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)
ax.set_ylim(0, 140)
plt.show()
