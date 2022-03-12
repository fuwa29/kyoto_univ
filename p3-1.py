# x の平方根を求める
x = 2

# 最初の近似値を想定する
rnew  = x

# 1週目
r1 = rnew
r2 = x/r1
rnew = (r1 + r2)/2
print(r1, rnew, r2)

