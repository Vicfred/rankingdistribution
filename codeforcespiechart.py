import matplotlib.pyplot as plt
import numpy as np

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'red', 'orange', 'purple', 'blue', 'cyan', 'green'
colors = ('#ff0000', '#ffb331', '#773eff', '#2667f2', '#3afeee', '#00c911')
# Color changes pages: 1,2,4,5,14,26,72,131,228
# May 31, 2021
# sizes = [650-1+1, 2836-654+1, 5388-2854+1, 12893-5406+1, 21102-12934+1, 34189-21157+1]
# April 09, 2025
sizes = [674-1+1, 2741-674+1, 5115-2741+1, 14363-5115+1, 26185-14363+1, 45558-26185+1]
#explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
#explode = (0.5, 0.3, 0.2, 0, 0, 0, 0, 0)

patches, texts = plt.pie(sizes, colors=colors, wedgeprops = { 'linewidth' : 1, 'edgecolor' : 'white' })
total = sum(sizes)
cumulative = sizes.copy()
for i in range(1,len(sizes)):
    cumulative[i] += cumulative[i - 1]
labels = [f'{s/total*100:0.2f}% {c/total*100:0.2f}%' for s, c in zip(sizes, cumulative)]
print(sizes,cumulative)
plt.legend(bbox_to_anchor=(0.95, 1), loc='upper left', labels=labels)
plt.title('Codeforces ranking distribution', bbox={'facecolor':'0.8', 'pad':5})
plt.axis('equal')
plt.tight_layout()

plt.savefig('codeforcespie.png')
