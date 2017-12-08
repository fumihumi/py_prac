import numpy as np
import pandas as pd
from pandas import Series

line = "-------------------------"

obj = Series([3,7,10,13])
print (f"obj: {obj}")

numpy_array = np.array([3,7,10,13])
print(f"numpy_Array: {numpy_array}")

# Series(シリーズ)は、一次元の配列のようなオブジェクトです。
# シリーズには、データ配列とそれに紐付くインデックスという配列が含まれます。
print(f"series: {Series(numpy_array)}")

print(f"obj values: {obj.values}")

obj2 = Series([3,7,10,13], index=['apple', 'orange', 'mango', 'peach'])
print(f"obj2 series, index : \n{obj2}")
# indexを指定して、値を取り出す
print(f"obj2: {obj2['orange']}")
