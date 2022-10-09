import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = pd.read_csv('datasets/persona.csv')
df.head()

'''   PRICE   SOURCE   SEX COUNTRY  AGE
0     39  android  male     bra   17
1     39  android  male     bra   17
2     49  android  male     bra   17
3     29  android  male     tur   17
4     49  android  male     tur   17
'''

df['SOURCE'].unique()
df['SOURCE'].nunique()

df['SOURCE'].value_counts()

df['PRICE'].unique()
df['PRICE'].value_counts()

df['COUNTRY'].value_counts()
df.groupby('COUNTRY')['PRICE'].sum()
df.groupby('SOURCE')['PRICE'].count()

'''COUNTRY
bra    51354
can     7730
deu    15485
fra    10177
tur    15689
usa    70225'''

df['SOURCE'].value_counts()
df.groupby('COUNTRY')['PRICE'].mean()

'''COUNTRY
bra   34.32754
can   33.60870
deu   34.03297
fra   33.58746
tur   34.78714
usa   34.00726'''

df.groupby('SOURCE')['PRICE'].mean()
df.groupby(['COUNTRY', 'SOURCE']).agg({'PRICE': 'mean'})

'''                   PRICE
COUNTRY SOURCE          
bra     android 34.38703
        ios     34.22222
can     android 33.33071
        ios     33.95146
deu     android 33.86989
                  ...
fra     ios     32.77622
tur     android 36.22944
        ios     33.27273
usa     android 33.76036
        ios     34.37170'''

agg_df = df.sort_values('PRICE', ascending=False)
agg_df
agg_df.reset_index()
agg_df = agg_df.reset_index()
agg_df
agg_df.drop('index', axis=1, inplace=True)
agg_df
agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"], bins=[0, 18, 23, 30, 40, 66],
                            labels=["0_18", "19_23", "24_30", "31_40", "41_66"])
agg_df.head()

'''   PRICE   SOURCE   SEX COUNTRY  AGE AGE_CAT
0     59      ios  male     fra   15    0_18
1     59  android  male     usa   47   41_66
2     59  android  male     tur   24   24_30
3     59  android  male     fra   15    0_18
4     59      ios  male     bra   16    0_18'''

agg_df.values
agg_df["CUSTOMERS_LEVEL_BASED"] = [str(row[3]).upper() + "_" + str(row[1]).upper() +
                                    "_" + str(row[2]).upper() + "_" + str(row[5]).upper()for row in agg_df.values]

agg_df = agg_df[["CUSTOMERS_LEVEL_BASED","PRICE"]]
agg_df.head()

'''    CUSTOMERS_LEVEL_BASED  PRICE
0       FRA_IOS_MALE_0_18     59
1  USA_ANDROID_MALE_41_66     59
2  TUR_ANDROID_MALE_24_30     59
3   FRA_ANDROID_MALE_0_18     59
4       BRA_IOS_MALE_0_18     59
'''

agg_df = agg_df.groupby("CUSTOMERS_LEVEL_BASED").agg({"PRICE":"mean"}).sort_values("PRICE", ascending=False)
agg_df = agg_df.reset_index()
agg_df.head()

'''      CUSTOMERS_LEVEL_BASED    PRICE
0        TUR_IOS_MALE_24_30 45.00000
1        TUR_IOS_MALE_31_40 42.33333
2  TUR_ANDROID_FEMALE_31_40 41.72727
3    CAN_ANDROID_MALE_19_23 40.11111
4    TUR_ANDROID_MALE_41_66 39.00000'''

agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])
agg_df.head()

'''      CUSTOMERS_LEVEL_BASED    PRICE SEGMENT
0        TUR_IOS_MALE_24_30 45.00000       A
1        TUR_IOS_MALE_31_40 42.33333       A
2  TUR_ANDROID_FEMALE_31_40 41.72727       A
3    CAN_ANDROID_MALE_19_23 40.11111       A
4    TUR_ANDROID_MALE_41_66 39.00000       A'''

agg_df.groupby(["SEGMENT"]).agg({"PRICE": ["min", "max", "mean"]})

'''             min      max     mean
SEGMENT                           
D       19.00000 32.65854 30.11316
C       32.70370 34.00000 33.51284
B       34.05435 35.43939 34.68143
A       35.52174 45.00000 37.54429'''

new_user = "FRA_IOS_FEMALE_31_40"
agg_df[agg_df["CUSTOMERS_LEVEL_BASED"] == new_user]

'''   CUSTOMERS_LEVEL_BASED    PRICE SEGMENT
79  FRA_IOS_FEMALE_31_40 32.75000       C'''

