# Week 3: Customer Segmentation

This is my report for my work on the week 3 task.

## Importing Libraries and Dataset

I have used the 'Online Shopping Dataset' dataset for my work which can be found on the below link.

Link : [https://www.kaggle.com/datasets/jacksondivakarr/online-shopping-dataset/data](https://www.kaggle.com/datasets/jacksondivakarr/online-shopping-dataset/data)

## About the Dataset

| Features | Description        |
| :------- | :----------------- |
|CustomerID| Unique identifier for each customer.|
|Gender|Gender of the customer (e.g., Male, Female).|
|Location|Location or address information of the customer.|
|Tenure_Months|Number of months the customer has been associated with the platform.|
|Transaction_ID|Unique identifier for each transaction.|
|Transaction_Date|Date of the transaction.|
|Product_SKU|Stock Keeping Unit (SKU) identifier for the product.|
|Product_Description|Description of the product.|
|Product_Category|Category to which the product belongs.|
|Quantity|Quantity of the product purchased in the transaction.|
|Avg_Price|Average price of the product.|
|Delivery_Charges|Charges associated with the delivery of the product.|
|Coupon_Status|Status of the coupon associated with the transaction.|
|GST|Goods and Services Tax associated with the transaction.|
|Date|Date of the transaction (potentially redundant with Transaction_Date).|
|Offline_Spend|Amount spent offline by the customer.|
|Online_Spend|Amount spent online by the customer.|
|Month|Month of the transaction.|
|Coupon_Code|Code associated with a coupon, if applicable.|
|Discount_pct|Percentage of discount applied to the transaction.|

## Data Handling

### Coupon and Discount

1. Checking for missing values: Found that there are very few missing data, so decided to drop them. And deleted the duplicate data (if present).

2. After dropping such values, there were missing values in Coupon_Code and Discount_pct. So I decided to check on them.

3. I found that the null values in both the column were together. So I decided to first fill them with the mode values of the columns and them adjusted them according to the Coupon_Status.

4. Coupon_Status such as 'Clicked' and 'Not Used' have no discount used on them. So i replaced them with 'None' in Coupon_Code and 0 in Discount_pct.

5. There were number mentioned in the coupon_code. So I checked them with the discount_pct by creating a new column of Coupon_Number and matched it with the Discount_pct.</br>
I found that the number was the discount percentage.

6. I also the name of the coupon and added it to Coupon_Name column.

## Exploratory Data Analysis (EDA)

First, dropped the useless columns like 'Unnamed 0:' and 'Product SKU'.

### 1. Location</br>

Plotted the count of customers from each country.</br>
Found that the customers were only from five countries with maximum from California and minumum from Wasington DC.

### 2. Gender </br>

Plotted the count of customers of each gender</br>
Found that the number of female customers were more than that of male.

### 3. Tenure months</br>

Plotted the number of customers corresponding to each months.
Found that the number varied too much.</br>
All the customers have single tenure months, showing the data is well updated.

### 4. Average delivery charge per location </br>

Found that New Jersey has the minimum delivery cost while California and New York has the highest.

### 5. Coupon Status</br>

Checked number of customers corresponding to each coupon status.</br>

1. Found that the number was more or less equally distributed, highest for 'Used' and minimum for 'Not Used'.</br>

2. The 'Clicked' status is also very high, showing that many customers are interested in coupon. So I checked for the number on the Coupon.</br>

3. Found that high number of customers have clicked on coupons with name 'Sale', 'OFF', 'ELEC', 'Extra' showing it caught interest of the customers.</br>

4. Other coupons have very less customers using them, showing that it showed be presented more.

### 6. Product Category</br>

Plotted number of customers corresponding to each category.</br>

#### Observations

1. Office Products are in high demand.
2. Products like Backpacks, android, gift cards, more bags have no almost no sales.
3. Accessories, Bottles, Fun, Google,Housewares,Nest, Waze have very less sales.

## Data Preprocessing

1. I have created new columns on the basis of Product_Categories. And added all the amount paid for that product by a customer. I have also created a new column called Total_amt_paid which has the value of total amt paid by the customer.

2. I have also created average columns for Offline_paid, Online_paid, GST, Discount_pct.

3. Binary encoding of Gender and one-hot encoding of Location is done.

4. Scalling of the data is done using StandardScalar.

## Clustering</br>

1. I performed PCA for understanding variance of each principal conponent.

2. I performed Elbow Method and calulated the Silhuoette Sscore for finding the optimal number of clusters for my dataset.

3. From Elbow method, I found the optimal number of clusters to be 3.

4. I also performed DBSCAN, but it showed only one clusters at any value of eps.

5. Finally, I performed KMeans for clustering on my data and plotted on 3D graph after PCA.
