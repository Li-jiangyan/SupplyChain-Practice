import pandas as pd

# 读取Excel文件
df = pd.read_excel("orders.xlsx")

# 计算总销售额
total_sales = df["销售额"].sum()

# 输出结果
print(f"总销售额：{total_sales}元")