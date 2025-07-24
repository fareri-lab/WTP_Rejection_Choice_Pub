getwd()


install.packages("sjPlot")
install.packages("lmertest")
install.packages("tidyverse")


library(lme4)
library(lmerTest)
library(tidyverse)
library(Rcpp)
library(Matrix)
library(ggplot2)
library(dplyr)
library(tidyr)
library(effsize)
library(sjPlot)
library(lmtest)
library(ggeffects)

setwd("/Users/jordansiegel/Documents/Github/WTP_Rejection_Choice/scoring")
rsq <- read.csv(file="rsq.csv", header =TRUE, sep = ',')

setwd("/Users/jordansiegel/Documents/Github/WTP_Rejection_Choice/")

wtp_rej_longdata<-read.csv(file="longformdata.csv",header=TRUE, sep=',')

wtp_rej_shortdata<-read.csv(file="shortformdata.csv",header=TRUE, sep=',')




#re-code acceptance from 2 to -1 for condition_recode and males from 0 to -1 in sex
wtp_rej_longdata$condition_recode[wtp_rej_longdata$condition_recode==2]<- -1
wtp_rej_longdata$sex[wtp_rej_longdata$sex==0]<- -1

#re-code acceptance from 2 to -1 for condition_recode and males from 0 to -1 in sex
wtp_rej_shortdata$condition_recode[wtp_rej_shortdata$condition_recode==2]<- -1
wtp_rej_shortdata$sex[wtp_rej_shortdata$sex==0]<- -1

#create anova dataframe


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

colnames(wtp_rej_longdata)[colnames(wtp_rej_longdata) == "order"] <- "order_var"

# Run a paired t-test
rej_acc_decisionprice <- t.test(rej$social_decisionprice_mean, 
                                acc$social_decisionprice_mean, 
                                paired = TRUE, 
                                alternative = "two.sided")

# Print the results
print(rej_acc_decisionprice)




condition_choicetype <- glm(formula = socialchoice ~ condition_recode, family=binomial,data=wtp_rej_longdata)

saliencecondition_choicetype_withregressors <- glm(formula = socialchoice ~ condition_recode + + salience_mean+ age + stress_mean+ sex + order_var +timebetween, family=binomial,data=wtp_rej_longdata)
summary(saliencecondition_choicetype_withregressors)
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

# Plot: Amount Spent on Social by Condition
amtspent <- ggplot(summary_data, aes(x = condition_recode, y = mean_spent, fill = condition_recode)) +
  geom_bar(stat = "identity", position = position_dodge(), color = "black", alpha = 0.8) +
  geom_errorbar(aes(ymin = mean_spent - sd_spent, ymax = mean_spent + sd_spent), 
                width = 0.1, position = position_dodge(.9), color = "black", size = 0.8) +
  scale_fill_manual(name = "Condition", values = c("Rejection" = "#FF6F61", "Acceptance" = "#88CCEE")) +
  labs(
    x = "Social Condition",
    y = "Amount Spent on Social"
  ) +
  theme_minimal() +
  theme(
    panel.grid = element_blank(),
    axis.title.x = element_text(size = 26, face = "bold", margin = margin(t = 25)),
    axis.title.y = element_text(size = 26, face = "bold", margin = margin(r = 25)),
    axis.text.x = element_text(size = 24, face = "bold"),
    axis.text.y = element_text(size = 24, face = "bold"),
    legend.title = element_text(size = 24, face = "bold"),
    legend.text = element_text(size = 22, face = "bold"),
    plot.margin = margin(t = 20, r = 20, b = 20, l = 30)
  )

# Save the plot
ggsave("avgspent_social_rejvacc_plot_fixed.png", plot = amtspent, width = 10, height = 8, dpi = 300)

#################################################


####################################
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

# 👇 Add this to set correct order: Social on the left, Non-Social on the right
summary_data$Choice_Type <- factor(summary_data$Choice_Type, levels = c("Social", "Non-Social"))


