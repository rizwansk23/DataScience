from pandas import read_csv
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

df=read_csv("Data/iris.csv")
# mm=MinMaxScaler()
# df['Age']=mm.fit_transform(df[['Age']])
# df['Income($)']=mm.fit_transform(df[['Income($)']])
# # print(df)

# km=KMeans(n_clusters=3)
# X=df[['Age','Income($)']]
# y_predict=km.fit_predict(X)

# df['clusters']=y_predict
# print(df)

# centroids=km.cluster_centers_
# print(centroids)

# df1=df[df['clusters']==0]
# df2=df[df['clusters']==1]
# df3=df[df['clusters']==2]

# plt.scatter(df1['Age'],df1['Income($)'],color='red')
# plt.scatter(df2['Age'],df2['Income($)'],color='blue')
# plt.scatter(df3['Age'],df3['Income($)'],color='green')
# plt.scatter(centroids[:,0],centroids[:,1],color='black')
# plt.xlabel('Age')
# plt.ylabel('Income($)')
# plt.legend(df['Income($)'])
# plt.show()


sse=[]
rng=range(1,10)
for k in rng:
    km=KMeans(n_clusters=k)
    km.fit(df[['Age','Income($)']])
    sse.append(km.inertia_)
    
plt.xlabel('Age')
plt.ylabel('Income($)')
plt.plot(rng,sse)
plt.show()