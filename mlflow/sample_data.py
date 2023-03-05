from sklearn import datasets
import numpy as np
import pandas as pd

data = datasets.load_diabetes()
df = pd.DataFrame(data.data)
print(data.feature_names)
print(df.head())

print(data.target[0])



# [[0.038076,  0.050680,  0.061696,  0.021872, -0.044223, -0.034821, -0.043401, -0.002592,  0.019908, -0.017646]]
# 151.0
# ["age", "sex", "bmi", "bp", "s1", "s2", "s3", "s4", "s5", "s6"]

# mlflow models serve -m ./mlruns/0/aeb895f254f64f04a26a666bd5070693/artifacts/model -p 1234

# curl -X POST -H "Content-Type:application/json"  \
# --data '{"columns":["age", "sex", "bmi", "bp", "s1", "s2", "s3", "s4", "s5", "s6"], \
# "data": [[0.038076,  0.050680,  0.061696,  0.021872, -0.044223, -0.034821, -0.043401, -0.002592,  0.019908, -0.017646]]}' http://127.0.0.1:1234/invocations

#  [157.3774842648259]