# Create the Bar Plot with Correct SEM-based Error Bars
propsoc_choicetype <- ggplot(summary_data, aes(x = Choice_Type, y = mean_prop, fill = Choice_Type)) +
  geom_bar(stat = "identity", position = position_dodge(), color = "black", alpha = 0.9) +  # Bars with outline
  geom_errorbar(aes(ymin = mean_prop - sem, ymax = mean_prop + sem), 
                width = 0.1, position = position_dodge(.9), color = "black", size = 0.8) +  # Corrected SEM error bars
  scale_fill_manual(name = "Choice Type", values = c("Social" = "#FF6F61", "Non-Social" = "#88CCEE")) +  # Custom colors
  labs(
    x = "Choice Type",
    y = "Proportion of Choices",
    title = ""
  ) +
  theme_minimal() +
  theme(
    panel.grid = element_blank(),
    axis.title.x = element_text(size = 26, face = "bold", margin = margin(t = 25)),
    axis.title.y = element_text(size = 26, face = "bold", margin = margin(r = 25)),
    axis.text.x = element_text(size = 24, face = "bold"),
    axis.text.y = element_text(size = 24, face = "bold"),
    legend.title = element_text(size = 24, face = "bold"),
    legend.text = element_text(size = 22, face = "bold"),
    plot.margin = margin(t = 20, r = 20, b = 20, l = 30)
  )

# Save the plot
ggsave("social_vs_nonsocial_choices_fixed.png", plot = propsoc_choicetype, width = 10, height = 8, dpi = 300)

#hierarchical logistic regression for PSE of social vs non social
PSE_notcondition <- glmer(socialchoice ~ value_diff + (1 + value_diff | participant),
             data = wtp_rej_longdata, family = binomial)

summary(PSE_notcondition)

#assign the coefficients
b0 <- 0.32973
b1 <- -69.19869

#compute overall PSE (logit=0)
pse<- -b0/b1
pse

# Define sequence of value differences to plot
value_diff_seq1 <- seq(-0.05, 0.05, length.out = 100)

# Create prediction data
pred_data1 <- data.frame(value_diff = value_diff_seq1) %>%
  mutate(
    linear_predictor = b0 + b1 * value_diff,
    predicted_prob = 1 / (1 + exp(-linear_predictor))
  )

PSE_plot1 <- ggplot(pred_data1, aes(x = value_diff, y = predicted_prob)) +
  geom_line(color = "#000000", size = 1.5) +
  geom_vline(xintercept = 0, linetype = "dashed", color = "gray40") +
  geom_point(aes(x = pse, y = 0.5), color = "black", size = 3, shape = 21, fill = "white") +
  annotate("text", x = pse, y = 0.55, label = paste0("PSE = ", round(pse, 4)), size = 6, fontface = "bold") +
  labs(
    x = "Value Difference",
    y = "Probability of Social Choice"
  ) +
  theme_classic(base_size = 14) +
  theme(
    panel.grid = element_blank(),
    axis.title.x = element_text(size = 26, face = "bold", margin = margin(t = 25)),
    axis.title.y = element_text(size = 26, face = "bold", margin = margin(r = 25)),
    axis.text.x = element_text(size = 24, face = "bold"),
    axis.text.y = element_text(size = 24, face = "bold"),
    axis.ticks.length = unit(6, "pt")
  )

# Save the plot
ggsave("PSE_plot_overall.png", plot = PSE_plot1, width = 10, height = 8, dpi = 300)

#hierarchical logistic regression for PSE with interaction of condition
PSE <- glmer(socialchoice ~ value_diff * condition_recode + (1 + value_diff | participant),
               data = wtp_rej_longdata, family = binomial)
summary(PSE)

# Assign the coefficients
b0 <- 0.32937
b1 <- -69.19869
b2 <- -0.02595
b3 <- -1.61406

# Compute condition-specific PSEs
#pse_accept <- - (b0 - b2) / (b1 - b3)
#pse_reject <- - (b0 + b2) / (b1 + b3)

pse_accept <- - (b0 + b2 * -1) / (b1 + b3 * -1)
pse_reject <- - (b0 + b2 * 1) / (b1 + b3 * 1)

# Print them
pse_accept
pse_reject


#plot PSE

value_diff_seq <- seq(-0.05, 0.05, length.out = 100)

