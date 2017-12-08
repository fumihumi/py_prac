import matplotlib.pyplot as plt
import numpy as np

line = '----------------------'

#############################3
##  python array 
print(line)
arr = np.array([[1,2,3], [4,5,6]])

print(arr * arr)
print(5 * arr)
print(arr / arr)
print(arr / 2)
print(1 / arr)
print(arr + arr) 
print( arr ** 3)
#-------------------------
print(line)
#----------------------------

ary = np.arange(10)
print(ary)


print(line)
# ----------------------
# 二次元

arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr)
# ２行、３列にアクセスする
print(arr[1, 2])

##-----------------------
## 3次元
print(line)

arr = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [0,1,2]]])
print(arr)
print(arr[0,1])
print(arr[1,0,2])


# -----------------------
# 演算子
print(line)
arr = np.arange(9).reshape((3,3))
print(arr)
arr = np.arange(10).reshape((2,5))
print(arr)

print(line)
print(np.arange(10))
# 平方根 sqrt (array)
print(np.sqrt(np.arange(10)))

# 正規分布に従う乱数
print(line)
print(np.random.randn(10))
# 要素ごとの符号を返す  sign （正は1、負は-1）
print(np.sign(np.random.randn(10)))

# 
print(line)
tmp = np.array([ 0.54090848,  0.70922084,  0.57458547,  0.55307476,  0.738459  ])
print(tmp)
# 平均を出力
print(tmp.mean())
#  標準偏差を出力
print(tmp.std())



