library(shiny)
library(forecast) # para ggtsdisplay()

# Definir la interfaz de usuario
ui <- fluidPage(
  titlePanel("Simulación de AR(1)"),
  
  sidebarLayout(
    sidebarPanel(
      sliderInput("n", "Número de observaciones:", 
                  min = 100, max = 1000, value = 100),
      sliderInput("ar", "Parámetro AR:", 
                  min = -0.9, max = 0.9, value = 0.1, step = 0.1)
    ),
    
    mainPanel(
      textOutput("simText"),
      plotOutput("simPlot")
    )
  )
)

# Definir el servidor
server <- function(input, output) {
  
  output$simText <- renderText({
    paste("AR(1) con parámetro:", input$ar, "y", input$n, "observaciones")
  })
  
  output$simPlot <- renderPlot({
    set.seed(123)
    simData <- arima.sim(n = input$n, list(ar = input$ar))
    ggtsdisplay(simData)
  })
}

# Correr la aplicación
shinyApp(ui = ui, server = server)
