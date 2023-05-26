import pandas as pd
import numpy as np
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("C:\\Users\\USER\\Desktop\\PTDL w Py\\ds_salaries.csv")#đọc dữ liệu
#print(data)

#print("đếm xem có bao nhiêu giá trị duy nhất trong cột:\n\n", data.nunique())

#print("tóm tắc ngắn gọn các thông tin của dữ liệu \n\n",data.info())

#print("in ta tổng số giá trị thiếu trong mỗi cột của dữ liệu \n\n",data.isna().sum())

#print("in ra tổng số các giá trị duy nhất trong các cột \n",data[['work_year', 'salary']].value_counts())

# - Tính trung bình, trung vị, max, min của mức lương của các công việc 
grouped_data = data.groupby('job_title')['salary'].agg(['mean', 'median', 'max', 'min'])
# In ra bản phân tổ 
#print("bảng phân tổ các loại công việc theo mức lương \n", grouped_data)

def bieu_do_tron_experience_level(): 
   # kích thước của hình
   plt.figure(figsize = (10, 8))
   # tạo biểu đồ tròn thể hiện sự phân phối cấp độ kinh nghiệm
   data['experience_level'].value_counts().plot(kind='pie', autopct='%1.1f%%', cmap='viridis')
   # thêm tiêu đề cho biểu đồ
   plt.title('Bảng phân phối các cấp độ kinh nghiệm')
   plt.show()
   
def bieu_do_duong_mean():
   meanYearlySalary = np.array(data['salary_in_usd'].groupby(data['work_year']).mean())
   plt.xlabel('Year')
   plt.ylabel('Mean Salary')
   plt.title("Giá trị trung bình mức lương USD qua các năm")
   sns.lineplot(x=['2020', '2021', '2022', '2023'], y=meanYearlySalary)
   plt.show()

def bieu_do_cot_median():
   data.groupby('work_year')['salary_in_usd'].median().plot.bar()
   plt.xlabel('Year')
   plt.ylabel('Median Salary')
   plt.title('Giá trị trung vị mức lương USD qua các năm ')
   plt.show()

def alltime_top_ten():
   allTimeTopTen = data["job_title"].value_counts().nlargest(10).reset_index()
   sns.barplot(x=allTimeTopTen["job_title"], y=allTimeTopTen["index"])
   plt.title("Tóp 10 công việc Data Scicence phổ biến nhất")
   plt.xlabel("Count")
   plt.ylabel("Job Title")
   plt.show()

def alltime_top_ten_2023():
   topTen2023 = data[data["work_year"]==2023]["job_title"].value_counts().nlargest(10).reset_index()
   sns.barplot(x=topTen2023["job_title"], y=topTen2023["index"])
   plt.title("Tóp 10 công việc Data Scicence phổ biến nhất 2023")
   plt.xlabel("Count")
   plt.ylabel("Job Title")
   plt.show()

def experience_level_vs_work_year():
    # Phân tích năm làm việc và mức độ kinh nghiệm bằng hàm pandas cross-tab
    pd.crosstab(data['work_year'],data['experience_level'], normalize = 'index').plot(kind = 'bar')
    plt.xlabel('Year')
    plt.ylabel('Mật độ xác suất')
    plt.title('Cấp độ kinh nghiệm so với năm làm việc')
    plt.xticks(rotation = 0)
    plt.show()

def bieu_do_remote_ratio():
   sns.histplot(data['remote_ratio'], kde = True)
   plt.xlabel('Remote Ratio')
   plt.ylabel('Mật độ')
   plt.title('Phân phối tỷ lệ từ xa')
   plt.show()

def cap_do_kinh_nghiem():
   fig, ax = plt.subplots()
   sns.countplot(ax = ax, data = data, x = data.experience_level)
   ax.set(xlabel='', ylabel='Counts', title='Cấp độ kinh nghiệm')
   ax.bar_label(ax.containers[0])
   plt.show()
def main():
    bieu_do_tron_experience_level()
    bieu_do_cot_median()
    bieu_do_duong_mean()
    alltime_top_ten()
    alltime_top_ten_2023()
    experience_level_vs_work_year()
   #  bieu_do_remote_ratio()
    cap_do_kinh_nghiem()
if __name__=="__main_":
    main()

# Đặt màu nền và kích thước hình
plt.style.use('dark_background')
plt.figure(figsize = (10, 6))
# tạo biểu đồ
sns.histplot(x = 'salary_in_usd', hue = 'experience_level', multiple = 'stack',
             edgecolor = '#cfd0d4', bins = 50, data = data, palette = 'viridis')

# Tùy chỉnh tiêu đề và nhãn
plt.grid(alpha = 0.3)
plt.title('Phân phối tiền lương (USD) theo kinh nghiệm')
plt.xlabel('Salary')
plt.ylabel('Count')
plt.show()
#lọc dữ liệu
chuong=data.loc[data['job_title']=='Data Scientist']
chuong1=data.loc[data['job_title']=='ML Engineer']
chuong2=data.loc[data['job_title']=='Applied Scientist']
#tính tỷ lệ phần trăm cho mỗi nhóm
sizes=[len(chuong),len(chuong1),len(chuong2)]
# biểu đồ hình tròn phần trăm công việc
my_explode = (0.1,0,0)
my_colors = ['red','orange','silver',]
plt.pie(sizes,labels=['Data Scientist','ML Engineer','Applied Scientist'], explode=my_explode, colors=my_colors, autopct='%.1f%%')
plt.title('Phân bố các vị trí công việc')
plt.show()

# tạo bản thông kê
dieu_kien1=['M','L','S']
quy_mo='company_size'
tan_so1=data[quy_mo].value_counts()
print(data)

#biểu đồ quy mô các công ty
my_colors = ['lightblue','lightsteelblue','silver']
my_explode = (0, 0.1, 0)
plt.pie(tan_so1,labels=dieu_kien1,autopct="%.1f%%",startangle=15,shadow=True,colors=my_colors,explode=my_explode)
plt.title("phân bố quy mô công ty")
plt.axis('equal')
plt.show()

import country_converter as coco
import pandas as pd
import plotly.express as px
rr = data.groupby('company_location')['remote_ratio'].mean().reset_index()
rr['company_location'] =  coco.convert(names = rr['company_location'], to = "ISO3")
rr.head()
fig = px.choropleth(rr,
                    locations = rr.company_location, 
                    color = rr.remote_ratio,                  
                    labels={'company_location':'Quốc gia','remote_ratio':'Tỷ lệ công việc từ xa'})
                    
fig.update_layout(title = "Vị trí công việc từ xa")
fig.show()

