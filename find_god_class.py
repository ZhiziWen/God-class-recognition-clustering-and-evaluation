import javalang
import os
import numpy as np
import pandas as pd

data = {}
methods =[]
god_class = {}

for paths, dirs, files in os.walk("./project-1-god-classes-ZhiziWen-main/resources/xerces2-j-src", topdown ="true"):
    for name in files:
        if '.java' in name:
            fullpath = os.path.join(paths, name)
            f = open(fullpath, 'r')
            f_read = f.read()
            tree = javalang.parse.parse(f_read)
            for path, node in tree:
                if type(node) is javalang.tree.ClassDeclaration:
                    methods.append(len(node.methods))
                    data[node.name] = len(node.methods)

average = np.mean(methods)
std = np.std(methods)
threshold_god = average + 6 * std

for key in data:
    if data[key] > threshold_god:
        god_class[key] = data[key]
god_df = pd.DataFrame(god_class.items(), columns=['class_name','method_num'])
print(god_df)


