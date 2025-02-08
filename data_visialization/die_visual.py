import plotly.express as px  # type: ignore

from die import Die

die = Die()
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

frequencies = []
poss_results = range(1, die.num_sizes + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

title = "六面のサイコロを1,000回転がした結果"
labels = {"x": "結果", "y": "発生した回数"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()
