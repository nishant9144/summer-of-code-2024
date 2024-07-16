# Week 1: Fraud Detection System

This is my report for assignment of first week.

## Installing Kaggle

I installed the kaggle in my colab for importing the dataset directly from Kaggle website. This required my 'kaggle.json' for allowing Colab to do so.</br>

## Importing Libraries and Dataset

I imported the necessary libraries for data reading, model training, evaluation and curve plotting.

I downloaded the following dataset with the link given below.</br>

Link: [https://www.kaggle.com/datasets/jainilcoder/online-payment-fraud-detection](https://www.kaggle.com/datasets/jainilcoder/online-payment-fraud-detection)

## About the dataset

| Features | Description |
| :------- | :---------- |
|step | represents a unit of time where 1 step equals 1 hour|
|type| type of online transaction|
|amount| the amount of the transaction|
|nameOrig| customer starting the transaction|
|oldbalanceOrg| balance before the transaction|
|newbalanceOrig| balance after the transaction|
|nameDest| recipient of the transaction|
|oldbalanceDest| recipient balance before the transaction|
|newbalanceDest| recipient balance after the transaction|
|isFraud| identifies a fraudulent transaction (1) and non fraudulent transaction (0)|

## Exploring the dataset

1. I explored the data, like datatypes of features and decided to drop some features like 'isFlaggedFraud', 'nameOrig', 'nameDest' as they show now relation to my data for training.

2. I decided to remove the duplicate values and drop the data with null values as they were very few of them.

3. I checked the transaction type to find which is used most for Fraud.</br>
I found that Cash_Out was the most used.

4. Decided to find correlation between features and drop columns which are related to each other more than 90% as they may cause Overfitting.</br>
For this purpose, I used the "Correlation Matrix" .</br>
Found that 'oldbalanceOrg', 'oldbalanceDest' were too much correlated so I dropped them.

## Data Preprocessing

1. After exploring the whole data, I one-hot encoded the 'type' column and splitted the data into training data, cross-validation data and testing data.</br>
I did so using the "test_train_split".

2. I scaled the data using "StandardScalar".

## Training of Models

After training the model, I calculated the accuracy_score, confussion matrix, error on training set and cross validation set. I also plotted the ROC-AUC curve.

### 1. Logistic Regression

Found that the model performs well and it does not everfit.

### 2. Random Forest Classifier

Found that the model overfits. So i performed RandomSearchCV for tuning the hyperparameters of the model.

### 3. XGBoost

Found that this model works best and it does not overfit.

### 4. LGBM

This model worked OK and it did not overfit over the data.

### 5. Neural Network

This model did not performed good on our dataset.

#### 6. SVM

As the dataset is very large, SVM will not be a good choice for our model as it works very slow. It is one of the best model for small to moderate sized dataset.

## Conclusion

After training all the model, I found that XGBoost model worked best for my dataset.
