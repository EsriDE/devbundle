# Generated documentation for module arcpy.stats


class CausalInferenceAnalysis(object):
    """
    Estimates the causal effect of a continuous exposure variable on a continuous outcome variable by approximating a randomized experiment and controlling for confounding variables.
    """

    @property
    def description(self) -> str:
        return """

        CausalInferenceAnalysis_stats(in_features, outcome_field, exposure_field, confounding_variables;confounding_variables..., out_features, {ps_method}, {balancing_method}, {enable_erf_popups}, {out_erf_table}, {target_outcomes;target_outcomes...}, {target_exposures;target_exposures...}, {lower_exp_trim}, {upper_exp_trim}, {lower_ps_trim}, {upper_ps_trim}, {num_bins}, {scale}, {balance_type}, {balance_threshold}, {bw_method}, {bandwidth}, {create_bootstrap_ci})

        Estimates the causal effect of a continuous exposure variable on a
        continuous outcome variable by approximating a randomized experiment
        and controlling for confounding variables.

     INPUTS:
      in_features (Table View):
          The input features or table containing fields of the exposure,
          outcome, and confounding variables.
      outcome_field (Field):
          The numeric field of the outcome variable. This is the variable that
          responds to changes in the exposure variable. The outcome variable
          must be continuous or binary (not categorical).
      exposure_field (Field):
          The numeric field of the exposure variable (sometimes called the
          treatment variable). This is the variable that causes changes in the
          outcome variable. The exposure variable must be continuous (not binary
          or categorical).
      confounding_variables (Value Table):
          The fields of the confounding variables. These are the variables that
          are related to both the exposure and outcome variables, and they must
          be balanced in order to estimate the causal effect between the
          exposure and outcome variables. The confounding variables can be
          continuous, categorical, or binary. Text fields must be categorical,
          integer fields can be either categorical or continuous, and other
          numeric fields must be continuous.For the exposure-response function
          to be unbiased, all variables that
          are related to the exposure and outcome variables must be included as
          confounding variables.
      ps_method {String}:
          Specifies the method that will be used for calculating the propensity
          scores of each observation.The propensity score of an observation is
          the likelihood (or
          probability) of receiving the observed exposure value, given the
          values of the confounding variables. Large propensity scores mean that
          the exposure is common for individuals with the associated confounding
          variables, and low propensity scores mean that the exposure value is
          uncommon for individuals with the confounding variables. For example,
          if an individual has high blood pressure (exposure) but has no risk
          factors for high blood pressure (confounders), this individual would
          have a low propensity score because it is uncommon to have high blood
          pressure without any risk factors. Conversely, high blood pressure for
          an individual with many risk factors would have a larger propensity
          score because it is more common.Propensity scores are estimated by a
          statistical model that predicts
          the exposure variable using the confounding variables as explanatory
          variables. You can use an OLS regression model or a machine learning
          model that uses gradient boosted regression trees. It is recommended
          that you first use regression and only use gradient boosting if
          regression fails to balance the confounding variables.REGRESSION-OLS
          regression will be used to estimate the propensity
          scores. This is the default.GRADIENT_BOOSTING-Gradient boosted
          regression trees will be used to
          estimate the propensity scores.
      balancing_method {String}:
          Specifies the method that will be used for balancing the confounding
          variables.Each method estimates a set of balancing weights that
          removes the
          correlation between the confounding variables and the exposure
          variable. It is recommended that you first use matching and only use
          inverse propensity score weighting if matching fails to balance the
          confounding variables. Inverse propensity score weighting will
          calculate faster than propensity score matching, so it also
          recommended when the calculation time of matching is not feasible for
          the data.MATCHING-Propensity score matching will be used to balance
          the
          confounding variables. This is the default.WEIGHTING-Inverse
          propensity score weighting will be used to balance
          the confounding variables.
      enable_erf_popups {Boolean}:
          Specifies whether pop-up charts that display the local ERF for the
          observation will be created for each observation.CREATE_POPUP-Local
          ERF pop-up charts will be created on the output
          features or table.NO_POPUP-Local ERF pop-up charts will not be created
          on the output
          features or table. This is the default.
      target_outcomes {Double}:
          A list of target outcome values from which required changes in
          exposure to achieve the outcomes will be calculated for each
          observation. For example, if the exposure variable is an air quality
          index and the outcome variable is the annual asthma hospitalization
          rate of counties, you can determine how much the air quality index
          needs to decrease to achieve asthma hospitalization rates below 0.01,
          0.005, and 0.001. For each provided target outcome value, two new
          fields will be created on the output. The first field contains the
          exposure value that would result in the target outcome, and the second
          field contains the required change in the exposure variable to produce
          the target outcome (positive values indicate that the exposure needs
          to increase, and negative values indicate that the exposure needs to
          decrease). In some cases, there will be no solution for some
          observations, so you should only provide target outcomes that are
          feasible to achieve by changing the exposure variable. For example,
          there is no PM2.5 level that can result in an asthma hospitalization
          rate of zero, so using a target outcome equal to zero will result in
          no solutions. If there are multiple exposure values that would result
          in the target outcome, the one that requires the smallest change in
          exposure will be used.If an output exposure-response function table is
          created, it will
          include any target outcome values and the associated exposure values
          appended to the end of the table. If there are multiple solutions,
          multiple records will be appended to the table with repeated outcome
          values.If local ERF pop-up charts are created, the target outcomes and
          associated exposure values will be shown in the pop-ups of each
          observation.
      target_exposures {Double}:
          A list of target exposure values that will be used to calculate new
          outcomes for each observation. For each target exposure value, the
          tool estimates the new outcome value that the observation would
          receive if its exposure variable was changed to the target exposure.
          For example, if the exposure variable is an air quality index and the
          outcome variable is the annual asthma hospitalization rate of
          counties, you can estimate how the hospitalization rate for each
          observation would change for different levels of air quality. For each
          provided target exposure value, two new fields will be created on the
          output. The first field contains the estimated outcome value if the
          observation received the target exposure, and the second field
          contains the estimated change in the outcome variable (positive values
          indicate that the outcome variable will increase, and negative values
          indicate that the outcome variable will decrease). The target
          exposures must be within the range of the exposure variable after
          trimming.If an output exposure-response function table is created, it
          will
          include any target exposure values and the associated response values
          appended to the end of the table.If local ERF pop-up charts are
          created, the target exposure values and
          associated outcomes will be shown in the pop-ups of each feature.
      lower_exp_trim {Double}:
          The lower quantile that will be used to trim the exposure variable.
          Any observations with exposure values below this quantile will be
          excluded from the analysis before estimating propensity scores. The
          value must be between 0 and 1. The default is 0.01, meaning that the
          bottom 1 percent of exposure values will be trimmed. It is recommended
          that you trim some of the lowest exposure values to improve the
          estimation of propensity scores.
      upper_exp_trim {Double}:
          The upper quantile that will be used to trim the exposure variable.
          Any observations with exposure values above this quantile will be
          excluded from the analysis before estimating propensity scores. The
          value must be between 0 and 1. The default is 0.99, meaning that the
          top 1 percent of exposure values will be trimmed. It is recommended
          that you trim some of the highest exposure values to improve the
          estimation of propensity scores.
      lower_ps_trim {Double}:
          The lower quantile that will be used to trim the propensity scores.
          Any observations with propensity scores below this quantile will be
          excluded from the analysis before performing propensity score matching
          or inverse propensity score weighting. The value must be between 0 and
          1. The default is 0, meaning that no trimming will be performed.Lower
          propensity score trimming is often needed when using inverse
          propensity score weighting. Propensity scores near zero can produce
          large and unstable balancing weights.
      upper_ps_trim {Double}:
          The upper quantile that will be used to trim the propensity scores.
          Any observations with propensity scores above this quantile will be
          excluded from the analysis before performing propensity score matching
          or inverse propensity score weighting. The value must be between 0 and
          1. The default is 1, meaning that no trimming will be performed.
      num_bins {Long}:
          The number of exposure bins that will be used for propensity score
          matching. In matching, the exposure variable is divided into evenly
          spaced bins (equal intervals), and matching is performed within each
          bin. At least two exposure bins are required, and it is recommended
          that at least five exposure values be included within each bin. If no
          value is provided, the value will be estimated while the tool runs and
          displayed in the messages.
      scale {Double}:
          The relative weight (sometimes called the scale) of the propensity
          score to the exposure variable that will be used when performing
          propensity score matching. Within each exposure bin, matches are
          determined using the differences in the propensity scores and in the
          values of the exposure variable. This parameter specifies how to
          prioritize each criteria. For example, a value equal to 0.5 means that
          the propensity score and exposure variables are given equal weight
          when finding matching observations.If no value is provided, the value
          will be estimated while the tool
          runs and displayed in the messages. The value that will provide the
          best balance is difficult to predict, so it is recommended that you
          allow the tool to estimate the value. Providing a manual value can be
          used to reduce the calculation time or to reproduce prior results. If
          the resulting exposure-response function shows vertical bands of
          observations with large weights, increasing the relative weight may
          provide a more realistic and accurate exposure-response function.
      balance_type {String}:
          Specifies the method that will be used to determine whether the
          confounding variables are balanced. After estimating weights with
          propensity score matching or inverse propensity score weighting,
          weighted correlations are calculated for each confounding variable. If
          the mean, median, or maximum absolute correlation is less than the
          balance threshold, the confounding variables are considered balanced,
          meaning they are sufficiently uncorrelated with the exposure
          variable.MEAN-Confounding variables will be considered balanced if the
          mean
          absolute correlation is less than the balance threshold. This is the
          default.MEDIAN-Confounding variables will be considered balanced if
          the median
          absolute correlation is less than the balance
          threshold.MAXIMUM-Confounding variables will be considered balanced if
          the
          maximum absolute correlation is less than the balance threshold.
      balance_threshold {Double}:
          The threshold value that will be compared to the weighted correlations
          of the confounding variables to determine if they are balanced. The
          value must be between 0 and 1. A larger balance threshold indicates a
          larger tolerance for imbalance in the confounding variables and bias
          in the exposure-response function. The default is 0.1.
      bw_method {String}:
          Specifies the method that will be used to estimate the bandwidth of
          the exposure-response function.PLUG_IN-A plug-in method will be used
          to estimate the bandwidth. This
          is the default.CV-The bandwidth that minimizes the mean square cross
          validation error
          will be used.MANUAL-A custom bandwidth will be used.
      bandwidth {Double}:
          The bandwidth value of the exposure-response function when using a
          manual bandwidth.
      create_bootstrap_ci {Boolean}:
          Specifies whether 95 percent confidence intervals for the exposure-
          response function will be created using M-out-of-N
          bootstrapping.CREATE_CI-Confidence intervals for the exposure-response
          function will
          be created.NO_CI-Confidence intervals for the exposure-response
          function will not
          be created. This is the default.

     OUTPUTS:
      out_features (Feature Class / Table):
          The output features or table containing the propensity scores,
          balancing weights, and a field indicating whether the feature was
          trimmed (excluded from the analysis). The exposure, outcome, and
          confounding variables are also included.
      out_erf_table {Table}:
          A table containing values of the exposure-response function. The table
          will contain 200 evenly spaced exposure values between the minimum and
          maximum exposure (after trimming) along with the estimated response
          from the exposure-response function. The response field represents the
          average value of the outcome variable if all members of the population
          received the associated exposure value. If bootstrapped confidence
          intervals are created, additional fields will be created containing
          the upper and lower bounds of the confidence interval for the exposure
          value, as well as the standard deviation and number of samples used to
          construct the confidence interval. If any target outcome or exposure
          values are provided, they will be appended to the end of the table.

        """