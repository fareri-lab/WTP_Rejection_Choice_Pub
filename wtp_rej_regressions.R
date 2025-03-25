getwd()

setwd("/Users/jordansiegel/Documents/Github/WTP_Rejection_Choice/")

install.packages("lme4", dependencies=TRUE)
install.packages("Rcpp", dependencies=TRUE)
install.packages("lmerTest", dependencies=TRUE)
install.packages("Matrix", dependencies=TRUE)
install.packages("lmer", dependencies=TRUE)

library(lme4)
library(lmerTest)
library(Rcpp)
library(Matrix)
library(ggplot2)
library(dplyr)


wtp_rej_longdata<-read.csv(file="longformdata.csv",header=TRUE, sep=',')

wtp_rej_shortdata<-read.csv(file="shortformdata.csv",header=TRUE, sep=',')

#re-code acceptance from 2 to -1 for condition_recode and males from 0 to -1 in sex
wtp_rej_longdata$condition_recode[wtp_rej_longdata$condition_recode==2]<- -1
wtp_rej_longdata$sex[wtp_rej_longdata$sex==0]<- -1

#re-code acceptance from 2 to -1 for condition_recode and males from 0 to -1 in sex
wtp_rej_shortdata$condition_recode[wtp_rej_longdata$condition_recode==2]<- -1
wtp_rej_shortdata$sex[wtp_rej_longdata$sex==0]<- -1



# Create prop_nonsocialchoice as the absolute difference from 1
wtp_rej_shortdata <- wtp_rej_shortdata %>%
  mutate(prop_nonsocialchoice = abs(prop_socialchoice - 1))

wtp_rej_longdata <- wtp_rej_longdata %>%
  mutate(prop_nonsocialchoice = abs(prop_socialchoice - 1))

# Check if the column was created correctly
head(wtp_rej_shortdata)

#create seperate variables with values for within each condition
# Subset data where condition_recode == 1
rej <- wtp_rej_shortdata %>%
  filter(condition_recode == 1) %>%
  as.data.frame()  # Ensure it's a data frame if needed

# Subset data where condition_recode == 2
acc <- wtp_rej_shortdata %>%
  filter(condition_recode == -1) %>%
  as.data.frame()

# Subset data where condition_recode == 1
rej_long <- wtp_rej_longdata %>%
  filter(condition_recode == 1) %>%
  as.data.frame()  # Ensure it's a data frame if needed

# Subset data where condition_recode == 2
acc_long <- wtp_rej_longdata %>%
  filter(condition_recode == -1) %>%
  as.data.frame()

# Run a paired t-test
rej_acc_decisionprice <- t.test(rej$social_decisionprice_mean, 
                                acc$social_decisionprice_mean, 
                                paired = TRUE, 
                                alternative = "two.sided")

# Print the results
print(rej_acc_decisionprice)


colnames(wtp_rej_longdata)[colnames(wtp_rej_longdata) == "order"] <- "order_var"

condition_choicetype <- glm(formula = socialchoice ~ condition_recode, family=binomial,data=wtp_rej_longdata)

saliencecondition_choicetype_withregressors <- glm(formula = socialchoice ~ condition_recode + + salience_mean+ age + stress_mean+ sex + order_var +timebetween, family=binomial,data=wtp_rej_longdata)

condition_choiceprice <- lmer(formula = decision_price ~ condition_recode +  (1 | participant), data = wtp_rej_longdata)

condition_choiceprice_withregressors <- lmer(decision_price ~ condition_recode + age + order_var + sex + timebetween + (1 | participant),
                                             data = wtp_rej_longdata)

affect_choicetype <- glm(formula = socialchoice ~ stress_mean, family=binomial,data=wtp_rej_longdata)

affect_choicetype_withregressors <- glm(formula = socialchoice ~ stress_mean + age + sex +order_var +timebetween, family=binomial,data=wtp_rej_longdata)

affect_choiceprice <- lmer(formula = decision_price ~ stress_mean +  (1 | participant), data = wtp_rej_longdata)

interaction_choicetype_withregressors <- glm(formula = socialchoice ~ condition_recode * stress_mean + age + sex +order_var +timebetween, family=binomial,data=wtp_rej_longdata)

salienceinteraction_choicetype_withregressors <- glm(formula = socialchoice ~ condition_recode * salience_mean + age + sex +order_var +timebetween, family=binomial,data=wtp_rej_longdata)

saliencestressinteraction_choicetype_withregressors <- glm(formula = socialchoice ~ stress_mean * salience_mean + age + condition_recode+ sex +order_var +timebetween, family=binomial,data=wtp_rej_longdata)


library(ggplot2)
library(dplyr)

