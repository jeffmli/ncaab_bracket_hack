import statsmodels.api as sm
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_Score
import pandas as pd

train_data = pd.read_csv('../Data/test_df.csv')
test_data = pd.read_csv('../Data/train_df.csv')


#
# lm = LinearRegression()
# lm.fit(x_train,y_train)
#
# pred = lm.predict(x_test)
#
# test_rsme = (np.sqrt(mean_squared_error(y_test, pred)))
#
# test_r2 = r2_score(y_test, pred)
#
# print(test_set_rmse)
# print(test_set_r2)
#
