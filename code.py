# --------------
# Import the required Libraries
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import calendar
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# Generate a line chart that visualizes the readings in the months

def line_chart(df,period,col):
    df[period] = pd.to_datetime(df[period])
    comp = df.pivot_table(values=[col], index=df[period].dt.month, aggfunc='mean')
    plt.plot(comp.index, comp[col], color='blue')
    plt.show()
    """ A line chart that visualizes the readings in the months
    
    This function accepts the dataframe df ,period(day/month/year) and col(feature), which plots the aggregated value of the feature based on the periods. Ensure the period labels are properly named.
    
    Keyword arguments:
    df - Pandas dataframe which has the data.
    period - Period of time over which you want to aggregate the data
    col - Feature of the dataframe
    
    """
    
    







# Function to perform univariate analysis of categorical columns
def plot_categorical_columns(df):
        for i in df.select_dtypes(include='object').columns.tolist():
                plt.figure(figsize=(20,7))
                df[i].value_counts().plot(kind='bar')
                plt.show()
    
    








# Function to plot continous plots
def plot_cont(df,plt_typ):
        for i in df.select_dtypes(include=np.number).columns.tolist():
            df[i].plot(kind=plt_typ)
            plt.show()
   
    
    







# Function to plot grouped values based on the feature
def group_values(df,col1,agg1,col2):
    df.groupby(col1).agg1()
    df.plot(kind="bar",x=df[col2], y=df[col1])
    plt.show()
    """ Agrregate values by grouping
    
    This function accepts a dataframe, 2 column(feature) and aggregated function(agg1) which groupby the dataframe based on the column and plots the bar plot.
   
    Keyword arguments:
    df - Pandas dataframe which has the data.
    col1 - Feature of the dataframe on which values will be aggregated.
    agg1 - Dictionary of aggregate functions with feature as the key and func as the value
    col2 - Feature of the dataframe to be plot against grouped data.
    
    Returns:
    grouping - Dataframe with all columns on which it is grouped on.
    """
    
    




# Read the Data and pass the parameter as parse_dates=True, index_col='Date/Time'
weather_df = pd.read_csv(path,index_col='Date/Time' ,parse_dates = True)
df =  pd.read_csv(path,parse_dates = True)
print(weather_df.shape)
# Lets try to generate a line chart that visualizes the temperature readings in the months.
# Call the function line_chart() with the appropriate parameters.
line_chart(df, "Date/Time", "Temp (C)")

# Now let's perform the univariate analysis of categorical features.
# Call the "function plot_categorical_columns()" with appropriate parameters.

plot_categorical_columns(df)
    

# Let's plot the Univariate analysis of Numerical columns.
# Call the function "plot_cont()" with the appropriate parameters to plot distplot



# Call the function "plot_cont()" with the appropriate parameters to plot boxplot


# Groupby the data by Weather and plot the graph of the mean visibility during different weathers. Call the function group_values to plot the graph.
# Feel free to try on diffrent features and aggregated functions like max, min.




