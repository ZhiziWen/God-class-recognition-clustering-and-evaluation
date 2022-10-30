# God-class-recognition-clustering-and-evaluation

This project identify God Classes from Java files. The detailed explaination is provided in the file "IMA_Project_1_ZhiziWen.pdf".

Definition:

A God class is a class that does too much: 

• violates the “single responsibility” and “abstraction/encapsulation” OO design principles 

• does not support reuse, because it does not implement a single, well defined functionality 

• does not abstract from the domain, since it is usually entangled with multiple implementation details (hence it is also difficult to test)

<br>


Short explaination of what I have done:

•	In find_god_class.py, I conduct data pre-processing to identify God classes in 700 Java files. Four god classes are found, e.g., CoreDocumentImpl. 

•	In extract_feature_vactors.py, I defined four utility functions: ”get fields”, ”get method”, ”get methods accessed by method” and ”get fields accessed by method” to identify the public fields and methods and if they are used in a class or not. With this python file, each methods in god classes has its feature vectors extracted (whether or not it has use a field or public class) and put into a csv file. For example, the java class "CoreDocumentImpl.java" has its feature vectors stored in the file "CoreDocumentImpl_FeatureVector.csv".

•	In the two file ”k means.py” and ”hierachical.py”, I apply clustering algorithms K-means and Hierarchical Clustering to partition the methods in God classes with python library scikit-learn. 

•	In silhouette.py, I check which K is the best to partition the methods in God classes. 

•	Since I am not developers of Xerces (source Java code), it is difficult to define the ground truth manually. So, I approximate it by checking the presence of keywords in method names (as substrings), such as "create", "event" in ground-truth.py. 

•	At the end, in prec-recall.py, I measure the quality of the God class partitions with precision, recall and F1 score.
