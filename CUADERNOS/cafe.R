library(car)
library(urca)
library(forecast)
library(tseries)
library(readxl)
library(readxl)
library(rio)
library(TSstudio)
library(highcharter)

#Producción registrada - Mensual			
#Miles de sacos de 60 Kg de café verde equivalente 			


cafe <- rio::import("https://github.com/Wilsonsr/Series-de-Tiempo/raw/main/bases/cafe.xlsx")

z1<- ts(cafe[,2], start = c(2000,1), end=c(2023,12), frequency = 12)

class(z1)
start(z1)
end(z1)
length(z1)


summary(z1)

ts_plot(z1)

ts_decompose(z1)

ts_seasonal(z1, type="all")

ts_heatmap(z1)
### Identificaci?n
###
hchart(z1)


par(mfrow=c(4,3))
plot(z1,type="o")
acf(z1, lag.max=40)
pacf(z1, lag.max=40)
plot(diff(z1),type="o")
abline(h=2*sqrt(var(diff(z1))),col="red",lty=2)
abline(h=-2*sqrt(var(diff(z1))),col="red",lty=2)
acf(diff(z1), lag.max=40)
pacf(diff(z1), lag.max=40)
plot(diff(z1,12),type="o")
acf(diff(z1,12), lag.max=40)
pacf(diff(z1,12), lag.max=40)
plot(diff(diff(z1,12)),type="o")
acf(diff(diff(z1,12)), lag.max=40)
pacf(diff(diff(z1,12)), lag.max=40)


### Test DF sobre la serie
### desestacionalizada


## Dickey Fuller sobre z1
plot(ur.df(z1,type="none",lag=10))
summary(ur.df(z1,type="none",lag=10))

adf.test(z1)


###  Dickey Fuller

plot(ur.df(diff(z1),type="none",lag=10))
summary(ur.df(diff(z1),type="none",lag=10))


#####
plot(ur.df(diff(z1,12),type="none",lag=10))
summary(ur.df(diff(z1,12),type="none",lag=10))



plot(ur.pp(diff(z1,12),type="Z-tau",
           model="constant", lags="long"))
summary(ur.pp(diff(z1,12),type="Z-tau",
              model="constant", lags="long"))


######### d=1  y   D=1
plot(ur.df(diff(diff(z1,12)),type="none",lag=10))
summary(ur.df(diff(diff(z1,12)),type="none",lag=10))





ts_cor(diff(diff(z1,12)), lag.max = 40)

ts_cor(diff(z1,12), lag.max = 40)


### Ajuste del Modelo

modelo1<-stats::arima(z1,
                      order=c(6,0,0), 
                      seasonal=list(order=c(0,1,1),
                                    period=12), fixed=c(NA,NA,NA,NA,NA,NA,NA)) 
modelo1
tt <- modelo1$coef[which(modelo1$coef!=0)]/sqrt(diag(modelo1$var.coef))
1 - pt(abs(tt),(modelo1$nobs - length(modelo1$coef[which(modelo1$coef!=0)])))
BIC(modelo1)

### Diagn?stico

et<-residuals(modelo1)
x1.fit <- fitted(modelo1)

par(mfrow=c(3,2))
plot(z1,type="l",lty=2)
lines(x1.fit,type="l",col="red")
plot(scale(et),type="l",main="Residuales")
abline(h=2*sqrt(var(scale(et))),col="red",lty=2)
abline(h=-2*sqrt(var(scale(et))),col="red",lty=2)
acf(et)
pacf(et)
qqPlot(scale(et))
acf(abs(et)) #Mide Estructura Heteroced?stica

## Test de Autocorrelacion de Ljung-Box
## Ho: r1=r2=r3=...=rlag=0
## Ha: Al menos una es dif de cero
tsdiag(modelo1, gof.lag = 20)

length(z1)
log(length(z1))

Box.test(et,lag=6,type="Ljung-Box")
#Box.test(abs(et),lag=20,type="Ljung-Box")

## Test de Normalidad basado en
## Sesgo y Curtosis
## Ho: Datos provienen de una Dist. Normal
## Ha: Los datos no provienen de una Dist. Normal

jarque.bera.test(et)

## Test de Aleatoriedad
## Ho: Residuales exhiben un comport. de Aleatoriedad
## Ha: Residuales no exhiben estructura (Tendencia, o cualquier otro 
##     comportamiento predecible)

runs.test(as.factor(sign(et)), alternative="two.sided")


#### Pron?stico Fuera Muestra

plot(forecast(modelo1,h=7, fan=T))
lines(fitted(modelo1), col="red")

####################################################

pronostico=  forecast(modelo1,h=7)[4]$mean
pronostico

Reales= consumo[277:283,4]
Reales

library(Metrics)
library(MLmetrics)

mae(Reales, pronostico)

RMSE(pronostico, Reales)

MAPE(pronostico, Reales)
mape(Reales,pronostico)
