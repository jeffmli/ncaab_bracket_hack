import pandas as pd
from pandas_profiling import ProfileReport
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from IPython.display import display


class PCAFeatureSelect:
    # """
    # Select top k features that are deemed to be most relevant by applying a PCA approach
    # and examining features that explain the most variance in the overall data
    # """

    def __init__ (self, input_df_wo_nulls:pd.DataFrame):
        # """
        # :input_df_wo_nulls: should be a feature-only dataframe with NO response / target variables
        #     should be void of any null / missing values
        # """
        # added decoder to be used in explained variance in component 1 output
        col_name_decoder = dict(zip(input_df_wo_nulls.columns, range(len(input_df_wo_nulls.columns))))
        self.colnum_to_name_decoder = {v:k for k,v in col_name_decoder.items()}

        # couldn't just dropnas because all rows still have at least one column with an NaN, chose to use simpleimputer
        # and fill NaNs with 0s.
        self.input_df = SimpleImputer(missing_values=np.nan, strategy='constant', fill_value=0).fit_transform(input_df_wo_nulls)
        #self.input_df = input_df_wo_nulls.dropna()
        std_scaler = StandardScaler()
        self.scaled_df = std_scaler.fit_transform(self.input_df)

    def fit_PCA (self, n_components:int=None):
        pca = PCA(n_components=n_components)
        self.model = pca.fit(self.scaled_df)

    def find_num_components (self, explained_variance_threshold:float=0.9):
        # """
        # find the number of components that make up the explained_variance_threshold (e.g. 90%) of the data
        # :explained_variance_threshold: must be a float ranging between 0 and 1
        #     takes the first k PCA components that comprise explained_variance_threshold
        # """
        component_cum_sum = np.cumsum(self.model.explained_variance_ratio_)

        num_components = 0
        for i, expl_var in enumerate(component_cum_sum):
            if expl_var < explained_variance_threshold:
                pass
            else:
                num_components = i
                break
        print(num_components)
        self.num_components = num_components

    def top_variance_explained(self):
        # """
        # find the top variance explained in component one
        # """
        self.top_variance_explained = self.model.explained_variance_ratio_.flat[0]

    def explained_variance_df (self):
        # """
        # create an explained variance dataframe
        # """
        expl_var_df = pd.DataFrame(self.model.components_,
                                   columns=pd.DataFrame(self.scaled_df).columns)

        expl_var_df = expl_var_df.iloc[:self.num_components, :]

        self.explained_variance_df = expl_var_df

    def find_relevant_features_fr_component_n (self, n:int=1):
        # """
        # :n: n-th component
        # :return: relevant feature df listing the column name and the eigenvalue
        # """
        if n > self.explained_variance_df.shape[0]:
            raise ValueError ('You specified an `n` that exceeds the number of PCA components')

        rel_df = pd.DataFrame(self.explained_variance_df.iloc[n].reset_index()).sort_values(by=[1], ascending=False)
        rel_df.columns = ['col_name','eigenval']
        rel_df.sort_values(by='eigenval', ascending=False)
        rel_df['orig_colname'] = rel_df['col_name'].apply(lambda x: self.colnum_to_name_decoder.get(x))

        return rel_df



data = pd.read_csv('../Data/data_by_game.csv')
print(data.columns)
keeps = ['Season', 'DayNum', 'WTeamID', 'WScore', 'LTeamID',
'LScore', 'NumOT', 'WFGM', 'WFGA', 'WFGM3', 'WFGA3', 'WFTM',
'WFTA', 'WOR', 'WDR', 'WAst', 'WTO', 'WStl', 'WBlk', 'WPF', 'LFGM',
'LFGA', 'LFGM3', 'LFGA3', 'LFTM', 'LFTA', 'LOR', 'LDR', 'LAst', 'LTO',
'LStl', 'LBlk', 'LPF', 'w_TeamID']

data_clean = data[keeps].copy()
# print(data_clean)
# pca = PCA()
# pca.fit(data)

# display(pca.components_)

# data_PCA = PCA(n_components=16)
# data_PCA.fit(data_clean)
# display(data_PCA.components_)
# display(data_PCA.explained_variance_ratio_.flat[0])

data_PCA = PCAFeatureSelect(data_clean)

data_PCA.fit_PCA()
n_components = data_PCA.find_num_components()
data_PCA.fit_PCA(5)

print(data_PCA.top_variance_explained())
print(data_PCA.explained_variance_df())
print(n_components)

highest_var_explained_in_columns = data_PCA.find_relevant_features_fr_component_n()
print(highest_var_explained_in_columns.orig_colnama == 'WFGM3')

years = data_clean.Season.unique()
print(years)

df = {}

# for i in years:
#     df.season.append(i)
#     include = data_clean[data_clean['Season'] == i]
#     pca = PCAFeatureSelect(include)
#     pca.fit_PCA()
