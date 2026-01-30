import pandas as pd
import random
from faker import Faker
from sqlalchemy import create_engine

# 1. Setup Connection (Tự tìm hiểu Connection String cho máy em)
# Lưu ý: Server name thường là 'localhost' hoặc '.\SQLEXPRESS'
SERVER = 'localhost'
DATABASE = 'Module_2'
DRIVER = 'ODBC Driver 17 for SQL Server'
connection_string = f'mssql+pyodbc://@{SERVER}/{DATABASE}?driver={DRIVER}&trusted_connection=yes'
engine = create_engine(connection_string)

# 2. Generate Dim_Customer Data
fake = Faker()
customers = []
for _ in range(50):
    customers.append({
        "Customer_Source_ID": fake.uuid4(),
        "Customer_Name": fake.name(),
        "City": fake.city(),
        "Phone": fake.phone_number()
        # ... điền nốt các cột khác
    })
df_customers = pd.DataFrame(customers)

# 3. Load to SQL Server
# if_exists='append': Thêm vào đuôi, không xóa bảng cũ
# index=False: Không insert cái index của DataFrame vào
try:
    df_customers.to_sql('Dim_Customer', con=engine, if_exists='append', index=False)
    print("Success: Loaded Dim_Customer")
except Exception as e:
    print(f"Error: {e}")

# ... (Làm tương tự cho Product, Date và Fact_Sales)

#Cho product, thì mình nên có 1 số dữ liệu nhất định thay vì toàn dummy data, sẽ hợp lí hơn, ví dụ

# Thay vì dùng faker cho mọi thứ, hãy tự định nghĩa để dữ liệu có nghĩa hơn
sample_brands = ["Apple", "Samsung", "Sony", "Dell", "HP"]
sample_categories = ["Electronics", "Smartphones", "Laptops", "Accessories"]
sample_products_base = ["iPhone", "Galaxy", "Xperia", "Inspiron", "Spectre", "Macbook"]

products = []
for _ in range(100):
    products.append({
        "Product_Source_ID" : fake.uuid4(),
        "Product_name" : f"{random.choice(sample_brands)} {random.choice(sample_products_base)}",
        "category" : random.choice(sample_categories),
        "Brand" : random.choice(sample_brands)
    })

df_products = pd.DataFrame(products)

try:
    df_products.to_sql('Dim_Product', con=engine, if_exists='append', index=False)
    print("Success: Loaded Dim_Product")
except Exception as e:
    print(f"Error: {e}")


# pd.date_range sẽ tạo ra một danh sách các ngày liên tục
date_range = pd.date_range(start="2023-01-01", end="2025-12-31", freq="D") # freq="D" là tần suất theo ngày (Day)

df_dates = pd.DataFrame(date_range, columns=['Full_Date'])


df_dates['Date_Key'] = df_dates['Full_Date'].dt.strftime('%Y%m%d').astype(int) # Smart Key: 20230101
df_dates['Day_Of_Week'] = df_dates['Full_Date'].dt.day_name() # 'Monday', 'Tuesday'...
df_dates['Day_Of_Month'] = df_dates['Full_Date'].dt.day
df_dates['Month'] = df_dates['Full_Date'].dt.month
df_dates['Quarter'] = df_dates['Full_Date'].dt.quarter
df_dates['Year'] = df_dates['Full_Date'].dt.year

try:
    df_dates.to_sql('Dim_Date', con=engine, if_exists='append', index=False)
    print("Success: Loaded Dim_Date")
except Exception as e:
    print(f"Error: {e}")


#Dồn dữ liệu vào fact table

# Dùng pandas để chạy câu lệnh SELECT và lấy kết quả
customer_keys_df = pd.read_sql("SELECT Customer_Key FROM Dim_Customer", engine)
product_keys_df = pd.read_sql("SELECT Product_Key FROM Dim_Product", engine)
date_keys_df = pd.read_sql("SELECT Date_Key FROM Dim_Date", engine)

# Chuyển các cột DataFrame này thành list để dễ dùng
customer_key_list = customer_keys_df['Customer_Key'].tolist()
product_key_list = product_keys_df['Product_Key'].tolist()
date_key_list = date_keys_df['Date_Key'].tolist()

# Tạo dữ liệu cho Fact_Sales
sales_records = []

for _ in range(10000):
    quantity = random.randint(1, 5)
    unit_price = round(random.uniform(10.0, 2000.0), 2)

    a_sale = {
        "Date_Key": random.choice(date_key_list),
        "Customer_Key": random.choice(customer_key_list),
        "Product_Key": random.choice(product_key_list),
        "Quantity": quantity,
        "Unit_Price": unit_price,
        "Total_Amount": quantity * unit_price
    }
    sales_records.append(a_sale)

# Chuyển thành DataFrame SAU KHI đã tạo hết 10000 bản ghi, dùng chunksize 1000 để chia nhỏ gói tin, tăng tốc giảm tải
df_sales = pd.DataFrame(sales_records)

try:
    df_sales.to_sql('Fact_Sales', con=engine, if_exists='append', index=False, chunksize=1000)
    print("Success: Loaded Fact_Sales")
except Exception as e:
    print(f"Error: {e}")