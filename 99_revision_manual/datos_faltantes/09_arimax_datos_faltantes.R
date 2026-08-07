#############################
###
###
### Ejemplo ARIMAX
### Prod Industrial
### EMM-DANE
###

library(tseries)
library(forecast)
library(FitAR)
library(dynlm)
library(car)
library(TSA)
library(highcharter)
library(dplyr)
####### ARIMAX


#baseb <- read.delim("/cloud/project/based.txt")

based1 <- read_table2("SARIMAX/based.txt")
based1


baset <- ts(based1,start=c(2001,1),freq=12)
View(baset)


head(baset)
plot(baset)
hchart(baset)

colnames(baset)

#View(baset)
### 1. Identificación

plot(baset[,"prodin"],col="red")
lines(baset[,"ventreal"],col="blue")
lines(baset[,"emptot"],col="green")


par(mfrow=c(1,3))
plot(log(baset[,"prodin"]))
acf(log(baset[,"prodin"]),lag.max=40)
pacf(log(baset[,"prodin"]),lag.max=40)



##### ¿ Es estacionaria ?
adf.test(log(baset[,"prodin"]))   #Dickey Fuller La serie no es tacionaria
pp.test(log(baset[,"prodin"]))   # Phillips-Perron.  La serie es estacionaria     

## Pruebas de estacionariedad con una diferencia
pp.test(diff(log(baset[,"prodin"])))  # la serie es estacionaria
adf.test(diff(log(baset[,"prodin"]))) # La serie es estacionaria


auto.arima(baset[,"prodin"])


par(mfrow=c(3,3))
plot(log(baset[,"prodin"]))
acf(log(baset[,"prodin"]),lag.max=40)
pacf(log(baset[,"prodin"]),lag.max=40)
plot(diff(log(baset[,"prodin"]),1))
acf(diff(log(baset[,"prodin"]),1),lag.max=24)
pacf(diff(log(baset[,"prodin"]),1),lag.max=24)
plot(diff(diff(log(baset[,"prodin"]),1)))
acf(diff(diff(log(baset[,"prodin"]),1)),lag.max=24)
pacf(diff(diff(log(baset[,"prodin"]),1)),lag.max=24)

## aumenta la variabilidad
sd(diff(baset[,"prodin"]))
sd(diff(diff(baset[,"prodin"],12)))



ccf(baset[,"prodin"],baset[,"ventreal"],lag.max=48)
ccf(baset[,"prodin"],baset[,"emptot"],lag.max=48)


a=prewhiten(as.numeric(baset[,"prodin"]),as.numeric(baset[,"ventreal"]),main='x & y',ylab='CCF')

b=prewhiten(as.numeric(baset[,"prodin"]),as.numeric(baset[,"emptot"]),main='x & y',ylab='CCF')

View(baset)


### 2. Estimación 

xreg1 <- baset[,c(2:3)]

Lagt <- function(x,k){
  n<-length(x)
  x1<- matrix(0,n)
  for(i in (k+1):n){
    x1[i] <- x[i-k] 
  }
  return(x1) 
}


x1<-Lagt(log(baset[,"ventreal"]),1) # 
x3<-Lagt(log(baset[,"emptot"]),1)


xreg2 <- data.frame(cbind(x1,x3))

head(xreg2)

yt <- baset[,"prodin"]
modelo1 <- TSA::arimax(log(yt), order=c(14,1,10), 
                       xreg = xreg2, fixed = c(0,0,0,NA,0,0,0,0,0,0,0,0,0,NA,
                                               NA,NA,0,0,0,0,0,0,0,NA,
                                               NA,NA))
modelo1
BIC(modelo1)
modelo1$coef[which(modelo1$coef!=0)] / sqrt(diag(modelo1$var.coef))



####################### Modelo 2

xregmod2 <- x1
yt <- baset[,"prodin"]
modelo2 <- TSA::arimax(log(yt), order=c(14,1,10), 
                       xreg = xregmod2)
modelo2
BIC(modelo2)
modelo2$coef[which(modelo2$coef!=0)] / sqrt(diag(modelo2$var.coef))




### 3. Diagnóstico

et <- residuals(modelo1)
yfit <- log(yt)-et

Box.test(et,lag=24,type="Ljung-Box")
jarque.bera.test(et)

runs.test(as.factor(sign(et)))

par(mfrow=c(2,2))
plot(yfit, type="l", col="red", lty=2, lwd=2)
lines(log(yt),col="blue")
qqPlot(et)
acf(et)
pacf(et)

### 4. pronostico

newxreg1 <- matrix(log(baset[dim(baset)[1],c(2:3)]),1,2)
colnames(newxreg1) <- colnames(xreg2)
pred <- predict(modelo1, n.ahead=12, newxreg = newxreg1)
exp(pred$pred)
exp(pred$pred - 2*pred$se)
exp(pred$pred + 2*pred$se)


plot(yfit, type="l", col="red", lty=2, lwd=2 ,xlim=c(2000,2021))
lines(log(yt),col="blue")
lines(pred$pred, col="green")



tail(baset)
##############################
#### Ejercicio 
####

data("USeconomic")
View(USeconomic)

#### Ajustar un modelo ARIMAX
#### para data(USeconomic)
#### del paquete "tseries"
#### Ajuste: log(M1)
#### Covariables: log(GNP),rs, rl
#### 1. Mejor modelo por BIC
#### 2. Cuales rezagos de las Covariables
####    ayudan a predecir la respuesta
####    usar ccf
#### 2. Pronostique 4 Trimestres
####
##################################

data(USeconomic)
View(USeconomic)

