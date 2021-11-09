model.csv -> model_cleaned.csv
*Changes*

* Map target column with binary encoding {satisfied: 1, not satisfied:0}
* Filled NaN values with mean of cluster (gender, customer type)
* Deleted wrong customer ID
* Deleted ID column



model_cleaned.csv -> selected_features.csv

*Changes*

* Log transformation and correlation test for numerical variables
* Chi square test and one hot encoding for categorical variables



selected_features.csv -> final.csv

* Standard scaler for numerical variables



final.csv -> final_down.csv

* Downsampling of target variables zeros
