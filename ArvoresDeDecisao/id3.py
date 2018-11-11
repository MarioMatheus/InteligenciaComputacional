import math
import playtennis

def calculate_entropy(data, len_sample):
    entropy = 0
    for key in data.keys():
        p_i = float(data[key]) / len_sample
        entropy += - p_i * math.log(p_i, 2)
    
    return entropy


def dataset_split(data, factor_index, val):
 newData = []
 for rec in data: 
   if rec[factor_index] == val:
     reducedSet = list(rec[:factor_index]) 
     reducedSet.extend(rec[factor_index+1:])
     newData.append(reducedSet)
 
 return newData


def calculate_factor_entropy(label_list, factor_index, data):
    factor_entropy = 0.0
    for label in label_list:
        new_data = dataset_split(data, factor_index, label)
        probability = len(new_data) / float(len(data))
        entropy = probability * calculate_entropy(playtennis.get_labels_count(new_data), len(new_data))
        factor_entropy += entropy
    
    return factor_entropy
        


def calculate_factors_gain(data, decisions):
    factors = len(data[0]) - 1
    base_entropy = calculate_entropy(decisions, len(data))
    factors_gain = []
    
    for i in range(factors):
        label_list = set([rec[i] for rec in data])
        factor_entropy = calculate_factor_entropy(label_list, i, data)
        factors_gain.append(base_entropy - factor_entropy)
        
    return factors_gain


def get_factor_max_gain(data, decisions, labels):
    factors_gains = calculate_factors_gain(data, decisions)
    index = factors_gains.index(max(factors_gains))

    return labels[index], index


def build_decision_tree(data, decisions, data_map):
    class_list = [rec[-1] for rec in data]
    if class_list.count(class_list[0]) == len(class_list):
        return class_list[0]

    tree_label, index = get_factor_max_gain(data, decisions, data_map)
    tree = { tree_label: {} }
    del(data_map[index])
    node_values = set([rec[index] for rec in data])
    for value in node_values:
        sub_labels = data_map[:]
        tree[tree_label][value] = build_decision_tree(dataset_split(data, index, value), decisions, sub_labels)

    return tree   


def id3_for_playtennis():
    return build_decision_tree(playtennis.data, playtennis.decisions, playtennis.data_map)


def i_can_play_tennis_with(conditions):
    answers = ['Yes', 'No']
    decision_tree = id3_for_playtennis()
    answer = ''
    while answer not in answers:
        node = list(decision_tree.keys())[0]
        if node not in conditions.keys():
            answer = 'Depends on the ' + node
            break
        answer = decision_tree[node][conditions[node]]
        decision_tree = answer

    return answer


# decision_tree = id3_for_playtennis()
# print(decision_tree)

current_conditions = {
    "Outlook": "Rain",
    "Humidity": "High"
}

answer = i_can_play_tennis_with(current_conditions)
print(answer)