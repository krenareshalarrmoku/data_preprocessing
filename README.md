# Pergaditja dhe vizualizimi i te dhenave per datasetin e shpenzimeve te studenteve

# Faza 1

Fillimisht fillojme me mbledhjen e te dhanave, ne rastin tone i marrim nga kaggle permes API call the i ruajme ne /data/student_spending.csv

Vazhdojme me analizimin e kualitetit te te dhenave

Head
   Unnamed: 0  age  ... miscellaneous preferred_payment_method
0           0   19  ...            72        Credit/Debit Card
1           1   24  ...            68        Credit/Debit Card
2           2   24  ...           133                     Cash
3           3   23  ...            55       Mobile Payment App
4           4   20  ...           104        Credit/Debit Card

[5 rows x 18 columns]

## Detektimi i tipit te te dhanve
RangeIndex: 1000 entries, 0 to 999
Data columns (total 18 columns):
 ~   Column                    Non-Null Count  Dtype 
---  ------                    --------------  ----- 
 0   Unnamed: 0                1000 non-null   int64 
 1   age                       1000 non-null   int64 
 2   gender                    1000 non-null   object
 3   year_in_school            1000 non-null   object
 4   major                     1000 non-null   object
 5   monthly_income            1000 non-null   int64 
 6   financial_aid             1000 non-null   int64 
 7   tuition                   1000 non-null   int64 
 8   housing                   1000 non-null   int64 
 9   food                      1000 non-null   int64 
 10  transportation            1000 non-null   int64 
 11  books_supplies            1000 non-null   int64 
 12  entertainment             1000 non-null   int64 
 13  personal_care             1000 non-null   int64 
 14  technology                1000 non-null   int64 
 15  health_wellness           1000 non-null   int64 
 16  miscellaneous             1000 non-null   int64 
 17  preferred_payment_method  1000 non-null   object
dtypes: int64(14), object(4)
memory usage: 140.8+ KB
None

## Pershkrimi i te dhanve duke logarite mesataren medianen dhe vlerat tjera si me poshte

                  count      mean         std  ...     50%      75%     max
Unnamed: 0       1000.0   499.500  288.819436  ...   499.5   749.25   999.0
age              1000.0    21.675    2.322664  ...    22.0    24.00    25.0
monthly_income   1000.0  1020.650  293.841161  ...  1021.0  1288.25  1500.0
financial_aid    1000.0   504.771  287.092575  ...   513.0   751.50  1000.0
tuition          1000.0  4520.395  860.657944  ...  4547.5  5285.00  6000.0
housing          1000.0   696.006  171.218620  ...   704.5   837.25  1000.0
food             1000.0   252.642   86.949606  ...   255.0   330.00   400.0
transportation   1000.0   124.637   43.557990  ...   123.0   162.25   200.0
books_supplies   1000.0   174.761   72.404518  ...   175.0   238.00   300.0
entertainment    1000.0    84.814   37.970451  ...    86.0   116.00   150.0
personal_care    1000.0    60.699   22.898007  ...    62.0    80.00   100.0
technology       1000.0   178.304   71.744441  ...   178.0   241.00   300.0
health_wellness  1000.0   114.310   49.591544  ...   115.0   158.00   200.0
miscellaneous    1000.0   108.910   52.412221  ...   110.0   153.00   200.0

[14 rows x 8 columns]

## Identifikimi dhe trajtimi i vlerave Null, ne rastin tone nuk kemi asnje te tille por megjithate kodi per largimin e tyre eshte prezent
Unnamed: 0                  0
age                         0
gender                      0
year_in_school              0
major                       0
monthly_income              0
financial_aid               0
tuition                     0
housing                     0
food                        0
transportation              0
books_supplies              0
entertainment               0
personal_care               0
technology                  0
health_wellness             0
miscellaneous               0
preferred_payment_method    0
dtype: int64


## Reduktimi i kolones se pare te datasetit pasi nuk ofron ndonje info me kuptim
   age      gender  ... miscellaneous preferred_payment_method
0   19  Non-binary  ...            72        Credit/Debit Card
1   24      Female  ...            68        Credit/Debit Card

[2 rows x 17 columns]


