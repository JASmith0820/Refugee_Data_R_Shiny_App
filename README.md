# Refugee_Data_R_Shiny_App
#### R Shiny Application with Refugee Trends (1995-2014)

The purpose of this project was to gain a deeper understanding of the scale of today's refugee crisis as well as the historical trends that led to this moment. Python was used to pull World Bank data via the pandas API, store and query the data using MySQL, and write all results to csv. An R Shiny application was built to read in the csv files and visualize historic refugee trends in an interactive web application.

To start you may want to watch my **YouTube video walk-through** of this project. It provides detailed information on why I choose to explore this data, what my sources were, and interesting trends found in the R Shiny application. You can find it at: https://youtu.be/tN6_a4sA_AA

Or, you may want to start by reading the **written report**, which includes a workflow and instructions for recreating my steps. This document (WrittenReport_JS_G35169458) has been provided as both a .pdf and a .tex file.

If you want to skip straight to the **R Shiny application** you can find it at: https://jasmith0820.shinyapps.io/Refugee_Shiny_App

If you don't want to do any of those you can completely **re-create my project** by following these steps:  
1) Create an empty directory and clone all files to your local machine. Ensure that this new directory will be your working directory for all phases of this project.  
2) Run the Python code IndividualProject_JS_G35169458.py. This will output 10 csv's to your working directory.  
3) Open R Studio, making sure to set your working directory. Assuming that you already have the Shiny library installed:  
  Run the command "library(shiny)"  
  Run the command "runApp()"

  