# Coefficients from your model
b0 <- 0.32937
b1 <- -69.19869
b2 <- -0.02595
b3 <- -1.61406

# Build dataframe
pred_data <- expand.grid(
  value_diff = value_diff_seq,
  condition_recode = c(-1, 1)  # -1 = Acceptance, 1 = Rejection
)

# Calculate linear predictor manually
pred_data <- pred_data %>%
  mutate(
    condition_label = ifelse(condition_recode == -1, "Acceptance", "Rejection"),
    linear_predictor = b0 + b1 * value_diff + b2 * condition_recode + b3 * value_diff * condition_recode,
    predicted_prob = 1 / (1 + exp(-linear_predictor))  # logistic function
  )
  
PSE_plot <- (
  ggplot(pred_data, aes(x = value_diff, y = predicted_prob, color = condition_label)) +
    geom_line(size = 1.2) +
    geom_vline(xintercept = 0, linetype = "dashed", color = "gray40") +
    geom_point(data = data.frame(
      value_diff = c(pse_accept, pse_reject),
      predicted_prob = 0.5,
      condition_label = c("Acceptance", "Rejection")
    ), aes(x = value_diff, y = predicted_prob, color = condition_label),
    size = 3, shape = 21, fill = "white") +
    scale_color_manual(
      values = c("Acceptance" = "#88CCEE",
                 "Rejection" = "#FF6F61")
    ) +
    labs(
      title = "",
      x = "Value Difference",
      y = "Probability of Social Choice",
      color = "Condition"
    ) +
    theme_classic(base_size = 14) +
    theme(
      panel.grid = element_blank(),
      axis.title.x = element_text(size = 26, face = "bold", margin = margin(t = 25)),
      axis.title.y = element_text(size = 26, face = "bold", margin = margin(r = 25)),
      axis.text.x = element_text(size = 24,face = "bold"),
      axis.text.y = element_text(size = 24,face = "bold"),
      legend.title = element_text(size = 24,face = "bold"),
      legend.text = element_text(size = 22,face = "bold"),
      axis.ticks.length = unit(6, "pt")  # Default is around 5–6 pt, go smaller if you want
      
    )
)
# Save the plot
#ggsave("PSE_plot.png", PSE_plot, width = 6, height = 4, dpi = 300)
ggsave("PSE_plot_fixed.png", plot = PSE_plot, width = 10, height = 8, dpi = 300)



#run correlation of rsq with decision price in rejection condition

rsq <- rsq %>%
  rename(participant = Prolific_ID)

rej <- rej %>%
  left_join(rsq, by = "participant")

rej <- rej %>%
  mutate(rsq = unlist(rsq))

#regression decision price
condition_rsq <- condition_rsq <- lm(
  social_decisionprice_mean ~ RSQ_finalscore,
  data = rej
)
summary(condition_rsq)

wtp_rej_longdata <- wtp_rej_longdata %>%
  left_join(rsq, by = "participant")

#PSE analysis with RSQ included

PSE_withrsq <- glmer(
  socialchoice ~ value_diff * condition_recode * RSQ_finalscore + (1 + value_diff | participant),
  data = wtp_rej_longdata,
  family = binomial
)

summary(PSE_withrsq)

############################################ Mixed Effects Regression with PCA components below

setwd("/Users/jordansiegel/Documents/Github/WTP_Rejection_Choice/scoring")
pca_data<-read.csv(file='wtp_rej_PCA_allsubjects.csv',header=TRUE, sep=',')
# Rename Prolific_ID to participant in the PCA data frame
colnames(pca_data)[colnames(pca_data) == "Prolific_ID"] <- "participant"


colnames(wtp_rej_longdata)
colnames(pca_data)


# Merge PCA components into your main dataset
merged_data <- left_join(wtp_rej_longdata, pca_data, by = "participant")

condition_choiceprice_withpca <- lmer(decision_price ~ condition_recode + PC1 + PC2 + (1 | participant), data = merged_data)

condition_choiceprice_withpcaonly <- lmer(decision_price ~ + PC1 + PC2 + (1 | participant), data = merged_data)

