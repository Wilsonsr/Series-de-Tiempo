library(shiny)
library(forecast) # para ggtsdisplay()
library(TTR) # para la función SMA, si es necesaria

# Definir la interfaz de usuario
ui <- fluidPage(
  titlePanel("Simulación de Modelo AR(p)"),
  
  sidebarLayout(
    sidebarPanel(
      sliderInput("n", "Número de observaciones:", 
                  min = 100, max = 5000, value = 1000),
      sliderInput("p", "Orden del modelo AR(p):", 
                  min = 1, max = 5, value = 1),
      uiOutput("ar_sliders")
    ),
    
    mainPanel(
      plotOutput("simPlot")
    )
  )
)

# Definir el servidor
server <- function(input, output) {
  
  output$ar_sliders <- renderUI({
    sliderInputs <- lapply(1:input$p, function(i) {
      sliderInput(
        inputId = paste0("ar", i),
        label = paste("Coeficiente AR", i, ":"),
        min = -0.9, max = 0.9, value = 0, step = 0.1
      )
    })
    do.call(tagList, sliderInputs)
  })
  
  simulatedData <- reactive({
    set.seed(123)
    ar_coefs <- sapply(1:input$p, function(i) input[[paste0("ar", i)]])
    arima.sim(n = input$n, list(ar = ar_coefs))
  })
  
  output$simPlot <- renderPlot({
    ggtsdisplay(simulatedData())
  })
}

# Correr la aplicación
shinyApp(ui = ui, server = server)
