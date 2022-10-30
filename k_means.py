import pandas as pd
from sklearn.cluster import KMeans

def CSV_reader(csvFile):
    df = pd.read_csv(csvFile)
    methodName = df[df.columns[0]].to_numpy()
    df = df.drop(df.columns[0], axis=1)
    featureVector = df.values
    return methodName, featureVector

def Kmeans_Caculator(methodName, featureVector, NumberOfClusters, file_name):
    kmeans = KMeans(n_clusters=NumberOfClusters, random_state=100).fit(featureVector) #random_state is for reproducibility
    prediction = kmeans.labels_
    result = pd.DataFrame({'cluster_id': prediction, 'method_name': list(methodName)}, columns=['cluster_id', 'method_name'])
    result = result.sort_values(by=['cluster_id'])
    result.to_csv(f"Kmeans_{file_name}_clustering_file.csv")
    print(result)
    return result

# God class: CoreDocumentImpl, DTDGrammar, XSDHandler, XIncludeHandler
GodClass_name = "CoreDocumentImpl" # add the name of god class here
methodName, featureVector = CSV_reader(f'{GodClass_name}_FeatureVector.csv')
Kmeans_Caculator(methodName, featureVector, 44, GodClass_name)

