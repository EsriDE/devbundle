# Generated documentation for module arcpy.stats


class GeneralizedLinearRegression(object):
    """
    Performs generalized linear regression (GLR) to generate predictions or to model a dependent variable in terms of its relationship to a set of explanatory variables. This tool can be used to fit continuous (OLS), binary (logistic), and count (Poisson) models.
    """

    @property
    def description(self) -> str:
        return """

        GeneralizedLinearRegression_stats(in_features, dependent_variable, model_type, output_features, {explanatory_variables;explanatory_variables...}, {distance_features;distance_features...}, {prediction_locations}, {explanatory_variables_to_match;explanatory_variables_to_match...}, {explanatory_distance_matching;explanatory_distance_matching...}, {output_predicted_features}, {output_trained_model})

        Performs generalized linear regression (GLR) to generate predictions
        or to model a dependent variable in terms of its relationship to a set
        of explanatory variables. This tool can be used to fit continuous
        (OLS), binary (logistic), and count (Poisson) models.

     INPUTS:
      in_features (Feature Layer):
          The feature class containing the dependent and independent variables.
      dependent_variable (Field):
          The numeric field containing the observed values to be modeled.
      model_type (String):
          Specifies the type of data that will be modeled.CONTINUOUS-The
          dependent_variable value is continuous. The model used
          is Gaussian, and the tool performs ordinary least squares
          regression.BINARY-The dependent_variable value represents presence or
          absence.
          This can be either conventional 1s and 0s, or continuous data that has
          been recoded based on a threshold value. The model used is Logistic
          Regression.COUNT-The dependent_variable value is discrete and
          represents
          events-for example, crime counts, disease incidents, or traffic
          accidents. The model used is Poisson regression.
      explanatory_variables {Field}:
          A list of fields representing independent explanatory variables in the
          regression model.
      distance_features {Feature Layer}:
          Automatically creates explanatory variables by calculating a distance
          from the provided features to the in_features values. Distances will
          be calculated from each of the input distance_features values to the
          nearest in_features value. If the input distance_features values are
          polygons or lines, the distance attributes will be calculated as the
          distance between the closest segments of the pair of features.
      prediction_locations {Feature Layer}:
          A feature class containing features representing locations where
          estimates will be computed. Each feature in this dataset should
          contain values for all the explanatory variables specified. The
          dependent variable for these features will be estimated using the
          model calibrated for the input feature class data.
      explanatory_variables_to_match {Value Table}:
          Matches the explanatory variables in the prediction_locations
          parameter to corresponding explanatory variables from the in_features
          parameter.
      explanatory_distance_matching {Value Table}:
          Matches the distance features specified for the features_to_predict
          parameter on the left to the corresponding distance features for the
          in_features parameter on the right.

     OUTPUTS:
      output_features (Feature Class):
          The new feature class that will contain the dependent variable
          estimates and residuals.
      output_predicted_features {Feature Class}:
          The output feature class that will receive dependent variable
          estimates for each prediction_location value. The output
          feature class that will receive dependent variable
          estimates for eachvalue. Prediction Location
      output_trained_model {File}:
          An output model file that will save the trained model, which can be
          used later for prediction.

        """