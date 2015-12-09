shinyUI(fluidPage(
  
  h2(strong("World Bank (UNHCR) Refugee Data"), align='center' ),
  
  h5("Each year the UNHCR (UN Refugee Agency) releases a snapshot of the 
     number of refugees worldwide. They provide two key indicators about the refugee population:"),
  h5("1) ",strong("Country of Asylum"),": The country in which refugees have been granted asylum
     or temporary protection (where the refugees are living now)"),
  h5("2) ",strong("Country of Origin"),": The countries of citizenship of the refugees (where the refugees left)"),
  h5("The following graphs and tables provide data compiled from these two indicators between 1995 and 2014. Further details regarding the sources can be found at the bottom of the site."),
  h5("Use the Year toolbar to the left to select a year, or click play to view the data as a slideshow."),
  br(),
  fluidRow(
    column(5,
      sliderInput("year", 
                  label = "Year",
                  min = 1995, max = 2014, value = 1995, step=1, animate = animationOptions(interval=4000))
    ),
    column(7,
           tableOutput("totalAsylum"),
           tableOutput("USA")
           )
  ),
  fluidRow(
    column(6, 
           h3("Where did they leave?", align='center'),
           h5("Top 10 Populations by Country of Origin", align='center'),
           plotOutput("originPlot")),
    column(6,
           h3("Where are they now?", align='center'),
           h5("Top 10 Populations by Country of Asylum", align='center'),
           plotOutput("asylumPlot"))
  ),
  fluidRow(
    column(12,
           h5("The following countries did not provide data to the UNHCR in this year, and therefore cannot be included:"),
           tableOutput("missingData"))
  ),
  br(),
  h4("These give us a snapshot of the worldwide refugee population and where they are now in terms of",strong('raw numbers'),". \
    But which countries have the highest ",strong("proportion"), "of refugees?", align='center'),
  h4("On the left, I have divided the number of refugees by total population using the country of origin indicator. \
    On the right I have done the same for the country of asylum. ", align='center'),
  br(),
  fluidRow(
    column(6,
           h3("Country of Origin"),
           tableOutput("originPercentage")),
    column(6,
           h3("Country of Asylum"),
           tableOutput("asylumPercentage"))
  ),
  br(),
  h4("Between 1995 and 2014, which countries had the", strong("all-time highest"),"\
  number of refugees seeking asylum elsewhere? Which had the highest number of refugees living there?"),
  fluidRow(
    column(6,
           h3("Country of Origin:"),
           tableOutput("highestOrigin")),
    column(6,
           h3("Country of Asylum:"),
           tableOutput("highestAsylum"))
  ),
  br(),
  fluidRow(
    column(12,
           h4("Between 1995 and 2014 what has been the refugee population in the", strong("United States"), "in each year?"),
           br(),
           h3("Total Refugee Population of the United Stated in Each Year", align='center'),
           plotOutput("USAPlot"))
  ),
  fluidRow(
    column(12,
      h6('Data Source: World Bank Data Indicators (originally gathered by the UNHCR). http://data.worldbank.org/indicator'),
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