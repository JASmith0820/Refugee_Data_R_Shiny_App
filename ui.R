shinyUI(fluidPage(
  
  h2(strong("World Bank Refugee Data"), align='center' ),
  
  h5("Select a year to learn which countries saw the most refugees leave, \nand which saw the most arrive.", align='center'),

  fluidRow(
    column(5,
      sliderInput("year", 
                  label = "Year",
                  min = 1995, max = 2014, value = 1995, step=1, animate = animationOptions(interval=4000)),
      h6(em("Press the play button (above) to view as slideshow."))
    ),
    column(7,
           tableOutput("totalAsylum"),
           tableOutput("USA")
           )
  ),
  fluidRow(
    column(6, 
           h3("Where are refugees leaving?", align='center'),
           h5("Top 10 Countries by # of Refugees Leaving", align='center'),
           plotOutput("originPlot")),
    column(6,
           h3("Where are refugees going?", align='center'),
           h5("Top 10 Countries by # of Refugees Arriving", align='center'),
           plotOutput("asylumPlot"))
  ),
  fluidRow(
    column(12,
           h5("The following countries did not provide data to the World Bank in this year, and therefore cannot be included:"),
           tableOutput("missingData"))
  ),
  br(),
  h4("These tell us a lot about the countries losing/taking the most refugees in terms of",strong('raw numbers'),". \
    But which countries lost/gained the higest number as a",strong("proportion"), "of their total population?", align='center'),
  br(),
  fluidRow(
    column(6,
           h3("Highest proportion leaving:"),
           tableOutput("originPercentage")),
    column(6,
           h3("Highest proportion arriving:"),
           tableOutput("asylumPercentage"))
  ),
  br(),
  h4("Within the timeframe included in this dataset, which countries and years represent the", strong("all-time-highest"),"\
  numbers of refugees leaving/arriving in a given year?"),
  fluidRow(
    column(6,
           h3("All-time highest # leaving:"),
           tableOutput("highestOrigin")),
    column(6,
           h3("All-time highest # arriving:"),
           tableOutput("highestAsylum"))
  ),
  br(),
  fluidRow(
    column(12,
           h4("Looking at the entire timeframe included in this dataset, how do trends in the", strong("USA"),"compare to the trends overall?"),
           br(),
           h3("Total Number of Refugees Granted Asylum in the USA each Year", align='center'),
           plotOutput("USAPlot"))
  ),
  fluidRow(
    column(12,
      h6('Data Source: World Bank Data, Indicators. http://data.worldbank.org/indicator'),
      h6('The two indicators used here are:'),
      h6('1) Refugee population by country or territory of ',strong('asylum'),': http://data.worldbank.org/indicator/SM.POP.REFG'),
      h6('Defined as "Refugees are people who are recognized as refugees under the 1951 Convention Relating to the Status of Refugees or its 1967 Protocol, the 1969 Organization of African Unity Convention Governing the Specific Aspects of Refugee Problems in Africa, people recognized as refugees in accordance with the UNHCR statute, people granted refugee-like humanitarian status, and people provided temporary protection. Asylum seekers--people who have applied for asylum or refugee status and who have not yet received a decision or who are registered as asylum seekers--are excluded. Palestinian refugees are people (and their descendants) whose residence was Palestine between June 1946 and May 1948 and who lost their homes and means of livelihood as a result of the 1948 Arab-Israeli conflict. Country of asylum is the country where an asylum claim was filed and granted."'),
      h6('2) Refugee population by country or territory of ',strong('origin'),': http://data.worldbank.org/indicator/SM.POP.REFG.OR'),
      h6('Defined as "Refugees are people who are recognized as refugees under the 1951 Convention Relating to the Status of Refugees or its 1967 Protocol, the 1969 Organization of African Unity Convention Governing the Specific Aspects of Refugee Problems in Africa, people recognized as refugees in accordance with the UNHCR statute, people granted refugee-like humanitarian status, and people provided temporary protection. Asylum seekers--people who have applied for asylum or refugee status and who have not yet received a decision or who are registered as asylum seekers--are excluded. Palestinian refugees are people (and their descendants) whose residence was Palestine between June 1946 and May 1948 and who lost their homes and means of livelihood as a result of the 1948 Arab-Israeli conflict. Country of origin generally refers to the nationality or country of citizenship of a claimant."'),
      h6('The proportionality tables also used the following indicator as the calculation\'s denominator:'),
      h6('3) Population, total: http://data.worldbank.org/indicator/SP.POP.TOTL'),
      h6('Defined as "Total population is based on the de facto definition of population, which counts all residents regardless of legal status or citizenship--except for refugees not permanently settled in the country of asylum, who are generally considered part of the population of their country of origin. The values shown are midyear estimates."')
    )
  )
))