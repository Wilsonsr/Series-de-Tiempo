#Librerias
library(car)
library(tseries)
library(urca)
library(highcharter)
library(TSstudio)
library(forecast)
library(rio)

### Caragar los datos

Caffeine=rio::import("https://github.com/Wilsonsr/Series-de-Tiempo/raw/main/bases/Caffeine.csv")
View(Caffeine)

z1=ts(Caffeine[,2])   #Formato serie de tiempo
z1

summary(z1)

### Grafico para la serie
plot(z1, main="Caffeine", ylab="Concentracion")
ts_plot(z1,color = "red",title = "Caffeine", Ytitle = "Concentración")
hchart(z1) %>%hc_add_theme(hc_theme_darkunica())

###### Identificacion
par(mfrow=c(2,3))
plot(z1)
acf(z1, lag.max = 40)
pacf(z1, lag.max = 40)
plot(diff(z1))
abline(h=2*sqrt(var(diff(z1))), col="red", lty=2  )
abline(h=-2*sqrt(var(diff(z1))), col="red", lty=2  )
acf(diff(z1), lag.max = 40)
pacf(diff(z1), lag.max = 40)

### Pruebas de Raíz Unitaria 
### Dickey- Fuller    y  Phillips Perron

#Ho:  z1  es no estacionaria
# Ha: z1 es estacionaria


adf.test(z1)
# p-value = 0.4918
# Conclusion z1 no es estacionaria

pp.test(z1) # serie es estacionaria

# Pruebas dde Dickey Fuller y Phillips Perron
# serie diferenciada

adf.test(diff(z1))
# p-value = 0.01

#Al differenciar la serie ya es estacionaria

pp.test(diff(z1))
# p-value = 0.01

ts_cor(diff(z1), lag.max = 40)

## ARIMA(0,1,5)
## ARIMA(0,1,8)
## ARIMA(0,1,11)
## ARIMA(5,1,0)
## ARIMA(6,1,0)
## ARIMA(10,1,0)
## ARIMA(6,1,5)
## ARIMA(6,1,8)
## ARIMA(10,1,11)

#### Estimacion

modelo1 = stats::arima(z1, order = c(0,1,8),
                       fixed = c(NA,NA,NA,NA,NA,NA,NA,NA))

modelo1

tt=  modelo1$coef[which(modelo1$coef!=0)]/sqrt(diag(modelo1$var.coef))
1-pt(abs(tt), (modelo1$nobs - length(modelo1$coef[which(modelo1$coef!=0)])))

BIC(modelo1)

### Diagnostico

et=residuals(modelo1)
z1.fit= z1-et
fitted(modelo1)

par(mfrow=c(3,2))
plot(z1)
lines(z1.fit, col="red", lty=2)
plot(scale(et), type="l")
abline(h=2*sqrt(var(scale(et))), col="red", lty=2)
abline(h=-2*sqrt(var(scale(et))), col="red", lty=2)
acf(scale(et),lag.max = 20)
pacf(scale(et),lag.max = 20)
qqPlot(et)
acf(abs(et))


#### Test Ljun Box

#Ho: r1=r2=....rlag=0                    
# Ha:  al menos uno es diferente de cero

#Ho:  Ausencia de correlación serial
#Ha  Hay correlación serial en los residuales


#### OBJETIVO:  NO RECHAZAR

Box.test(et, lag=6,type = "Ljung-Box")
#p-value = 0.02093   Rechazamos Ho
tsdiag(modelo1,  gof.lag = 20)



### Prueba de Normalidad
# Ho: Los residuales se distribuyen normal
#Ha: Los residuales se  No se distribuyen normal

jarque.bera.test(et)
#p-value = 0.0001379


##### Test de Aleatoriedad  Run Test
#Ho Los residuales son aleatorios
#Ho Los residuales no son aleatorios

runs.test(as.factor(sign(et)), alternative ="two.sided" )
#p-value = 0.07992


### PRONOSTICO

plot(forecast(modelo1, h=6, fan=T))
lines(fitted(modelo1), col="red")









