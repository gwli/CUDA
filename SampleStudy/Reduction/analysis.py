import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  
DataList= ["int.csv", "float.csv", "double.csv" ]


rs_int=pd.read_csv(DataList[0])

fig=plt.figure("time with num of element")
rs_int.ix[0].plot(label="reduce0",legend=True)
rs_int.ix[1].plot(label="reduce1",legend=True)
rs_int.ix[2].plot(label="reduce2",legend=True)
rs_int.ix[3].plot(label="reduce3",legend=True)
rs_int.ix[4].plot(label="reduce4",legend=True)
rs_int.ix[5].plot(label="reduce5",legend=True)
rs_int.ix[6].plot(label="reduce6",legend=True)

fig.show()
fig.savefig("reduce_int.png")


fig2=plt.figure("element less on 512")
rs_int.iloc[:,1:25].plot()
fig2.show()
fig2.savefig("int_lt_512.png")




