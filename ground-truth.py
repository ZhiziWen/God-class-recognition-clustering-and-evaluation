import pandas as pd

# God class: CoreDocumentImpl, DTDGrammar, XSDHandler, XIncludeHandler
GodClass_name = "CoreDocumentImpl" # add the name of god class here
df = pd.read_csv(f"{GodClass_name}_FeatureVector.csv")
methods_list = df.iloc[:,0].tolist() # get list of methods

keywords_list = ["create", "object", "cache", "uri", "standalone", "encoding", "identifier",
                 "user", "error", "content", "parameter", "subset", "global", "component"]

ground_truth = {}
ground_truth = ground_truth.fromkeys(keywords_list, list())
ground_truth['None'] = list()
methods_added = list()

for method in methods_list:
    for keys in keywords_list:
        if keys.lower() in method.lower():
            methods_added.append(method)
            if ground_truth[keys] == []:
                ground_truth[keys] = [method]
            else:
                ground_truth[keys].append(method)
        continue

for met in methods_list:
    if met not in methods_added:
        if ground_truth['None'] == []:
            ground_truth['None'] = [met]
        else:
            ground_truth['None'].append(met)

df = pd.DataFrame.from_dict(ground_truth, orient = "index").sort_index().stack().reset_index(level=1, drop=True).reset_index()
df.columns = ['Keywords','MethodName']
df.to_csv(f"ground-truth_{GodClass_name}.csv")

print(df)