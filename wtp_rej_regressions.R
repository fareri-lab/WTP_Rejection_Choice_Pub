getwd()

setwd("/Users/jordansiegel/Documents/Github/WTP_Rejection_Choice/")

install.packages("lme4", dependencies=TRUE)
install.packages("Rcpp", dependencies=TRUE)
install.packages("lmerTest", dependencies=TRUE)
install.packages("Matrix", dependencies=TRUE)
install.packages("lmer", dependencies=TRUE)
install.packages("effsize", dependencies=TRUE)

library(lme4)
library(lmerTest)
library(Rcpp)
library(Matrix)
library(ggplot2)
library(ggplot2)
library(dplyr)
library(tidyr)
library(effsize)





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
  theme(panel.grid = element_blank(),
        axis.title.x = element_text(size = 18, face = "bold"),
        axis.title.y = element_text(size = 18, face = "bold"),
        axis.text.x = element_text(size = 16),
        axis.text.y = element_text(size = 16),
        legend.title = element_text(size = 16),
        legend.text = element_text(size = 14))  # Remove gridlines

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
  theme(panel.grid = element_blank(),
        axis.title.x = element_text(size = 18, face = "bold"),
        axis.title.y = element_text(size = 18, face = "bold"),
        axis.text.x = element_text(size = 16),
        axis.text.y = element_text(size = 16),
        legend.title = element_text(size = 16),
        legend.text = element_text(size = 14)) 

# Save the plot
ggsave("social_vs_nonsocial_choices_fixed.png", width = 8, height = 6, dpi = 300)

#hierarchical logistic regression for PSE with interaction of condition
PSE <- glmer(socialchoice ~ value_diff * condition + (1 + value_diff | participant),
               data = wtp_rej_longdata, family = binomial)
summary(PSE)

# Assign the coefficients
b0 <- 0.32937
b1 <- -69.19869
b2 <- -0.02595
b3 <- -1.61406

# Compute condition-specific PSEs
pse_accept <- - (b0 - b2) / (b1 - b3)
pse_reject <- - (b0 + b2) / (b1 + b3)

# Print them
pse_accept
pse_reject


#re-run with centering
wtp_rej_longdata <- wtp_rej_longdata %>%
  mutate(value_diff_centered = value_diff - mean(value_diff, na.rm = TRUE))

model_centered <- glmer(
  socialchoice ~ value_diff_centered * condition_recode + (1 + value_diff_centered | participant),
  data = wtp_rej_longdata,
  family = binomial
)

summary(model_centered)

b0 <- 0.33595
b1 <- -69.22584
b2 <- -0.02581
b3 <- -1.61493

pse_accept <- -(b0 - b2) / (b1 - b3)
pse_reject <- -(b0 + b2) / (b1 + b3)

pse_accept
pse_reject








# Step 1: Fit logistic regression per participant per condition
pse_df <- wtp_rej_longdata %>%
  group_by(participant, condition_recode) %>%
  do({
    mod <- try(glm(socialchoice ~ value_diff, data = ., family = binomial), silent = TRUE)
    
    if (inherits(mod, "try-error")) {
      data.frame(pse = NA)
    } else {
      coefs <- coef(mod)
      intercept <- coefs[1]
      slope <- coefs[2]
      pse <- -intercept / slope
      data.frame(pse = pse)
    }
  }) %>%
  ungroup()

# Convert condition codes to descriptive names
pse_wide <- pse_df %>%
  mutate(condition_recode = ifelse(condition_recode == -1, "acceptance", "rejection")) %>%
  pivot_wider(names_from = condition_recode, values_from = pse, names_prefix = "pse_") %>%
  mutate(pse_diff = pse_rejection - pse_acceptance)

# Paired Cohen's d on the difference in PSEs
cohen_result <- cohen.d(pse_wide$pse_rejection, pse_wide$pse_acceptance, paired = TRUE)
print(cohen_result)

head(pse_wide)








#This version shows each participant's values, with a line connecting them:

# Gather into long format to plot with lines
pse_long <- pse_wide %>%
  select(participant, pse_acceptance, pse_rejection) %>%
  pivot_longer(cols = starts_with("pse_"), names_to = "condition", values_to = "pse") %>%
  mutate(condition = ifelse(condition == "pse_acceptance", "Acceptance", "Rejection"))

pse_long <- pse_long %>%
  mutate(participant = as.factor(participant))

# Line plot per participant
ggplot(pse_long, aes(x = condition, y = pse, group = participant)) +
  geom_line(alpha = 0.3, color = "#0072B2") +
  geom_point(alpha = 0.6, color = "#0072B2") +
  labs(
    title = "Participant-Level PSEs Across Conditions",
    x = "Condition",
    y = "Point of Subjective Equivalence (PSE)"
  ) +
  theme_minimal(base_size = 14)





