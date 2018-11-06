import math
import playtennis

def calculate_entropy(data, len_sample):
    entropy = 0
    for key in data.keys():
        p_i = float(data[key]) / len_sample
        entropy += - p_i * math.log(p_i, 2)
    
    return entropy


decision_entropy = calculate_entropy(playtennis.decisions, playtennis.total_decisions)
print(decision_entropy)
