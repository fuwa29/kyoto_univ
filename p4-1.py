# x の平方根を求める list格納版
x = 2

# 最初の近似値を想定する
rnew  = x
rnew_list = [rnew]

# 1週目
r1 = rnew
r2 = x/r1
rnew = (r1 + r2)/2
print(r1, rnew, r2)
## list にrnewを追加
rnew_list.append(rnew)

# 2週目
r1 = rnew
r2 = x/r1
rnew = (r1 + r2)/2
print(r1, rnew, r2)
## list にrnewを追加
rnew_list.append(rnew)

# 3週目
r1 = rnew
r2 = x/r1
rnew = (r1 + r2)/2
print(r1, rnew, r2)
## list にrnewを追加
rnew_list.append(rnew)

# 4週目
r1 = rnew
r2 = x/r1
rnew = (r1 + r2)/2
print(r1, rnew, r2)
## list にrnewを追加
rnew_list.append(rnew)

# print list
print(rnew_list)
