# Generated documentation for module arcpy.stats


class ExploratoryRegression(object):
    """
    Evaluates all possible combinations of the input candidate explanatory variables, looking for OLS models that best explain the dependent variable within the context of user-specified criteria.
    """

    @property
    def description(self) -> str:
        return """

        ExploratoryRegression_stats(Input_Features, Dependent_Variable, Candidate_Explanatory_Variables;Candidate_Explanatory_Variables..., {Weights_Matrix_File}, {Output_Report_File}, {Output_Results_Table}, {Maximum_Number_of_Explanatory_Variables}, {Minimum_Number_of_Explanatory_Variables}, {Minimum_Acceptable_Adj_R_Squared}, {Maximum_Coefficient_p_value_Cutoff}, {Maximum_VIF_Value_Cutoff}, {Minimum_Acceptable_Jarque_Bera_p_value}, {Minimum_Acceptable_Spatial_Autocorrelation_p_value})

        Evaluates all possible combinations of the input candidate explanatory
        variables, looking for OLS models that best explain the dependent
        variable within the context of user-specified criteria.

     INPUTS:
      Input_Features (Feature Layer):
          The feature class or feature layer containing the dependent and
          candidate explanatory variables to analyze.
      Dependent_Variable (Field):
          The numeric field containing the observed values you want to model
          using OLS.
      Candidate_Explanatory_Variables (Field):
          A list of fields to try as OLS model explanatory variables.
      Weights_Matrix_File {File}:
          A file containing spatial weights that define the spatial
          relationships among your input features. This file is used to assess
          spatial autocorrelation among regression residuals. You can use the
          Generate Spatial Weights Matrix File tool to create this. When you do
          not provide a spatial weights matrix file, residuals are assessed for
          spatial autocorrelation based on each feature's 8 nearest
          neighbors.Note: The spatial weights matrix file is only used to
          analyze spatial
          structure in model residuals; it is not used to build or to calibrate
          any of the OLS models.
      Maximum_Number_of_Explanatory_Variables {Long}:
          All models with explanatory variables up to the value entered here
          will be assessed. If, for example, the
          Minimum_Number_of_Explanatory_Variables is 2 and the
          Maximum_Number_of_Explanatory_Variables is 3, the Exploratory
          Regression tool will try all models with every combination of two
          explanatory variables, and all models with every combination of three
          explanatory variables.
      Minimum_Number_of_Explanatory_Variables {Long}:
          This value represents the minimum number of explanatory variables for
          models evaluated. If, for example, the
          Minimum_Number_of_Explanatory_Variables is 2 and the
          Maximum_Number_of_Explanatory_Variables is 3, the Exploratory
          Regression tool will try all models with every combination of two
          explanatory variables, and all models with every combination of three
          explanatory variables.
      Minimum_Acceptable_Adj_R_Squared {Double}:
          This is the lowest Adjusted R-Squared value you consider a passing
          model. If a model passes all of your other search criteria, but has an
          Adjusted R-Squared value smaller than the value entered here, it will
          not show up as a Passing Model in the Output_Report_File. Valid values
          for this parameter range from 0.0 to 1.0. The default value is 0.5,
          indicating that passing models will explain at least fifty percent of
          the variation in the dependent variable.
      Maximum_Coefficient_p_value_Cutoff {Double}:
          For each model evaluated, OLS computes explanatory variable
          coefficient p-values. The cutoff p-value you enter here represents the
          confidence level you require for all coefficients in the model in
          order to consider the model passing. Small p-values reflect a stronger
          confidence level. Valid values for this parameter range from 1.0 down
          to 0.0, but will most likely be 0.1, 0.05, 0.01, 0.001, and so on. The
          default value is 0.05, indicating passing models will only contain
          explanatory variables whose coefficients are statistically at the 95
          percent confidence level (p-values smaller than 0.05). To relax this
          default you would enter a larger p-value cutoff, such as 0.1. If you
          are getting lots of passing models, you will likely want to make this
          search criteria more stringent by decreasing the default p-value
          cutoff from 0.05 to 0.01 or smaller.
      Maximum_VIF_Value_Cutoff {Double}:
          This value reflects how much redundancy (multicollinearity) among
          model explanatory variables you will tolerate. When the VIF (Variance
          Inflation Factor) value is higher than about 7.5, multicollinearity
          can make a model unstable; consequently, 7.5 is the default value
          here. If you want your passing models to have less redundancy, you
          would enter a smaller value, such as 5.0, for this parameter.
      Minimum_Acceptable_Jarque_Bera_p_value {Double}:
          The p-value returned by the Jarque-Bera diagnostic test indicates
          whether the model residuals are normally distributed. If the p-value
          is statistically significant (small), the model residuals are not
          normal and the model is biased. Passing models should have large
          Jarque-Bera p-values. The default minimum acceptable p-value is 0.1.
          Only models returning p-values larger than this minimum will be
          considered passing. If you are having trouble finding unbiased passing
          models, and decide to relax this criterion, you might enter a smaller
          minimum p-value such as 0.05.
      Minimum_Acceptable_Spatial_Autocorrelation_p_value {Double}:
          For models that pass all of the other search criteria, the Exploratory
          Regression tool will check model residuals for spatial clustering
          using Global Moran's I. When the p-value for this diagnostic test is
          statistically significant (small), it indicates the model is very
          likely missing key explanatory variables (it isn't telling the whole
          story). Unfortunately, if you have spatial autocorrelation in your
          regression residuals, your model is misspecified, so you cannot trust
          your results. Passing models should have large p-values for this
          diagnostic test. The default minimum p-value is 0.1. Only models
          returning p-values larger than this minimum will be considered
          passing. If you are having trouble finding properly specified models
          because of this diagnostic test, and decide to relax this search
          criteria, you might enter a smaller minimum such as 0.05.

     OUTPUTS:
      Output_Report_File {File}:
          The report file contains tool results, including details about any
          models found that passed all the search criteria you entered. This
          output file also contains diagnostics to help you fix common
          regression problems in the case that you don't find any passing
          models.
      Output_Results_Table {Table}:
          The optional output table created containing the explanatory variables
          and diagnostics for all of the models within the Coefficient p-value
          and VIF value cutoffs.

        """