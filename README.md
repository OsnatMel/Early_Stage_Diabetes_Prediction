# Early_Stage_Diabetes_Prediction

## Introduction
This project aim to demonstrate addressing labeled structured dataset, from initial assesment of the data till training (with hyperparameters tuning) and feature importance measuring.

The dataset is the diabetes_data_upload.csv file, which was taken from the next link:
https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset

## Projects steps

### Importing Data
Import dataset in csv format to pandas dataframe.

### EDA
Conducting basic exploratory data analysis in order to have am initial understanding on data quality and integrity.  
The following charecterizations of the data are explored by a function (EDA.py)- data types, missing data and the informativeness per column.
![EDA_Results_](https://github.com/OsnatMel/Early_Stage_Diabetes_Prediction/blob/master/ImagesForSummary/EDA_Results.PNG)
- The column 'Age' is the numeric column in the dataset so describe function returns results on it.
- All other Y/N columns were examined with regards to the balance between the values, especially to see that the columns are informative or balanced (in the classification column).

Balance between the classes was examined: <br />
![Classes_Histogram_](https://github.com/OsnatMel/Early_Stage_Diabetes_Prediction/blob/master/ImagesForSummary/Classes_Histogram.png)

Distribution of ages between the two classes: <br />
![Age_D_](https://github.com/OsnatMel/Early_Stage_Diabetes_Prediction/blob/master/ImagesForSummary/Age_D.PNG)

### Preprocessing
Even though in the tested dataset there's no missing data, as a step a function to replace nulls is run. 

In addition, there's only one numeric column 'Age' and the data  in it is binned via the function 'Data_Binning'. 
![Age_Categories_](https://github.com/OsnatMel/Early_Stage_Diabetes_Prediction/blob/master/ImagesForSummary/Age_Categories.PNG)

As preparation for training models, the string values are replaced by a numeric values by a function.
![Data_Textual_Desc_](https://github.com/OsnatMel/Early_Stage_Diabetes_Prediction/blob/master/ImagesForSummary/Data_Textual_Desc.PNG)

![Data_Numeric_Coding_](https://github.com/OsnatMel/Early_Stage_Diabetes_Prediction/blob/master/ImagesForSummary/Data_Numeric_Coding.PNG)

All of the functions are listed in Preprocessing.py file.

### Models
Two models were chosen for the specific dataset - Naive Bayes and Random Forest, with metrics to test their results.

Random forest modeling was explored further by:
- hyperparameter tuning with GridSearch 
- comparing metrics between the models
- comparing feature importance, either by RandomForestClassifier.feature_importances_ attribute and by Boruta.

##### Two GridSearch were conducted, both held these parameters:
    'bootstrap': [True],
    'max_depth': [2, 4, 6, 8],
    'min_samples_leaf': [3, 4, 5],
    'min_samples_split': [8, 10, 12],
    'n_estimators': [10, 20, 30]

But the difference between was with 'max_features' parameter:
* [2, 3]
* ['auto','log2']

#### Models' metrics comparison

The metrics were mostly improving from model to model, as follow:

| Model| Accuracy| Precision|Recall|
| :--- | :--- | :--- | :--- |
| Naïve Bayes| 91.54% | 92.94% | 94.05% |
| Random Forest| 88.46%| 87.91%| 95.24% |
| Random Forest best_estimator - numeric max_features   | 96.15%| 97.59%| 96.43%|
| Random Forest best_estimator - auto as max_features     | 96.92% | 100% | 95.24%|

##### Comparing the different models shows that the best model was with the next parameters:
    'bootstrap': True,
     'max_depth': 8,
     'max_features': 'auto',
     'min_samples_leaf': 4,
     'min_samples_split': 8,
     'n_estimators': 10

#### Features Importance:

Comparing between the models and with boruta, reveal that top 3 features are Polyuria (excessive urination volume), Polydipsia (excessive thirst) and Gender.

![Features_Importance_](https://github.com/OsnatMel/Early_Stage_Diabetes_Prediction/blob/master/ImagesForSummary/Features_Importance.PNG)