condition_choicetype_withpca <- lmer(socialchoice ~ condition_recode + age + order_var + sex + timebetween + PC1 + PC2 + (1 | participant),data = merged_data)

condition_choicetype_withpcaonly <- lmer(socialchoice ~ condition_recode * PC1 + condition_recode* PC2 + value_diff + decision_price + (1 | participant), data = merged_data)

condition_choicetype_withpcaonly3way <- lmer(socialchoice ~ condition_recode + value_diff * PC1 * condition_recode + PC2 + (1 | participant), data = merged_data)

condition_choicetype_valuediff_int_withpcaonly <- lmer(socialchoice ~ 1+ value_diff * PC1 + condition_recode * PC1 + PC2 * condition_recode + (1 | participant), data = merged_data)

summary(condition_choicetype_withpcaonly3way)
summary(condition_choiceprice_withpca)
summary(condition_choicetype_withpca)
summary(condition_choiceprice_withpcaonly)
summary(condition_choicetype_withpcaonly)
summary(condition_choicetype_valuediff_int_withpcaonly)


model_interaction <- lmer(decision_price ~ condition_recode * (PC1 + PC2 + PC3) +
                            age + order_var + sex + timebetween + (1 | participant),
                          data = merged_data)
summary(model_interaction)

model_interaction_choicetype <- lmer(socialchoice ~ condition_recode * (PC1 + PC2 + PC3) +
                            age + order_var + sex + timebetween + (1 | participant),
                          data = merged_data)
summary(model_interaction_choicetype)

###running by models within conditions
merged_data_rej <- subset(merged_data, condition_recode == "1")
merged_data_acc <- subset(merged_data, condition_recode == "-1")

model_rej <- lmer(decision_price ~ PC1 + PC2 + PC3 + age + order_var + sex + timebetween + (1 | participant),
                data = merged_data_rej)
model_acc <- lmer(decision_price ~ PC1 + PC2 + PC3 + age + order_var + sex + timebetween + (1 | participant),
                data = merged_data_acc)
summary(model_rej)
summary(model_acc)

condition_valuediff_withpca <- lmer(decision_price ~ value_diff * condition_recode + PC1 + PC2 + PC3 + (1 + value_diff | participant), data = merged_data)

summary(condition_valuediff_withpca)

ggplot(merged_data, aes(x = PC1, y = value_diff)) +
  +     geom_smooth(method = "lm", se = TRUE, color = "blue") +
  +     labs(title = "Regression Line of Value Difference on PC1",
             +          x = "PC1", y = "Value Difference") +
  +     theme_minimal()

#################################### regression instead of ANOVA data frame
long_df <- wtp_rej_shortdata %>%
  pivot_longer(
    cols = c(social_decisionprice_total, nonsocial_decisionprice_total),
    names_to = "choice_source",
    values_to = "decisionprice_total"  # use a temporary unique name
  ) %>%
  mutate(
    choicetype = case_when(
      choice_source == "social_decisionprice_total" ~ 1,
      choice_source == "nonsocial_decisionprice_total" ~ 0
    ),
    condition_recode = recode(condition_recode, `1` = 1, `2` = -1)
  ) %>%
  select(participant, condition_recode, choice = decisionprice_total, choicetype) %>%
  arrange(participant, condition_recode, choicetype)

print(head(long_df, 10))

#run regression model:

twobytwo <- lm(choice ~ condition_recode*choicetype, data=long_df)
summary(twobytwo)

#logistic regression of condition predicting the type of choice made

condition_choicetype <- glm(formula = socialchoice ~ condition_recode, family=binomial,data=wtp_rej_longdata)
summary(condition_choicetype)

#Logit regression: trial by trial (mixed effects models) Social_choice ~ condition_recode * decision_price
wtp_rej_longdata$decision_price_z <- scale(wtp_rej_longdata$decision_price)
decisionprice_condition_onchoice1 <- lmer(socialchoice ~  decision_price_z * condition_recode + (1 | participant), data = wtp_rej_longdata)
summary(decisionprice_condition_onchoice1)
#plot_model(decisionprice_condition_onchoice1, type='int')


