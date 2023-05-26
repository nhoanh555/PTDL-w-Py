import pandas as pd
import matplotlib.pyplot as plt


# Đọc dữ liệu từ file Excel
df = pd.read_csv("C:\\Users\\USER\\Desktop\\PTDL w Py\\ds_salaries.csv")

# Hiển thị dữ liệu
print(df)


# bài toán tính hệ số tương quan giữa lương và lương bằng USD, lấy dữ liệu trong khoảng từ hàng1-100
# Tính toán hệ số tương quan trong khoảng từ 1 đến 100
data_subset = df.iloc[0:100]
correlation = data_subset['salary'].corr(data_subset['salary_in_usd'])


# correlation = df['salary'].corr(df['salary_in_usd'])

print("Hệ số tương quan:", correlation)

# Vẽ biểu đồ
plt.scatter(data_subset['salary'], data_subset['salary_in_usd'], color='blue', label='Dữ liệu')

plt.xlabel('Lương')
plt.ylabel('Lương bằng USD')
plt.title('Biểu đồ tương quan')
plt.legend()

plt.show()
