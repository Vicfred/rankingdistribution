import matplotlib.pyplot as plt
import numpy as np

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'red', 'orange', 'yellow', 'blue', 'cyan', 'green', 'brown', 'gray'
colors = ('#ff0000', '#ffb331', '#fef53a', '#2667f2', '#3afeee', '#00c911', '#5e4838', '#afafaf')
sizes = [147-1+1, 379-148+1, 1340-382+1, 3295-1352+1, 7221-3301+1, 14671-7254+1, 25565-14702+1, 79577-25598+1]
labels = 'red', 'orange', 'yellow', 'blue', 'cyan', 'green', 'brown'
colors = ('#ff0000', '#ffb331', '#fef53a', '#2667f2', '#3afeee', '#00c911', '#5e4838')
sizes = [147-1+1, 379-148+1, 1340-382+1, 3295-1352+1, 7221-3301+1, 14671-7254+1, 25565-14702+1]
# labels = 'red', 'orange', 'yellow', 'blue', 'cyan', 'green'
# colors = ('#ff0000', '#ffb331', '#fef53a', '#2667f2', '#3afeee', '#00c911')
# sizes = [147-1+1, 379-148+1, 1340-382+1, 3295-1352+1, 7221-3301+1, 14671-7254+1]
#explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
#explode = (0.5, 0.3, 0.2, 0, 0, 0, 0, 0)

patches, texts = plt.pie(sizes, colors=colors, wedgeprops = { 'linewidth' : 1, 'edgecolor' : 'white' })
total = sum(sizes)
cumulative = sizes.copy()
for i in range(1,len(sizes)):
    cumulative[i] += cumulative[i - 1]
labels = [f'{l}, {s/total*100:0.2f}%' for l, s in zip(labels, sizes)]
labels = [f'{s/total*100:0.2f}% {c/total*100:0.2f}%' for s, c in zip(sizes, cumulative)]
print(sizes, cumulative)
plt.legend(bbox_to_anchor=(0.95, 1), loc='upper left', labels=labels)
plt.title('Atcoder ranking distribution', bbox={'facecolor':'0.8', 'pad':5})
plt.axis('equal')
plt.tight_layout()

plt.savefig('atcoderpie.png')