# Function to calculate Standard Deviation safely
safe_sd <- function(x) {
  if (length(na.omit(x)) > 1) {
    return(sd(x, na.rm = TRUE))
  } else {
    return(NA)
  }
}

# ✅ Correct Filtering: Rejection = 1, Acceptance = -1
rej_long <- wtp_rej_longdata %>% filter(condition_recode == 1)   # Rejection
acc_long <- wtp_rej_longdata %>% filter(condition_recode == -1)  # Acceptance

# Compute Mean Decision Price for Each Condition
mean_data <- wtp_rej_longdata %>%
  group_by(condition_recode) %>%
  summarise(
    mean_spent = mean(social_decisionprice_mean, na.rm = TRUE),
    .groups = "drop"
  )

# Compute SD separately for Rejection and Acceptance
sd_rej <- safe_sd(rej_long$social_decisionprice_mean)
sd_acc <- safe_sd(acc_long$social_decisionprice_mean)

# ✅ Debugging: Ensure SDs exist
print(paste("SD for Rejection:", sd_rej))
print(paste("SD for Acceptance:", sd_acc))

# ✅ Assign SD values correctly
summary_data <- mean_data %>%
  mutate(
    sd_spent = c(sd_rej, sd_acc),  # ✅ Correct order of SD assignment
    condition_recode = factor(condition_recode, levels = c(1, -1), labels = c("Rejection", "Acceptance"))  # ✅ Correct ordering
  )

# ✅ Debugging: Check if both conditions appear
print(summary_data)

# ✅ Plot with Corrected Data
ggplot(summary_data, aes(x = condition_recode, y = mean_spent, fill = condition_recode)) +
  geom_bar(stat = "identity", position = position_dodge(), color = "black", alpha = 0.8) +  # Slightly transparent bars
  geom_errorbar(aes(ymin = mean_spent - sd_spent, ymax = mean_spent + sd_spent), 
                width = 0.1, position = position_dodge(.9), color = "black", size = 0.8) +  # Corrected error bars
  scale_fill_manual(name = "Condition", values = c("Rejection" = "#88CCEE", "Acceptance" = "#DDCC77")) +  # Custom colors
  labs(
    x = "Social Condition",
    y = "Amount Spent on Social"
  ) +
  theme_minimal() +
  theme(panel.grid = element_blank())  # Remove gridlines

# Save the plot
ggsave("avgspent_social_rejvacc_plot_fixed.png", width = 8, height = 6, dpi = 300)


# Run a paired t-test
overall_propsoc <- t.test(rej$prop_socialchoice, 
                          rej$prop_nonsocialchoice, 
                          paired = TRUE, 
                          alternative = "two.sided")

# Print the results
print(overall_propsoc)

# Function to calculate Standard Error of the Mean (SEM)
safe_se <- function(x) {
  if (length(na.omit(x)) > 1) {
    return(sd(x, na.rm = TRUE) / sqrt(sum(!is.na(x))))
  } else {
    return(NA)
  }
}

# Compute SEM separately for prop_socialchoice and prop_nonsocialchoice from the rej dataframe
sem_social <- safe_se(rej$prop_socialchoice)
sem_nonsocial <- safe_se(rej$prop_nonsocialchoice)

# Compute Means for Social and Non-Social Choices from the rej dataframe
summary_data <- data.frame(
  Choice_Type = c("Social", "Non-Social"),
  mean_prop = c(mean(rej$prop_socialchoice, na.rm = TRUE), 
                mean(rej$prop_nonsocialchoice, na.rm = TRUE)),
  sem = c(sem_social, sem_nonsocial)  # Assign calculated SEMs
)

# Print summary data to verify SEM values
print(summary_data)

# Create the Bar Plot with Correct SEM-based Error Bars
ggplot(summary_data, aes(x = Choice_Type, y = mean_prop, fill = Choice_Type)) +
  geom_bar(stat = "identity", position = position_dodge(), color = "black", alpha = 0.9) +  # Bars with outline
  geom_errorbar(aes(ymin = mean_prop - sem, ymax = mean_prop + sem), 
                width = 0.1, position = position_dodge(.9), color = "black", size = 0.8) +  # Corrected SEM error bars
  scale_fill_manual(name = "Choice Type", values = c("Social" = "#88CCEE", "Non-Social" = "#DDCC77")) +  # Custom colors
  labs(
    x = "Choice Type",
    y = "Proportion of Choices",
    title = ""
  ) +
  theme_minimal()+
  theme(panel.grid = element_blank()) 

# Save the plot
ggsave("social_vs_nonsocial_choices_fixed.png", width = 8, height = 6, dpi = 300)
