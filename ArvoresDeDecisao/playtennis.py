
data_map = ["Outlook", "Temperature", "Humidity", "Wind", "Decision"]

data = [
    ["Sunny", "Hot", "High", "Weak", "No"],
    ["Sunny", "Hot", "High", "Strong", "No"],
    ["Overcast", "Hot", "High", "Weak", "Yes"],
    ["Rain", "Mild", "High", "Weak", "Yes"],
    ["Rain", "Cool", "Normal", "Weak", "Yes"],
    ["Rain", "Cool", "Normal", "Strong", "No"],
    ["Overcast", "Cool", "Normal", "Strong", "Yes"],
    ["Sunny", "Mild", "High", "Weak", "No"],
    ["Sunny", "Cool", "Normal", "Weak", "Yes"],
    ["Rain", "Mild", "Normal", "Weak", "Yes"],
    ["Sunny", "Mild", "Normal", "Strong", "Yes"],
    ["Overcast", "Mild", "High", "Strong", "Yes"],
    ["Overcast", "Hot", "Normal", "Weak", "Yes"],
    ["Rain", "Mild", "High", "Strong", "No"]
]

total_decisions = len(data)
decisions = {}
for d in data:
    if d[-1] in decisions.keys():
        decisions[d[-1]] += 1
    else:
        decisions[d[-1]] = 1

def get_labels_count(data):
    labels_count = {}
    for d in data:
        if d[-1] in labels_count.keys():
            labels_count[d[-1]] += 1
        else:
            labels_count[d[-1]] = 1
            
    return labels_count
