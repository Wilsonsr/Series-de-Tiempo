################
# # SARIMAX
################
library(TSA)
library(tseries)
library(forecast)
library(FitAR)
library(dynlm)
library(car)
library(TSA)
library(urca)


#########  funciones de ayuda ##################
#Funcion 1
plotserie = function(data){
  par(mfrow = c(2,3))
  plot(data)
  stats::acf(data)
  stats::pacf(data)
  
  plot(diff(data))
  abline(h=2*sd(diff(data)), col = "red")
  abline(h=-2*sd(diff(data)), col = "red")
  stats::acf(diff(data))
  stats::pacf(diff(data))
}

#funcion2
plotserieciclo = function(data, s) {
  par(mfrow = c(1,3))
  plot(diff(data, s))
  abline(h=2*sd(diff(data,s)), col = "red")
  abline(h=-2*sd(diff(data,s)), col = "red")
  stats::acf(diff(data,s))
  stats::pacf(diff(data,s))
}


#funcion3
plotresiduos = function(residuos, data) {
  par(mfrow = c(2,2))
  yfit = data - residuos
  plot(yfit, type="l", col="red", lty = 2)
  lines(data, col="blue")
  qqPlot(et)
  acf(et)
  pacf(et) 
}

#funcion 4
ttest = function(modelo) {
  return(modelo$coef[which(modelo$coef!=0)] / sqrt(diag(modelo$var.coef)))
}

#Funcion5
Lagtp = function(x, k){
  n = length(x)
  x1 = matrix(0, n)
  for (i in (k+1):n) {
    x1[i] = x[i-k]
  }
  return(x1)
}

#Funcion6
Lagt = function(x, k){
  n = length(x)
  x1 = matrix(0, n, k)
  for (j in 1:k){
    for (i in (j+1):n) {
      x1[i,j] = x[i-j]
    }
  }
  return(x1)
}


#### FASE 1: IDENTIFICACION ####
baset_raw <- read.delim("SARIMAX/pib.csv")
#View(baset_raw)
dim(baset_raw)




baset = ts(baset_raw, start=c(2001,1),  freq = 4)

PIB = baset[,"PIB"]  #PIB=baset[,10]
colnames(baset) # nombre de las columnas


autoplot(PIB, )
plot(baset)



plotserie(PIB) # función creada arriba



hchart(PIB)


pp.test(PIB)    # Phillips-Perron
adf.test(PIB)  #Dickey Fuller



sd(diff(PIB))
sd(diff(diff(PIB),4))

# La variabilidad aumento, 
# no es recomendable usar una serie estacional


pp.test(diff(PIB))   # La serie estacionaria
adf.test(diff(PIB))  # La serie estacionaria

#########################3
xreg1 = baset[,c(1:9)] # sacamos las series de tiempo de la 1 a la 9 (no se incluye PIB)
View(xreg1)




xreg1
colnames(xreg1)

auto.arima(PIB)

##########################################
modelo1 = arima(PIB, order = c(0,1,4),
                 season = list(order = c(0,0,0), 
                               freq = 4),
                 xreg = xreg1)    # TODAS LAS VARIAVLES
BIC(modelo1)      #-547.533

ttest(modelo1)     # FUNCION DE ayuda creada arriba


############################################
modelo$coef[which(modelo$coef!=0)] / sqrt(diag(modelo$var.coef))

tt <- modelo1$coef[which(modelo1$coef!=0)]/sqrt(diag(modelo1$var.coef))
1 - pt(abs(tt),(modelo1$nobs - length(modelo1$coef[which(modelo1$coef!=0)])))


################# Modelo 2

modelo2 = arima(PIB, order = c(0,1,1),
                 season = list(order = c(0,0,0), 
                               freq = 4),
                 xreg = xreg1)   #  con todas las variable sin rezagar
BIC(modelo2) #-556.7664
ttest(modelo2)



tt <- modelo2$coef[which(modelo1$coef!=0)]/sqrt(diag(modelo1$var.coef))
1 - pt(abs(tt),(modelo2$nobs - length(modelo2$coef[which(modelo1$coef!=0)])))



#############################
et <- residuals(modelo2)
Box.test(et,lag=24,type="Ljung-Box")
jarque.bera.test(et)
plotresiduos(et, PIB) # función creada arriba


# modelo 3: Sector financiero rezagado
xreg2 = baset[, "FINAN"]
View(xreg2)
par(mfrow=c(2,1))
plot(PIB)
plot(xreg2)


xlag = Lagt(xreg2, 4) # FUNCION ARRIBA 6
xlag

####
xxlag=Lagtp(xreg2,4)
xxlag

modeloxxx = arima(PIB, order = c(0,1,1),
                season = list(order = c(0,0,0), 
                              freq = 4),
                xreg = xlag)

BIC(modeloxxx)
####
############################

modelo3 = arima(PIB, order = c(0,1,1),
                 season = list(order = c(0,0,0), 
                               freq = 4),
                 xreg = xlag)
BIC(modelo3) #-327.0935

ttest(modelo3)
tt3 <- modelo3$coef[which(modelo1$coef!=0)]/sqrt(diag(modelo3$var.coef))
1 - pt(abs(tt3),(modelo3$nobs - length(modelo3$coef[which(modelo3$coef!=0)])))





et <- residuals(modelo3)
Box.test(et,lag=24,type="Ljung-Box")  #pvalue= 0.008
jarque.bera.test(et)
plotresiduos(et, PIB)

# modelo 4: Sector financiero hace 4 periodos
FINAN4 = Lagtp(baset[, "FINAN"], 4) 

# función creada arriba
modelo4 = arima(PIB, order = c(0,1,1),
                 season = list(order = c(0,0,0), 
                               freq = 4),
                 xreg = cbind(xreg1, FINAN4))
BIC(modelo4) #-552.72
ttest(modelo4)
tt4 <- modelo4$coef[which(modelo4$coef!=0)]/sqrt(diag(modelo4$var.coef))
1 - pt(abs(tt4),(modelo4$nobs - length(modelo4$coef[which(modelo4$coef!=0)])))



et <- residuals(modelo4)
Box.test(et,lag=24,type="Ljung-Box")
jarque.bera.test(et)
plotresiduos(et, PIB)


# Correlación cruzada
par(mfrow = c(1,1))
b<-ccf( baset[,"FINAN"], PIB, lag.max =20)


?prewhiten
prewhiten(baset[,"FINAN"], PIB)

#############################################################
# Modelo                       # BIC     # LB    # JB    # e_t #
#                              #         #       #       #     #
# 1: SARIMAX(0,1,4)x(0,0,0)_4  # -547.53 #       #       #     #
# 2: SARIMAX(0,1,1)x(0,0,0)_4  # -556.77 # 92.1% # 99.8% # ok  #
# 3: SARIMAX(0,1,7)x(1,1,0)_4  # -115.89 # 86.8% # 46%   # ok  #
#############################################################
modelo2
BIC(modelo2)


#####

