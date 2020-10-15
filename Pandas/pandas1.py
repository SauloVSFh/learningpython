#Kaggle course for pandas
import pandas as pd

                                            #DataFrame

#class pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
# fruits = pd.DataFrame({"Apples":[30], "Bananas":[21]})

# fruit_sales = pd.DataFrame([[35, 21], [41, 34]], columns=['Apples', 'Bananas'], index=['2017 Sales', '2018 Sales'])
# print(fruit_sales)


                                            #Series

#class pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
# ingredients = pd.Series(['4 cups','1 cup', '2 large','1 can'], index = ['Flour','Milk','Eggs','Spam'],name="Dinner")
# print(ingredients)


                                            #read_csv

# pandas.read_csv(filepath_or_buffer, sep=',', delimiter=None, header='infer',
# names=None, index_col=None, usecols=None, squeeze=False, prefix=None,
# mangle_dupe_cols=True, dtype=None, engine=None, converters=None,
# true_values=None, false_values=None, skipinitialspace=False, skiprows=None,
# skipfooter=0, nrows=None, na_values=None, keep_default_na=True, na_filter=True,
# verbose=False, skip_blank_lines=True, parse_dates=False, infer_datetime_format=False,
#  keep_date_col=False, date_parser=None, dayfirst=False, cache_dates=True,
#  iterator=False, chunksize=None, compression='infer', thousands=None, decimal='.',
#  lineterminator=None, quotechar='"', quoting=0, doublequote=True, escapechar=None,
#  comment=None, encoding=None, dialect=None, error_bad_lines=True, warn_bad_lines=True,
#  delim_whitespace=False, low_memory=True, memory_map=False, float_precision=None)

# animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])


                                            #to_csv

# animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
# animals.to_csv('cows_and_goats.csv')


                                            #set_index

df = pd.DataFrame({'Amount':[1,17,20,21],'Fruits':['Apples','Oranges','Melon','Apples']})
# df = df.set_index("Fruits")
# print(df)

                                            #conditional selection

# print(df.loc[(df.Fruits == 'Apples')])
# print(df.loc[(df.Fruits == 'Apples') & (df.Amount == 21)]) #and -> the best to use two conditions
# print(df.loc[(df.Fruits == 'Apples') | (df.Amount == 21)]) #or


                                            #Built-in conditional selectors

# print(df.loc[(df.Fruits == 'Apples') | (df.Fruits == "Oranges")]) #selecting more than one argument
# print(df.loc[df.Fruits.isin(['Apples','Oranges'])]) #this way you can pass in a list. The best to match more than one
# print(df.loc[df.Fruits.notnull()])
# print(df.loc[df.Fruits.isnull()])
# top_oceania_wines = reviews.loc[(reviews.country.isin(['Australia','New Zealand'])) & (reviews.points >= 95)]
