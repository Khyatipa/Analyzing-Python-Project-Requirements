import csv
import matplotlib.pyplot as plt

csv_file_path = 'output_temp.csv'

with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    fewCounter = 0
    moderateCounter = 0
    regularCounter = 0
    noCounter = 0
    index = 1
    for row in reader:
        if len(row) == 4:
            field3 = int(row[2])
            field4 = int(row[3])
            if field3 > 0:
                percentage = field4 * 100 / field3
            else:
                percentage = 0
            print(f"{index} -- Field 3: {field3}, Field 4: {field4} -- Percentage: {percentage}")
            index += 1
            if percentage == 0:
                noCounter += 1
            elif 0 < percentage < 20:
                fewCounter += 1
            elif 20 < percentage < 60:
                moderateCounter += 1
            else:
                regularCounter += 1

# Create data for the pie chart
labels = ['No Changes', 'Few Changes', 'Moderate Changes', 'Regular Changes']
sizes = [noCounter, fewCounter, moderateCounter, regularCounter]
colors = ['green', 'gold', 'lightskyblue', 'lightcoral']

# Create the pie chart with percentages and counts
def autopct_format(pct):
    total = sum(sizes)
    count = int(pct / 100.0 * total)
    return f'{pct:.1f}%\n({count})'

# Create the pie chart
plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct=autopct_format, shadow=True, startangle=140)

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Distribution of Percentages")

# Display the pie chart
plt.show()

print("Stats:")
print(f"noCounter - {noCounter}")
print(f"fewCounter - {fewCounter}")
print(f"moderateCounter - {moderateCounter}")
print(f"regularCounter - {regularCounter}")
