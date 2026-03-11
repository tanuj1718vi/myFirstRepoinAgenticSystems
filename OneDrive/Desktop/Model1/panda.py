import pandas as pd
import matplotlib.pyplot as plt


data={"user":["tanuj","satyarth","satyarth","tanuj"],
      "product":["laptop","mobile","laptop","mobile"],
      "price":[1000,500,1000,500]
      }
df=pd.DataFrame(data)
print(df)
df.plot(x="user", y="price", kind="bar")
plt.show()