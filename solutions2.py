from pandasql import sqldf
import pandas as pd
InjurySummary= pd.read_csv('/Users/peterparker/Desktop/untitled folder/Takehometest/InjurySummary.csv')
bodyparts= pd.read_csv('/Users/peterparker/Desktop/untitled folder/Takehometest/bodyParts.csv')
diagnosis= pd.read_csv('/Users/peterparker/Desktop/untitled folder/Takehometest/diagnosis.csv')
Location= pd.read_csv('/Users/peterparker/Desktop/untitled folder/Takehometest/Location.csv')


#1 Total number of cases in each location and display the percentage of cases for each sex per location.
#Solution 1 that shows Percentage for each location separately

print('Question 1 Total number of cases in each location and display the percentage of cases for each sex per location. \n')

print('Solution 1 that shows Percentage for each location separately \n')

print(sqldf("select location,sex,count(*),count(*) * 100.0 / sum(count(*)) over(Partition by location) as Percent_Total from InjurySummary group by location,sex"))

print('\n\n\n')

#Solution 2 that shows overall percentage

print('Solution 2 that shows overall percentage \n')

print(sqldf("select location,sex,count(*),count(*) * 100.0 / sum(count(*)) over() as Percent_Total from InjurySummary group by location,sex"))

print('\n\n\n')

#2 What are the body parts affected for the diagnosis "crushing" and what are the common locations this accident happens?

print('Q2 What are the body parts affected for the diagnosis "crushing" and what are the common locations this accident happens?\n')

print('Solution 2 that uses inner join on tables to identofy body parts for diagnosis crushing\n')

print(sqldf("select distinct diagnosis.Diagnosis,bodyParts.'Body Part Affected',Location.'Incident Locale' from InjurySummary inner join diagnosis on InjurySummary.diagnosis= diagnosis.Code inner join Location on InjurySummary.location=Location.Code inner join bodyparts on InjurySummary.bodyPart=bodyParts.Code where diagnosis.Diagnosis='Crushing'"))

print('\n\n\n')

#3 Find the top 5 diagnosis and which range of age group are affected by these diagnosis

print('Q3 Find the top 5 diagnosis and which range of age group are affected by these diagnosis\n')

print('Solution 3 \n')

print(sqldf("select diagnosis.Diagnosis,min(age),max(age),count(*) as TotalCount from InjurySummary inner join diagnosis on InjurySummary.diagnosis= diagnosis.Code inner join Location on InjurySummary.location=Location.Code inner join bodyparts on InjurySummary.bodyPart=bodyParts.Code group by diagnosis.Diagnosis order by TotalCount desc limit 5"))

