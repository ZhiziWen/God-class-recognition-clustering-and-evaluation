from sklearn.metrics import silhouette_score
import pandas as pd
from sklearn.cluster import KMeans
from k_means import CSV_reader
from sklearn.cluster import AgglomerativeClustering
from sklearn.utils._testing import ignore_warnings
from sklearn.exceptions import ConvergenceWarning
import numpy as np

def silhouete_caculator_with_clustering(FeatureVectorFile, ClusteringFile):
    dfF = pd.read_csv(FeatureVectorFile)
    dfC = pd.read_csv(ClusteringFile)
    df = dfC.merge(dfF, left_on='method_name', right_on='Unnamed: 0')
    ClusterLabel = df[df.columns[1]].to_numpy()
    df = df.drop(df.columns[:4], axis=1)
    featureVector = df.values
    print("silhouete score with this clustering file: ", silhouette_score(featureVector, ClusterLabel))

@ignore_warnings(category=ConvergenceWarning)
def silhouete_caculator_without_clustering(FeatureVectorFile):
    methodName, array = CSV_reader(FeatureVectorFile)
    KmeansSilhouete = []
    HierarchicalSilhouete = []

    for k in range(2, 61):
        KmeansLabels = KMeans(n_clusters=k, random_state=100).fit(array).labels_
        HierarchicalLabels = AgglomerativeClustering(n_clusters=k, linkage = "complete").fit(array).labels_
        KmeansSilhouete.append(silhouette_score(array, KmeansLabels))
        HierarchicalSilhouete.append(silhouette_score(array, HierarchicalLabels))

    print("K-means")
    for a in range(0, 59):
        print(a + 2, KmeansSilhouete[a])

    print("Agglomerative")
    for b in range(0, 59):
        print(b + 2, HierarchicalSilhouete[b])

    MaxKmeansSilhouete = np.max(KmeansSilhouete)
    MaxHierarchicalSilhouete = np.max(HierarchicalSilhouete)

    for i in range(0, 59):
        if KmeansSilhouete[i] == MaxKmeansSilhouete:
            print("The best K for Kmeans algorithum is", i + 2, "with Silhouete score of", MaxKmeansSilhouete)
            break
    for i in range(0, 59):
        if HierarchicalSilhouete[i] == MaxHierarchicalSilhouete:
            print("The best K for Agglomerative algorithum is", i + 2, "with Silhouete score of", MaxHierarchicalSilhouete)
            break

# God class: CoreDocumentImpl, DTDGrammar, XSDHandler, XIncludeHandler
GodClass_name = "CoreDocumentImpl" # add the name of god class here
silhouete_caculator_with_clustering(f'{GodClass_name}_FeatureVector.csv', f'Kmeans_{GodClass_name}_clustering_file.csv')
silhouete_caculator_without_clustering(f'{GodClass_name}_FeatureVector.csv')
