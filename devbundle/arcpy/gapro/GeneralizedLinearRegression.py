# Generated documentation for module arcpy.gapro


class GeneralizedLinearRegression(object):
    """
    Performs generalized linear regression (GLR) to generate predictions or to model a dependent variable in terms of its relationship to a set of explanatory variables. This tool can be used to fit continuous (OLS), binary (logistic), and count (Poisson) models.
    """

    @property
    def description(self) -> str:
        return """

        GeneralizedLinearRegression_gapro(input_features, dependent_variable, model_type, explanatory_variables;explanatory_variables..., output_features, {input_features_to_predict}, {explanatory_variables_to_match;explanatory_variables_to_match...}, {dependent_variable_mapping;dependent_variable_mapping...}, {output_predicted_features}, {coefficient_table})

        Performs generalized linear regression (GLR) to generate predictions
        or to model a dependent variable in terms of its relationship to a set
        of explanatory variables. This tool can be used to fit continuous
        (OLS), binary (logistic), and count (Poisson) models.

     INPUTS:
      input_features (Table View):
          The layer containing the dependent and independent variables.
      dependent_variable (Field):
          The numeric field containing the observed values to be modeled.
      model_type (String):
          Specifies the type of data that will be modeled.CONTINUOUS-The
          dependent_variable value is continuous. The Gaussian
          model will be used, and the tool will perform ordinary least squares
          regression. This is the default. BINARY-The
          dependent_variable value represents presence or
          absence. This can be either conventional ones and zeroes, or string
          values mapped to zero or ones in theparameter. The Logistic regression
          model will be used. Match Explanatory VariablesCOUNT-The
          dependent_variable value is discrete and represents events,
          for example, crime counts, disease incidents, or traffic accidents.
          The Poisson regression model will be used.
      explanatory_variables (Field):
          A list of fields representing independent explanatory variables in the
          regression model.
      input_features_to_predict {Table View}:
          A layer containing features representing locations where estimates
          will be computed. Each feature in this dataset should contain values
          for all the explanatory variables specified. The dependent variable
          for these features will be estimated using the model calibrated for
          the input layer data.
      explanatory_variables_to_match {Value Table}:
          Matches the explanatory variables in the input_features_to_predict
          parameter to corresponding explanatory variables from the
          input_features parameter-for example, [["LandCover2000",
          "LandCover2010"], ["Income", "PerCapitaIncome"]].
      dependent_variable_mapping {Value Table}:
          Two strings representing the values used to map to 0 (absence)
          and 1 (presence) for binary regression. By default, 0 and 1 will be
          used. For example, to predict an arrest with field values of Arrest
          and No Arrest, enter No Arrest forand Arrest for. False Value
          (0)True Value (1)

     OUTPUTS:
      output_features (Table / Feature Class):
          The name of the feature class that will be created containing the
          dependent variable estimates and residuals.
      output_predicted_features {Table / Feature Class}:
          The output feature class with the dependent variable estimates for
          each input_features_to_predict value. The output feature class
          with the dependent variable estimates
          for eachvalue. Input Prediction Features
      coefficient_table {Table}:
          An output table containing the coefficients from the model fit.

        """