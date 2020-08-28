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
Also the balance between the classes is observed.

### Preprocessing
Even though in the tested dataset there's no missing data, as a step a function to replace nulls is run.
In addition, there's only one numeric column 'Age' and the data  in it is binned via the function 'Data_Binning'.
As preparation for training models, the string values are replaced by a numeric values by a function.
All of the functions are listed in Preprocessing.py file.

### Models
Two models were chosen for the specific dataset - Naive Bayes and Random Forest, with metrics to test their results.

Random forest modeling was explored further by:
- hyperparameter tuning with GridSearch 
- comparing metrics between the models
- comparing feature importance, either by RandomForestClassifier.feature_importances_ attribute and by Boruta.
