# server.R

library(dplyr)
library(ggplot2)

asylum <- read.csv('top_asylum.csv', 
                   header=TRUE, sep=",", quote="\"")

origin <- read.csv('top_origin.csv', 
                   header=TRUE, sep=",", quote="\"")

totalOrigin <- read.csv('total_origin.csv', 
                               header=TRUE, sep=",", quote="\"")

totalAsylum <- read.csv('total_asylum.csv', 
                        header=TRUE, sep=",", quote="\"")

names(totalAsylum)[names(totalAsylum)=="asylum_total"] <- "Total # refugees counted worldwide:"


originPercentage <- read.csv('origin_percentage.csv', 
                             header=TRUE, sep=",", quote="\"")

names(originPercentage)[names(originPercentage)=="origin_over_pop"] <- "% of total pop. leaving"

asylumPercentage <- read.csv('asylum_percentage.csv', 
                             header=TRUE, sep=",", quote="\"")

names(asylumPercentage)[names(asylumPercentage)=="asylum_over_pop"] <- "% of total pop. arriving"

originHighs <- read.csv('highest_origin.csv', 
                             header=TRUE, sep=",", quote="\"")

names(originHighs)[names(originHighs)=="total_refugees"] <- "# of refugees leaving"

asylumHighs <- read.csv('highest_asylum.csv', 
                             header=TRUE, sep=",", quote="\"")

names(asylumHighs)[names(asylumHighs)=="total_refugees"] <- "# of refugees arriving"

USA <- read.csv('USA.csv', 
                        header=TRUE, sep=",", quote="\"")

names(USA)[names(USA)=="asylum"] <- "Total # refugees accepted in the USA:"

missingData <- read.csv('missing_data.csv', 
                header=TRUE, sep=",", quote="\"")



shinyServer(function(input, output) {
  
  output$asylumPlot <- renderPlot({
    ggplot(data=subset(asylum, year == input$year), aes(x=reorder(country, -asylum), y=asylum)) +
      geom_bar(stat="identity", fill="blue") +
      theme(axis.text.x=element_text(angle=90, color="black", size=12)) +
      theme(axis.text.y=element_text(color="black")) +
      xlab("") +
      ylab("# of Refugees Leaving (in thousands)") +
      geom_text(aes(label=asylum), vjust=-.1) +
      expand_limits(y=c(0, 4000))
  })
    
  output$originPlot <- renderPlot({
    ggplot(data=subset(origin, year == input$year), aes(x=reorder(country, -origin), y=origin)) +
      geom_bar(stat="identity", fill="orange") +
      theme(axis.text.x=element_text(angle=90, color="black", size=12)) +
      theme(axis.text.y=element_text(color="black")) +
      xlab("") +
      ylab("# of Refugees Arriving (in thousands)") +
      geom_text(aes(label=origin), vjust=-.1) +
      expand_limits(y=c(0, 4000))
  })
  
  output$totalAsylum <- renderTable({
    subset(subset(totalAsylum, year == input$year), select = names(totalAsylum)[names(totalAsylum)=="Total # refugees counted worldwide:"])
  }, include.rownames=FALSE)
  
  output$originPercentage <- renderTable({
    subset(originPercentage, year == input$year)
  }, include.rownames=FALSE)
  
  output$asylumPercentage <- renderTable({
    subset(asylumPercentage, year == input$year)
  }, include.rownames=FALSE)
  
  output$highestOrigin<- renderTable({
    originHighs
  }, include.rownames=FALSE)
  
  output$highestAsylum <- renderTable({
    asylumHighs
  }, include.rownames=FALSE)
  
  output$USA <- renderTable({
    subset(subset(USA, year == input$year), select = names(USA)[names(USA)=="Total # refugees accepted in the USA:"])
  }, include.rownames=FALSE)
  
  output$USAPlot <- renderPlot({
    ggplot(data=USA, aes(x=year, y=`Total # refugees accepted in the USA:`)) +
      geom_bar(stat="identity", fill="dark green") +
      theme(axis.text.x=element_text(angle=90, color="black", size=12)) +
      theme(axis.text.y=element_text(color="black")) +
      xlab("") +
      ylab("# of Refugees Accepted") +
      geom_text(aes(label=`Total # refugees accepted in the USA:`), vjust=-.1)
  })
  
  output$missingData <- renderTable({
    subset(subset(missingData, year == input$year), select = names(missingData)[names(missingData)=="countries"])
  }, include.rownames=FALSE)
    
  
})