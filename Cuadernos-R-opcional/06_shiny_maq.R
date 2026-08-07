library(shiny)
library(forecast) # para ggtsdisplay()

# Definir la interfaz de usuario
ui <- fluidPage(
  titlePanel("Simulación de Modelo MA(q)"),
  
  sidebarLayout(
    sidebarPanel(
      sliderInput("n", "Número de observaciones:", 
                  min = 100, max = 5000, value = 1000),
      sliderInput("q", "Orden del modelo MA(q):", 
                  min = 1, max = 5, value = 1),
      uiOutput("ma_sliders")
    ),
    
    mainPanel(
      plotOutput("simPlot")
    )
  )
)

# Definir el servidor
server <- function(input, output) {
  
  output$ma_sliders <- renderUI({
    sliderInputs <- lapply(1:input$q, function(i) {
      sliderInput(
        inputId = paste0("ma", i),
        label = paste("Coeficiente MA", i, ":"),
        min = -0.9, max = 0.9, value = 0, step = 0.1
      )
    })
    do.call(tagList, sliderInputs)
  })
  
  simulatedData <- reactive({
    set.seed(123)
    ma_coefs <- sapply(1:input$q, function(i) input[[paste0("ma", i)]])
    arima.sim(n = input$n, model = list(ma = ma_coefs), innov=rnorm(input$n))
  })
  
  output$simPlot <- renderPlot({
    ggtsdisplay(simulatedData())
  })
}

# Correr la aplicación
shinyApp(ui = ui, server = server)
