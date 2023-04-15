# ejercicio simple de ajuste armax

library(forecast)
library(TSA)
library(dynlm)

uno <- read.csv("/cloud/project/SARIMAX/armax1.dat", sep="")

#uno = read.table("armax1.dat", header=TRUE)
x = uno$x
y = uno$y

x = ts(x, frequency = 12)
y = ts(y, frequency = 12)

yx = ts.intersect(x,y)
yx = na.omit(yx)

# grafica de ambas series

plot(yx,yax.flip=TRUE,main='') 

# una exploracion ingenua inicial

par(mfrow = c(2,2))
plot(lag(x,-3), y)
abline(lm(y ~ lag(x,-3)),col = "red")

plot(lag(x,-2), y)
lines(lowess(y ~ lag(x,-2) , f=0.8), col="blue")

plot(lag(x,-2), lag(y,-1))
lines(lowess(lag(y,-1) ~ lag(x,-3) , f=0.8), col="blue")

plot(lag(x,-3), lag(y,-1))
lines(lowess(lag(y,-1) ~ lag(x,-3) , f=0.8), col="blue")

# la correlacion cruzada antes de preblanqueo

par(mfrow = c(1,1))

ccf(as.numeric(yx[,1]),as.numeric(yx[,2]),main='x & y',ylab='CCF')

# la correlacion despues de preblanqueo
prewhiten(as.numeric(yx[,1]),as.numeric(yx[,2]),ylab='CCF' )

# un posible modelo

m3 = dynlm(y ~ L(y, c(1,2)) +  L(x,c(1,2)) -1 )

coeftest(m3)

summary(m3)

anova(m3)

yhat = m3$fitted.values
et   = m3$residuals

# residuos y ajuste dentro de la muestra

par(mfrow = c(1,1))

plot(y,type = 'b', col='red')
lines(yhat,col = 'blue')

par(mfrow = c(2,1))

acf(et)
pacf(et)


# problemas con funcion arima: no pronostica...      

m2 = arima(y,order = c(2,0,0), xreg =  lag(x,-1))

pron = predict(m2,n.ahead = 10)
xhat = pron$pred


# la version arimax de arima

m1=arimax(y,
          order = c(1,0,0),
          xtransf = x,
          transfer = list(c(2,1)),
          method='ML')

