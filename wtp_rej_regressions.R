library(lme4)
library(lmerTest)
library(Rcpp)
library(Matrix)

getwd()

setwd("/Users/jordansiegel/Documents/Github/WTP_Rejection_Choice/")

install.packages("lme4", dependencies=TRUE)
install.packages("Rcpp", dependencies=TRUE)
install.packages("lmerTest", dependencies=TRUE)
install.packages("Matrix", dependencies=TRUE)

wtp_rej_longdata<-read.csv(file="longformdata.csv",header=TRUE, sep=',')

condition_choicetype <- glm(formula = socialchoice ~ condition_recode, family=binomial,data=wtp_rej_longdata)
