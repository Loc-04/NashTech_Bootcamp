-- 1. Dim_Date: Sử dụng Smart Key, không Identity
CREATE TABLE Dim_Date (
    Date_Key INT PRIMARY KEY, -- Smart Key: 20240130. KHÔNG để Identity.
    Full_Date DATE NOT NULL,  -- Cột này để hiển thị lên báo cáo (30-01-2024)
    Day_Of_Week NVARCHAR(10) NOT NULL, -- 'Monday', 'Tuesday'...
    Day_Of_Month INT NOT NULL, -- 1-31
    Month INT NOT NULL, -- 1-12
    Quarter INT NOT NULL, -- 1-4
    Year INT NOT NULL
);

-- 2. Dim_Customer: Giữ Surrogate Key và Business Key
CREATE TABLE Dim_Customer (
    Customer_Key INT IDENTITY(1,1) PRIMARY KEY, -- Surrogate Key (Nội bộ DW)
    Customer_Source_ID VARCHAR(50) NOT NULL,    -- Business Key (Map với Source ERP)
    Customer_Name NVARCHAR(255) NOT NULL,
    City NVARCHAR(100),
    Phone VARCHAR(50)
);

-- 3. Dim_Product
CREATE TABLE Dim_Product (
    Product_Key INT IDENTITY(1,1) PRIMARY KEY,
    Product_Source_ID VARCHAR(50) NOT NULL,
    Product_Name NVARCHAR(255) NOT NULL,
    Category NVARCHAR(100) NOT NULL,
    Brand NVARCHAR(100)
);

-- 4. Fact_Sales: Granularity thấp nhất (Atomic)
CREATE TABLE Fact_Sales (
    Sales_Key INT IDENTITY(1,1) PRIMARY KEY, -- Optional, thường dùng Composite Key
    Date_Key INT NOT NULL,      -- Foreign Key tới Dim_Date
    Customer_Key INT NOT NULL,  -- Foreign Key tới Dim_Customer
    Product_Key INT NOT NULL,   -- Foreign Key tới Dim_Product

    -- Measures (Các chỉ số cần tính toán)
    Quantity INT NOT NULL,
    Unit_Price DECIMAL(18,2) NOT NULL,
    Total_Amount DECIMAL(18,2) NOT NULL, -- Thường tính sẵn để query nhanh hơn

    -- Metadata
    Load_Date DATETIME DEFAULT GETDATE(),

    -- Constraints
    CONSTRAINT FK_Fact_Date FOREIGN KEY (Date_Key) REFERENCES Dim_Date(Date_Key),
    CONSTRAINT FK_Fact_Customer FOREIGN KEY (Customer_Key) REFERENCES Dim_Customer(Customer_Key),
    CONSTRAINT FK_Fact_Product FOREIGN KEY (Product_Key) REFERENCES Dim_Product(Product_Key)
);