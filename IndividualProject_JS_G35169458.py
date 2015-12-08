# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 15:05:54 2015

@author: vagrant
"""

import pandas as pd
from pandas.io import wb
import MySQLdb as SQL
import matplotlib.pyplot as plt
import scipy
import matplotlib.pylab as pylab
import numpy as np
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

def initialize_years(start_year, end_year):
    #Takes a start year and an end year
    #Returns the start and end year and a numpy array with
    #one entry for each year within that range

    start_year = start_year
    end_year = end_year
    years = np.arange(start_year,end_year+1)
    
    return start_year, end_year, years
    
def get_wb_data(indicator, start_year, end_year):
    #Takes the name of an indicator and the start and end years
    #Returns the result of the pandas dataframe API from the world bank
    #for that API
    
    dataset = wb.download(indicator=indicator, country='all', start=start_year, end=end_year)

    return dataset
    
def drop_and_create_db(db_name, cursor):
    #Takes a database name and a cursor as input
    #Drops a database if one of that name exists
    #Creates a new database with that name
    #Does not return anything
    sql = 'DROP DATABASE IF EXISTS %s;' % db_name
    cursor.execute(sql)
    sql = ' CREATE DATABASE %s; ' % db_name
    cursor.execute(sql)
    
def initialize_db(db_name):
    # Set up a connection to the new music database
    mydb = SQL.connect(host='localhost', user='root', passwd='root', db=db_name)
    cursor = mydb.cursor()
    
    return cursor
    
def prepare_for_csv_write():
    # Prepares the necessary variables for writing to csv
    # This process is completed several times at the end of the code
    # Returns two blank lists, a blank dictionary, and an index value of 0
    blank_list = []
    blank_dict = {}
    blank_list_for_csv = []
    idx = 0
    
    return blank_list,blank_dict,blank_list_for_csv,idx  

    
#Set the timeframe    
start_year, end_year, years = initialize_years(1995, 2014)

#Get the world bank data
origin_raw = get_wb_data('SM.POP.REFG.OR', start_year, end_year)
asylum_raw = get_wb_data('SM.POP.REFG', start_year, end_year)
population_raw = get_wb_data('SP.POP.TOTL', start_year, end_year)

#Determine the rows to remove so only have country-level data
rows_to_remove = 34 * (end_year-start_year+1)

#Create a master dataframe, then remove non-country level data
master_df = pd.concat([origin_raw, asylum_raw, population_raw], axis=1)
master_df_countries = master_df.iloc[rows_to_remove:,:]

#Rename the columns so they are easier to use
master_df_countries = master_df_countries.rename(columns={'SM.POP.REFG.OR':'Origin','SM.POP.REFG':'Asylum', 'SP.POP.TOTL':'Population' })

#The following country codes will be appended to the dataframe
country_codes = [["Afghanistan","AFG"], ["Albania","ALB"], ["Algeria","DZA"], 
                 ["American Samoa","ASM"], ["Andorra","AND"], ["Angola","AGO"], 
                 ["Antigua and Barbuda","ATG"], ["Argentina","ARG"], ["Armenia","ARM"], 
                 ["Aruba","ABW"], ["Australia","AUS"], ["Austria","AUT"], 
                 ["Azerbaijan","AZE"], ["Bahamas, The","BHS"], ["Bahrain","BHR"], 
                 ["Bangladesh","BGD"], ["Barbados","BRB"], ["Belarus","BLR"], 
                 ["Belgium","BEL"], ["Belize","BLZ"], ["Benin","BEN"], ["Bermuda","BMU"],
                 ["Bhutan","BTN"], ["Bolivia","BOL"], ["Bosnia and Herzegovina","BIH"], 
                 ["Botswana","BWA"], ["Brazil","BRA"], ["Brunei Darussalam","BRN"], 
                 ["Bulgaria","BGR"], ["Burkina Faso","BFA"], ["Burundi","BDI"], 
                 ["Cabo Verde","CPV"], ["Cambodia","KHM"], ["Cameroon","CMR"], 
                 ["Canada","CAN"], ["Cayman Islands","CYM"], ["Central African Republic","CAF"],
                 ["Chad","TCD"], ["Channel Islands","CHI"], ["Chile","CHL"], ["China","CHN"],
                 ["Colombia","COL"], ["Comoros","COM"], ["Congo, Dem. Rep.","COD"], 
                 ["Congo, Rep.","COG"], ["Costa Rica","CRI"], ["Cote d'Ivoire","CIV"], 
                 ["Croatia","HRV"], ["Cuba","CUB"], ["Curacao","CUW"], ["Cyprus","CYP"], 
                 ["Czech Republic","CZE"], ["Denmark","DNK"], ["Djibouti","DJI"], 
                 ["Dominica","DMA"], ["Dominican Republic","DOM"], ["Ecuador","ECU"], 
                 ["Egypt, Arab Rep.","EGY"], ["El Salvador","SLV"], ["Equatorial Guinea","GNQ"],
                 ["Eritrea","ERI"], ["Estonia","EST"], ["Ethiopia","ETH"], 
                 ["Faeroe Islands","FRO"], ["Fiji","FJI"], ["Finland","FIN"], ["France","FRA"], 
                 ["French Polynesia","PYF"], ["Gabon","GAB"], ["Gambia, The","GMB"], 
                 ["Georgia","GEO"], ["Germany","DEU"], ["Ghana","GHA"], ["Greece","GRC"], 
                 ["Greenland","GRL"], ["Grenada","GRD"], ["Guam","GUM"], ["Guatemala","GTM"], 
                 ["Guinea","GIN"], ["Guinea-Bissau","GNB"], ["Guyana","GUY"], ["Haiti","HTI"], 
                 ["Honduras","HND"], ["Hong Kong SAR, China","HKG"], ["Hungary","HUN"], 
                 ["Iceland","ISL"], ["India","IND"], ["Indonesia","IDN"], ["Iran, Islamic Rep.","IRN"], 
                 ["Iraq","IRQ"], ["Ireland","IRL"], ["Isle of Man","IMN"], ["Israel","ISR"], 
                 ["Italy","ITA"], ["Jamaica","JAM"], ["Japan","JPN"], ["Jordan","JOR"], 
                 ["Kazakhstan","KAZ"], ["Kenya","KEN"], ["Kiribati","KIR"], 
                 ["Korea, Dem. Rep.","PRK"], ["Korea, Rep.","KOR"], ["Kosovo","KSV"], 
                 ["Kuwait","KWT"], ["Kyrgyz Republic","KGZ"], ["Lao PDR","LAO"], 
                 ["Latvia","LVA"], ["Lebanon","LBN"], ["Lesotho","LSO"], ["Liberia","LBR"], 
                 ["Libya","LBY"], ["Liechtenstein","LIE"], ["Lithuania","LTU"], 
                 ["Luxembourg","LUX"], ["Macao SAR, China","MAC"], ["Macedonia, FYR","MKD"], 
                 ["Madagascar","MDG"], ["Malawi","MWI"], ["Malaysia","MYS"], ["Maldives","MDV"],
                 ["Mali","MLI"], ["Malta","MLT"], ["Marshall Islands","MHL"], 
                 ["Mauritania","MRT"], ["Mauritius","MUS"], ["Mexico","MEX"], 
                 ["Micronesia, Fed. Sts.","FSM"], ["Moldova","MDA"], ["Monaco","MCO"], 
                 ["Mongolia","MNG"], ["Montenegro","MNE"], ["Morocco","MAR"], 
                 ["Mozambique","MOZ"], ["Myanmar","MMR"], ["Namibia","NAM"], ["Nepal","NPL"], 
                 ["Netherlands","NLD"], ["New Caledonia","NCL"], ["New Zealand","NZL"], 
                 ["Nicaragua","NIC"], ["Niger","NER"], ["Nigeria","NGA"], ["Northern Mariana Islands","MNP"], 
                 ["Norway","NOR"], ["Oman","OMN"], ["Pakistan","PAK"], ["Palau","PLW"], ["Panama","PAN"], 
                 ["Papua New Guinea","PNG"], ["Paraguay","PRY"], ["Peru","PER"], ["Philippines","PHL"], 
                 ["Poland","POL"], ["Portugal","PRT"], ["Puerto Rico","PRI"], ["Qatar","QAT"], 
                 ["Romania","ROU"], ["Russian Federation","RUS"], ["Rwanda","RWA"], ["Samoa","WSM"], 
                 ["San Marino","SMR"], ["Sao Tome and Principe","STP"], ["Saudi Arabia","SAU"], 
                 ["Senegal","SEN"], ["Serbia","SRB"], ["Seychelles","SYC"], ["Sierra Leone","SLE"], 
                 ["Singapore","SGP"], ["Sint Maarten (Dutch part)","SXM"], ["Slovak Republic","SVK"], 
                 ["Slovenia","SVN"], ["Solomon Islands","SLB"], ["Somalia","SOM"], ["South Africa","ZAF"], 
                 ["South Sudan","SSD"], ["Spain","ESP"], ["Sri Lanka","LKA"], ["St. Kitts and Nevis","KNA"], 
                 ["St. Lucia","LCA"], ["St. Martin (French part)","MAF"], ["St. Vincent and the Grenadines","VCT"], 
                 ["Sudan","SDN"], ["Suriname","SUR"], ["Swaziland","SWZ"], ["Sweden","SWE"], 
                 ["Switzerland","CHE"], ["Syrian Arab Republic","SYR"], ["Taiwan, China","TWN"], 
                 ["Tajikistan","TJK"], ["Tanzania","TZA"], ["Thailand","THA"], ["Timor-Leste","TLS"], 
                 ["Togo","TGO"], ["Tonga","TON"], ["Trinidad and Tobago","TTO"], ["Tunisia","TUN"],
                 ["Turkey","TUR"], ["Turkmenistan","TKM"], ["Turks and Caicos Islands","TCA"], 
                 ["Tuvalu","TUV"], ["Uganda","UGA"], ["Ukraine","UKR"], ["United Arab Emirates","ARE"], 
                 ["United Kingdom","GBR"], ["United States","USA"], ["Uruguay","URY"], 
                 ["Uzbekistan","UZB"], ["Vanuatu","VUT"], ["Venezuela, RB","VEN"], 
                 ["Vietnam","VNM"], ["Virgin Islands (U.S.)","VIR"], ["West Bank and Gaza","PSE"], 
                 ["Yemen, Rep.","YEM"], ["Zambia","ZMB"], ["Zimbabwe","ZWE"]]

#Convert the above list to a dataframe and set an index
df_country_codes = pd.DataFrame(country_codes, columns=['country','country_code'])
df_country_codes = df_country_codes.set_index(['country'])

#Add country codes to the master dataframe
master_df_countries.reset_index(inplace=True)
df_country_codes.reset_index(inplace=True)

Master_df_merged = pd.merge(master_df_countries,df_country_codes,
                            left_on=['country'],right_on=['country'],how='inner')

#Reset the indices to country and country code in the master data frame
Master_df_merged = Master_df_merged.set_index(['country','country_code', 'year'])

#Create a dataframe with only the null values
Master_df_NAs = Master_df_merged[Master_df_merged.isnull().any(axis=1)]

#Remove all rows with 1 or more null values
Master_df_country_nonull = Master_df_merged.dropna() 

#Reset the indexes
Master_df_country_nonull.reset_index(inplace=True)
Master_df_NAs.reset_index(inplace=True)

#-----------MAKE MYSQL DATABASE-------------------------
#This will have a table for each data source we use
conn = SQL.connect(host='localhost', user='root', passwd='root')
cursor = conn.cursor()

# Delete the refugees database if it already exists, then create it
drop_and_create_db('refugees', cursor)
sql = ' USE refugees; '
cursor.execute(sql)  
cursor.close()

# Set up a connection to the new music database
cursor = initialize_db('refugees')

#set autocommit to 1 so data can be appended easily
sql = ' SET AUTOCOMMIT = 1;'
cursor.execute(sql)

sql = ' DROP TABLE IF EXISTS refugee_data;' 
cursor.execute(sql)
sql = '''
 CREATE TABLE refugee_data (
 country CHAR(255),
 country_code CHAR(3),
 year CHAR(4),
 origin INT,
 asylum INT,
 population INT);
 ''' 
cursor.execute(sql)

sql = ' DROP TABLE IF EXISTS refugee_nulls;' 
cursor.execute(sql)
sql = '''
 CREATE TABLE refugee_nulls (
 country CHAR(255),
 country_code CHAR(3),
 year CHAR(4),
 origin CHAR(20),
 asylum CHAR(20),
 population CHAR(20));
 ''' 
cursor.execute(sql)

#Take the data from the dictionary and place it in the table
for i in np.arange(0,len(Master_df_country_nonull)):
    sql='''
    INSERT INTO refugee_data (country,country_code,year,origin,asylum,population)
    VALUES ("%s", "%s","%s", "%s", "%s", "%s");''' % (Master_df_country_nonull.iloc[i]['country'], \
    Master_df_country_nonull.iloc[i]['country_code'], Master_df_country_nonull.iloc[i]['year'], \
    Master_df_country_nonull.iloc[i]['Origin'], Master_df_country_nonull.iloc[i]['Asylum'], \
    Master_df_country_nonull.iloc[i]['Population'])
    cursor.execute(sql)  
    
#Take the data from the dictionary and place it in the table
for i in np.arange(0,len(Master_df_NAs)):
    sql='''
    INSERT INTO refugee_nulls (country,country_code,year,origin,asylum,population)
    VALUES ("%s", "%s","%s", "%s", "%s", "%s");''' % (Master_df_NAs.iloc[i]['country'], \
    Master_df_NAs.iloc[i]['country_code'], Master_df_NAs.iloc[i]['year'], \
    Master_df_NAs.iloc[i]['Origin'], Master_df_NAs.iloc[i]['Asylum'], \
    Master_df_NAs.iloc[i]['Population'])
    cursor.execute(sql)  
  
#----------WRITE DATA TO CSV FILES FOR RSHINY---------------------

#create a csv file for the top origin countries
append_list, append_dict, blank_list_for_csv, idx = prepare_for_csv_write()

for year in years:
    sql = '''
    SELECT * FROM
    (SELECT country, country_code, origin/1000 FROM refugee_data WHERE year="%s"
    ORDER BY origin desc) A
    LIMIT 10''' % year
    cursor.execute(sql)
    append_list = cursor.fetchall()
    
    for i in append_list:
        append_dict[idx] = {'country':i[0], 
                        'country_code':i[1] ,
                        'year': year,
                        'origin':int(i[2])}
        idx = idx+1

list_for_csv = []        
for idx in np.arange(0, len(append_dict)):
    list_for_csv.append( ('"%s","%s","%s","%s"') % (append_dict[idx]['country'],append_dict[idx]['country_code'],append_dict[idx]['year'],append_dict[idx]['origin']))

        
with open('top_origin.csv', 'w') as handle:
    handle.write('"country","country_code","year","origin"\n')
    for i in list_for_csv:
        handle.write(i)
        handle.write('\n')
    
#create a csv file for the top asylum countries
append_list, append_dict, blank_list_for_csv, idx = prepare_for_csv_write()

for year in years:
    sql = '''
    SELECT * FROM
    (SELECT country, country_code, asylum/1000 FROM refugee_data WHERE year="%s"
    ORDER BY asylum desc) A
    LIMIT 10''' % year
    cursor.execute(sql)
    append_list = cursor.fetchall()
    
    for i in append_list:
        append_dict[idx] = {'country':i[0], 
                        'country_code':i[1] ,
                        'year': year,
                        'asylum':int(i[2])}
        idx = idx+1

list_for_csv = []        
for idx in np.arange(0, len(append_dict)):
    list_for_csv.append( ('"%s","%s","%s","%s"') % (append_dict[idx]['country'],append_dict[idx]['country_code'],append_dict[idx]['year'],append_dict[idx]['asylum']))

        
with open('top_asylum.csv', 'w') as handle:
    handle.write('"country","country_code","year","asylum"\n')
    for i in list_for_csv:
        handle.write(i)
        handle.write('\n')
    
#Get the total number of refugees (origin) by year    
append_list, append_dict, blank_list_for_csv, idx = prepare_for_csv_write()
sql = '''
SELECT year, sum(origin) as origin_total
FROM refugee_data
GROUP BY  year
ORDER BY year 
'''
cursor.execute(sql)
append_list = cursor.fetchall()

append_dict = {}

for i in append_list:
    append_dict[idx] = {
    'year':i[0],
    'origin_total':"{:,}".format(int(i[1]))}
    idx = idx+1
    
blank_list_for_csv = []        
for idx in np.arange(0, len(append_dict)):
    blank_list_for_csv.append( ('"%s","%s"') % (append_dict[idx]['year'],append_dict[idx]['origin_total']))
    
with open('total_origin.csv', 'w') as handle:
    handle.write('"year","origin_total"\n')
    for i in blank_list_for_csv:
        handle.write(i)
        handle.write('\n')
        
#Get the total number of refugees (asylum) by year
append_list, append_dict, blank_list_for_csv, idx = prepare_for_csv_write()
sql = '''
SELECT year, sum(asylum) as asylum_total
FROM refugee_data
GROUP BY  year
ORDER BY year 
'''
cursor.execute(sql)
append_list = cursor.fetchall()

append_dict = {}

for i in append_list:
    append_dict[idx] = {
    'year':i[0],
    'asylum_total':"{:,}".format(int(i[1]))}
    idx = idx+1
    
blank_list_for_csv = []        
for idx in np.arange(0, len(append_dict)):
    blank_list_for_csv.append( ('"%s","%s"') % (append_dict[idx]['year'],append_dict[idx]['asylum_total']))
    
with open('total_asylum.csv', 'w') as handle:
    handle.write('"year","asylum_total"\n')
    for i in blank_list_for_csv:
        handle.write(i)
        handle.write('\n')
    

#Get data as a percentage of the population leaving
append_list, append_dict, blank_list_for_csv, idx = prepare_for_csv_write()

for year in years:
    
    sql = '''
        SELECT * FROM
        (SELECT country, year, origin/population * 100 as origin_over_pop
        FROM refugee_data
        WHERE year = "%s"
        ORDER BY origin_over_pop DESC) A
        LIMIT 10;''' %year
    cursor.execute(sql)
    append_list = cursor.fetchall()
    
    for i in append_list:
        append_dict[idx] = {'country':i[0], 
                        'year': i[1],
                        'origin_over_pop':"{:4.2f}".format(float(i[2]))}
        idx = idx+1
        
blank_list_for_csv = []        
for idx in np.arange(0, len(append_dict)):
    blank_list_for_csv.append( ('"%s","%s","%s"') % (append_dict[idx]['country'],append_dict[idx]['year'],append_dict[idx]['origin_over_pop']))
    
with open('origin_percentage.csv', 'w') as handle:
    handle.write('"country","year","origin_over_pop"\n')
    for i in blank_list_for_csv:
        handle.write(i)
        handle.write('\n')
        
#Get data as a percentage of the population arriving
append_list, append_dict, blank_list_for_csv, idx = prepare_for_csv_write()

for year in years: 
    sql = '''
        SELECT * FROM
        (SELECT country, year, asylum/population * 100 as asylum_over_pop
        FROM refugee_data
        WHERE year = "%s"
        ORDER BY asylum_over_pop desc) A
        LIMIT 10;''' %year
    cursor.execute(sql)
    append_list = cursor.fetchall()
    
    for i in append_list:
        append_dict[idx] = {'country':i[0], 
                        'year': i[1],
                        'asylum_over_pop':"{:4.2f}".format(float(i[2]))}
        idx = idx+1
        
blank_list_for_csv = []        
for idx in np.arange(0, len(append_dict)):
    blank_list_for_csv.append( ('"%s","%s","%s"') % (append_dict[idx]['country'],append_dict[idx]['year'],append_dict[idx]['asylum_over_pop']))
    
with open('asylum_percentage.csv', 'w') as handle:
    handle.write('"country","year","asylum_over_pop"\n')
    for i in blank_list_for_csv:
        handle.write(i)
        handle.write('\n')
        
#What are the all-time high's in terms of refugee origins?
append_list, append_dict, blank_list_for_csv, idx = prepare_for_csv_write()
sql = '''
SELECT country, year, origin
FROM refugee_data
ORDER BY origin desc
LIMIT 10
'''
cursor.execute(sql)
append_list = cursor.fetchall()

append_dict = {}

for i in append_list :
    append_dict[idx] = {
    'country':i[0],
    'year':i[1],
    'total_refugees':"{:,}".format(int(i[2]))}
    idx = idx+1
    
blank_list_for_csv = []        
for idx in np.arange(0, len(append_dict)):
    blank_list_for_csv.append( ('"%s","%s","%s"') % (append_dict[idx]['country'],append_dict[idx]['year'],append_dict[idx]['total_refugees']))
    
with open('highest_origin.csv', 'w') as handle:
    handle.write('"country","year","total_refugees"\n')
    for i in blank_list_for_csv:
        handle.write(i)
        handle.write('\n')

#What are the all-time high's in terms of refugee asylum?
append_list, append_dict, blank_list_for_csv, idx = prepare_for_csv_write()
sql = '''
SELECT country, year, asylum
FROM refugee_data
ORDER BY asylum desc
LIMIT 10
'''
cursor.execute(sql)
append_list = cursor.fetchall()

for i in append_list :
    append_dict[idx] = {
    'country':i[0],
    'year':i[1],
    'total_refugees':"{:,}".format(int(i[2]))}
    idx = idx+1
    
blank_list_for_csv = []        
for idx in np.arange(0, len(append_dict)):
    blank_list_for_csv.append( ('"%s","%s","%s"') % (append_dict[idx]['country'],append_dict[idx]['year'],append_dict[idx]['total_refugees']))
    
with open('highest_asylum.csv', 'w') as handle:
    handle.write('"country","year","total_refugees"\n')
    for i in blank_list_for_csv:
        handle.write(i)
        handle.write('\n')

#How many refugees does the USA take?
append_list, append_dict, blank_list_for_csv, idx = prepare_for_csv_write()
sql = '''
SELECT year, asylum
FROM refugee_data
WHERE country = 'United States'
ORDER BY year
'''
cursor.execute(sql)
append_list = cursor.fetchall()

for i in append_list :
    append_dict[idx] = {
    'year':i[0],
    'asylum':"{:,}".format(int(i[1]))}
    idx = idx+1
    
blank_list_for_csv = []        
for idx in np.arange(0, len(append_dict)):
    blank_list_for_csv.append( ('"%s","%s"') % (append_dict[idx]['year'],append_dict[idx]['asylum']))
    
with open('USA.csv', 'w') as handle:
    handle.write('"year","asylum"\n')
    for i in blank_list_for_csv:
        handle.write(i)
        handle.write('\n')
        
#Which countries are missing data in each year?
append_list, append_dict, blank_list_for_csv, idx = prepare_for_csv_write()
sql = '''
SELECT country, year
FROM refugee_nulls
'''
cursor.execute(sql)
append_list = cursor.fetchall()

for i in append_list :
    append_dict[idx] = {
    'country':i[0],
    'year':i[1]}
    idx = idx+1
    
blank_list_for_csv = []        
for idx in np.arange(0, len(append_dict)):
    blank_list_for_csv.append( ('"%s","%s"') % (append_dict[idx]['country'],append_dict[idx]['year']))
    
with open('missing_data.csv', 'w') as handle:
    handle.write('"country","year"\n')
    for i in blank_list_for_csv:
        handle.write(i)
        handle.write('\n')


append_list, append_dict, blank_list_for_csv, idx = prepare_for_csv_write()  
     
for year in years:
    append_list = []
    sql = '''
    SELECT country
    FROM refugee_nulls
    where year = %s
    ''' % year
    cursor.execute(sql)
    for i in cursor.fetchall():
        append_list.append(i[0])
        
    list_as_string = ', '.join(append_list)

    append_dict[year] = {
    'countries': list_as_string}
            
for idx in np.arange(start_year, end_year+1):
    blank_list_for_csv.append( ('\"%s\",\"%s\"') % (idx,append_dict[idx]['countries']))
    
with open('missing_data.csv', 'w') as handle:
    handle.write('"year","countries"\n')
    for i in blank_list_for_csv:
        handle.write(i)
        handle.write('\n')
        