# Generate predicted probabilities across values of decision_price_z
preds <- ggpredict(decisionprice_condition_onchoice1, terms = c("decision_price_z", "condition_recode"))

# View structure
head(preds)


linearmixedeffects <- ggplot(preds, aes(x = x, y = predicted, color = group, fill = group)) +
  geom_line(size = 1.5) +
  geom_ribbon(aes(ymin = conf.low, ymax = conf.high), alpha = 0.2, color = NA) +
  scale_color_manual(
    name = "Condition",
    values = c("-1" = "#88CCEE", "1" = "#FF6F61"),
    labels = c("-1" = "Acceptance", "1" = "Rejection")
  ) +
  scale_fill_manual(
    name = "Condition",
    values = c("-1" = "#88CCEE", "1" = "#FF6F61"),
    labels = c("-1" = "Acceptance", "1" = "Rejection")
  ) +
  labs(
    x = "Decision Price (z)",
    y = "Pred Probability of Choosing Social"
  ) +
  theme_minimal() +
  theme(
    panel.grid = element_blank(),
    axis.title.x = element_text(size = 26, face = "bold", margin = margin(t = 25)),
    axis.title.y = element_text(size = 26, face = "bold", margin = margin(r = 25)),
    axis.text.x = element_text(size = 24, face = "bold"),
    axis.text.y = element_text(size = 24, face = "bold"),
    legend.title = element_text(size = 24, face = "bold"),
    legend.text = element_text(size = 22, face = "bold"),
    plot.margin = margin(t = 20, r = 20, b = 20, l = 30)
  )

# Save the plot

ggsave("linearmixedeffects.png", plot = linearmixedeffects, width = 10, height = 8, dpi = 300)

stress <- lm( stress_mean ~ condition_recode, data=wtp_rej_shortdata)
summary(stress)

likelihoodtoshare <- lm(salience_mean ~ condition_recode + PC1 + PC2, data=merged_data)
summary(likelihoodtoshare)

#principal components analysis
pca_simple <- lmer(socialchoice ~ PC1 + PC2 + salience_mean+ (1 | participant), data = merged_data)
summary(pca_simple)

pca_complex <-lmer(socialchoice ~ PC1 * condition_recode + value_diff * PC1 + PC2 + salience_mean * PC1 + (1 | participant), data = merged_data)
summary(pca_complex)

valdiff_qs <- quantile(merged_data$value_diff, probs = c(0.1, 0.5, 0.9), na.rm = TRUE)

preds <- ggpredict(pca_complex, terms = c(
  paste0("PC1 [", round(min(merged_data$PC1),2), ":", round(max(merged_data$PC1),2), " by=0.1]"),
  paste0("value_diff [", paste(round(valdiff_qs,2), collapse = ","), "]")
))

pcmixedeffects <- ggplot(preds, aes(x = x, y = predicted, color = group, fill = group)) +
  geom_line(size = 1.5) +
  geom_ribbon(aes(ymin = conf.low, ymax = conf.high), alpha = 0.2, color = NA) +
  scale_color_manual(
    values = c("#E2B007", "#007C91", "#5B3A70"),
    name = "Value Diff",
    labels = c("Nonsoc > Soc", "Equal", "Soc > Nonsoc")
  ) +
  scale_fill_manual(
    values = c("#E2B007", "#007C91", "#5B3A70"),
    name = "Value Diff",
    labels = c("Nonsoc > Soc", "Equal", "Soc > Nonsoc")
  ) +
  labs(
    x = "PC1",
    y = "Pred Probability of Choosing Social",
    title = ""
  ) +
  theme_minimal() +
  theme(
    panel.grid = element_blank(),
    axis.title = element_text(size = 24, face = "bold"),
    axis.text = element_text(size = 20),
    legend.title = element_text(size = 20, face = "bold"),
    legend.text = element_text(size = 18),
    plot.title = element_text(size = 22, face = "bold", hjust = 0.5)
  )
ggsave("pcmixedeffects.png", plot = pcmixedeffects, width = 10, height = 8, dpi = 300)

#comparing models
anova(pca_simple, pca_complex)
