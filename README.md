# SRH-Spaceship-Titanic-ML

Description:

Original data (spaceship_titanic.csv)

- PassengerId - A unique Id for each passenger. Each Id takes the form gggg_pp where gggg indicates a group the passenger is travelling with and pp is their number within the group. People in a group are often family members, but not always.
- HomePlanet - The planet the passenger departed from, typically their planet of permanent residence.
- CryoSleep - Indicates whether the passenger elected to be put into suspended animation for the duration of the voyage. Passengers in cryosleep are confined to their cabins.
- Cabin - The cabin number where the passenger is staying. Takes the form deck/num/side, where side can be either P for Port or S for Starboard.
- Destination - The planet the passenger will be debarking to.
- Age - The age of the passenger.
- VIP - Whether the passenger has paid for special VIP service during the voyage.
- RoomService, FoodCourt, ShoppingMall, Spa, VRDeck - Amount the passenger has billed at each of the Spaceship Titanic's many luxury amenities.
- Name - The first and last names of the passenger.
- Transported - Whether the passenger was transported to another dimension. This is the target, the column you are trying to predict.



### Steps:
#### 1. Data Extract

A new dataset was created (spaceship_titanic_e.csv) which contains additional columns:
- GroupId - Id of a group in which a passenger is travelling
- PassengerIdInGroup - Id of a passenger inside a group
- MembersOfGroupById - Number of passengers in a group with the same id
- Surname - Surname of a passenger
- MembersOfFamilyBySurname - Suggested number of family members calculated from surname
- CabinDeck - Deck of cabin
- CabinNum - Number of cabin
- CabinSide - Side of cabin
- AgeBinned - Binned Age (Child, Teenager, Young, Senior, Elder)

#### 2. EDA:
First I think we must drop the columns which for sure not relevant to our target. These columns would be:
- PassengerId - No useful information here, I have already extracted the ids 
- Cabin - Again, nothing useful, as I have already extracted the Deck, Number and Side from this column
- Name - I extracted surname which is the only relevant information here
- GroupId - This column was generated from PassengerId and was used to calculate the number of passenger in the same group. The id itself (number) is useless
- PassengerIdInGroup - Same as GroupId
- Surname - Was used to calculate the number of passenger with the same surname. I don't think the surname is useful

For plotting the data I suggest plotly library, it is easy and generates interactive plot, the documentation can be found here:
https://plotly.com/python/, also a greate resource for plotting: https://python-graph-gallery.com/

Then we need to draw a number of plots, the useful ones could be:
1. Investigate the target (Transported), bar plot to look at the numbers to see if there is any disbalance (I have looked there is none)
2. Investigate nans: bar plot to look at the amount of nan values in each column (better to use relative values)
3. Check outliers: box plots for every numerical column
4. Check categorical data: bar plots to check the count of each category in the categorical column. (better to use relative values). 
If the number objects  of a specific category is very low then it could be better to merge this category with another. Also, plot
a table for each categorical columns compared to target for example how many passengers transported for each destination.
5. Check correlation: heatmap
6. Plot the scattermatrix of all numeric columns

#### 3. Feature Engineering

First of all we must tend to nans and outliers. For each numerical column we must see if there are any obvious outliers.
The general rule might be if the value is out of the borders [mean - 5std, mean + 5std] it can be an outlier. 

If there are
no obvious outliers then we can fill the nans with mean values, otherwise with median values. For categories if there are nan 
values we can fill them with a new category 'Unknown'.

Then, we must replace the outliers. If you see that the value is an obvious outlier, you can replace them with mean plus or minus 5 standard errors.

The next step is to do One-Hot-Encoding for each categorical column. Do not forget to drop the original column after transformation


#### 4. Feature Selection

I will use such methods as permutation importance and greedy selection to select the features to pass to model. You
can read about it in the scikit-learn documentation.
The output will be the names of features to use in the next step.

#### 5. Modeling

I suggest to use CatBoost https://catboost.ai/en/docs/ (CatBoostClassifier) or LightGBM https://lightgbm.readthedocs.io/en/stable/ 
(LightGBMClassifier) model. It is compatible with sklearn interface and is considered the state-of-the-art
for such kind of data.

Here there are a number of steps. The first one is to split data in two parts: training-validation set and test set.
The reason why we call it train-validation set is that we want to use cross-validation technique. So, we put test data
aside until the very end of modeling (model evaluation). The good amount of test data would be 20%. Do not forget to use random_state!

*optinal step: scaling. But I think it can be not that easy if you are new to sklearn. That is because in this case you will
have to create a Pipeline (which is a scaler and a model in one object) because the scaler must be fit only to the training data
and it is tricky to use cross-validation with scaler manually. The good thing is that tree-based models such as gradient boosting
are not sensitive to scaling*

The second step is to adjust the hyperparameters of the model. My suggestion is to use GridSearchCV. It will use the cross-validation
to adjust the hyperparameters in the best way possible. 
https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html. Do not forget to use train-validation set for this.
My suggestion for hyperparameters of gradient boosting:
- n_estimators (or equal to that): 30, 50, 100, 200, 300, 400, 500, 600, 700
- max_depth (or equal): 3, 4, 5, 6, 7, 8
- colsample_bytree (or colample_bylevel): 0.7, 0.8, 0.9, 1
- num_leaves (or equal to that): 21, 31, 41, 51, 61, 71, 81

** Good choice of metric for this type of problem is f1-score. You can use it in gridsearch and in model evaluation **

Then, it is time to train the model with the best hyperparameters.

#### 6. Model Evaluation

1. Calculate predictions for the test dataset
2. Calculate metrics for the predictions (accuracy, f1-score, precision, recall)
3. Create a confusion matrix
4. Compare our result with the dummy model (the dummy model accuracy should be 0.5)
5. Optional: if you are good at it, you can plot ROC-AUC plot which is very useful in understanding the result.
6. Try to come up with some statistics of where we did the most number of mistakes (maybe it is some specific category of something else)
