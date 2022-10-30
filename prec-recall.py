import pandas as pd
import itertools

# God class: CoreDocumentImpl, DTDGrammar, XSDHandler, XIncludeHandler
GodClass_name = "CoreDocumentImpl" # add the name of god class here
truth = pd.read_csv(f"ground-truth_{GodClass_name}.csv")
df = pd.read_csv(f"hierarchical_{GodClass_name}_clustering_file.csv") # cluster file

# get a dictionary, whose key is the cluster, value is MethodName in the same cluster
df_dict = df.groupby(['cluster_id']).apply(lambda x: x['method_name'].tolist()).to_dict()
# get a dictionary, whose key is the keyword, value is MethodName with the same keyword
truth_dict = truth.groupby(['Keywords']).apply(lambda x: x['MethodName'].tolist()).to_dict()

# get intra-pairs
df_pair = []
for key, value in df_dict.items():
    for pair in itertools.permutations(value,2):
        df_pair.append(pair)

truth_pair = []
for key, value in truth_dict.items():
    for pair in itertools.permutations(value,2):
        truth_pair.append(pair)

# get numbers of intra-pairs in our clusters and ground truth
intraD = len(df_pair)
intraG = len(truth_pair)

intersection = 0
for i in df_pair:
    if i in truth_pair:
        intersection += 1

p = intersection/intraD
r = intersection/intraG
F1 = 2 * p * r / (p + r)
print("p =",p)
print("r =",r)
print("F1 =",F1)