## Definimi i tipit te te dhenave me ndihmen e python
age                          int64
gender                      object
year_in_school              object
major                       object
monthly_income               int64
financial_aid                int64
tuition                      int64
housing                      int64
food                         int64
transportation               int64
books_supplies               int64
entertainment                int64
personal_care                int64
technology                   int64
health_wellness              int64
miscellaneous                int64
preferred_payment_method    object
dtype: object


## Categorical columns:
gender
year_in_school
major
preferred_payment_method


## Numerical columns:
age
monthly_income
financial_aid
tuition
housing
food
transportation
books_supplies
entertainment
personal_care
technology
health_wellness
miscellaneous


## Statistika pershkruese per atributet numerike:
               age  monthly_income  ...  health_wellness  miscellaneous
count  1000.000000     1000.000000  ...      1000.000000    1000.000000
mean     21.675000     1020.650000  ...       114.310000     108.910000
std       2.322664      293.841161  ...        49.591544      52.412221
min      18.000000      501.000000  ...        30.000000      20.000000
25%      20.000000      770.750000  ...        73.000000      63.750000
50%      22.000000     1021.000000  ...       115.000000     110.000000
75%      24.000000     1288.250000  ...       158.000000     153.000000
max      25.000000     1500.000000  ...       200.000000     200.000000

[8 rows x 13 columns]


## Statistika pershkruese per atributet kategorike:
       gender year_in_school    major preferred_payment_method
count    1000           1000     1000                     1000
unique      3              4        5                        3
top      Male         Senior  Biology       Mobile Payment App
freq      356            254      228                      350


## Encoding Categorical Variables
   age  gender  ...  miscellaneous  preferred_payment_method
0   19       2  ...             72                         1
1   24       0  ...             68                         1
2   24       2  ...            133                         0
3   23       0  ...             55                         2
4   20       0  ...            104                         1

[5 rows x 17 columns]

## Kolonat numerike te perdorura per reduktimin e dimensionit:
      age  monthly_income  ...  health_wellness  miscellaneous
0     19             958  ...              127             72
1     24            1006  ...              129             68
2     24             734  ...              112            133
3     23             617  ...              105             55
4     20             810  ...               71            104
..   ...             ...  ...              ...            ...
995   22            1346  ...               65            163
996   19            1407  ...               84            135
997   20             957  ...               57             28
998   22            1174  ...              101             65
999   24             541  ...               88            145

[1000 rows x 13 columns]


## Te dhenat me dimensione te reduktura ne 3.              
PC1         PC2         PC3
0   -1417.793598  171.018080 -179.194464
1    -389.033443 -165.042651  331.342824
2    1467.814046   42.911074  514.333985
3    -413.967751  470.064982  -15.722405
4     633.961118  175.479478  117.790551
..           ...         ...         ...
995   833.219156 -294.344070 -144.782288
996  1139.648822 -366.053361 -133.778429
997  1023.965370  106.732374  -62.534253
998   870.445303 -187.716894   22.879345
999 -1445.276607  355.703815  346.822663

[1000 rows x 3 columns]

## Binarizimi i kolones financial_aid dhe diskretizimi i kolones monthly_income:
   age  gender  year_in_school  ...  total_expenses  has_financial_aid  income_group
0   19       2               0  ...            7707                  1           1.0
1   24       0               1  ...            6756                  1           1.0
2   24       2               1  ...            4810                  1           0.0
3   23       0               2  ...            6665                  1           0.0
4   20       0               2  ...            5828                  1           0.0

[5 rows x 20 columns]

# Faza 2

 Detektimi i perjashtuesve:

## Reshtat qe permbajne perjashtues: 
Index([  0,   5,   6,   8,   9,  11,  13,  14,  15,  16,
       ...
       990, 991, 992, 993, 994, 995, 996, 997, 998, 999],
      dtype='int64', length=565)

dhe paraqitja e cooralation matrix e bashkangjitur ne /visual/1_phase2.png

# Faza 3

Visualizimi i te dhenave ne baze te tipit, vizualizimi statik dhe interaktiv si dhe vizualizimi multi dimensional

## Visualization Based on Data Type

## Numerical data visualization
(histogram) 1_phase2.png

## Categorical data visualization 
(bar plot) 2_phase3.png

## Static Visualization
Box plot (static) 3_phase3.png

## Interactive Visualization
Scatter plot (interactive) 4_phase3.png

# Multidimensional Data Visualization
Pair plot (multidimensional) 5_phase3.png
