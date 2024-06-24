# Generated documentation for module arcpy.stats


class PresenceOnlyPrediction(object):
    """
    Models the presence of a phenomenon given known presence locations and explanatory variables using a maximum entropy approach (MaxEnt). The tool provides output features and rasters that include the probability of presence and can be applied to problems in which only presence is known and absence is not known.
    """

    @property
    def description(self) -> str:
        return """

        PresenceOnlyPrediction_stats(input_point_features, {contains_background}, {presence_indicator_field}, {explanatory_variables;explanatory_variables...}, {distance_features;distance_features...}, {explanatory_rasters;explanatory_rasters...}, {basis_expansion_functions;basis_expansion_functions...}, {number_knots}, {study_area_type}, {study_area_polygon}, {spatial_thinning}, {thinning_distance_band}, {number_of_iterations}, {relative_weight}, {link_function}, {presence_probability_cutoff}, {output_trained_features}, {output_trained_raster}, {output_response_curve_table}, {output_sensitivity_table}, {features_to_predict}, {output_pred_features}, {output_pred_raster}, {explanatory_variable_matching;explanatory_variable_matching...}, {explanatory_distance_matching;explanatory_distance_matching...}, {explanatory_rasters_matching;explanatory_rasters_matching...}, {allow_predictions_outside_of_data_ranges}, {resampling_scheme}, {number_of_groups}, {output_trained_model})

        Models the presence of a phenomenon given known presence locations and
        explanatory variables using a maximum entropy approach (MaxEnt). The
        tool provides output features and rasters that include the probability
        of presence and can be applied to problems in which only presence is
        known and absence is not known.

     INPUTS:
      input_point_features (Feature Layer):
          The point features representing locations where presence of a
          phenomenon of interest is known to occur.
      contains_background {Boolean}:
          Specifies whether the input point features contain background
          points.If the input points do not contain background points, the tool
          will
          generate background points using cells in the explanatory training
          rasters. The tool uses background points to model the characteristics
          of the landscape in unknown locations and compare them to landscape
          characteristics in known presence locations. Therefore, background
          points can be considered as the study area. Generally, these are
          locations where presence of a phenomenon of interest is unknown.
          However, if any information is known about the background points, the
          relative_weight parameter can be used to indicate
          this.PRESENCE_AND_BACKGROUND_POINTS-The input point features include
          background points.PRESENCE_ONLY_POINTS-The input point features do not
          include
          background points. This is the default.
      presence_indicator_field {Field}:
          The field from the input point features containing binary values that
          indicate each point as presence (1) or background (0). The field must
          be numeric.
      explanatory_variables {Value Table}:
          A list of fields representing the explanatory variables that will help
          predict the probability of presence. You can specify whether each
          variable is categorical or numeric. Specify the CATEGORICAL option for
          each variable that represents a class or category (such as land
          cover).
      distance_features {Feature Layer}:
          A list of feature layers or feature classes that will be used to
          automatically create explanatory variables that represent the distance
          from the input point features to the nearest provided distance
          features. If the input explanatory training distance features are
          polygons or lines, the distance attributes are calculated as the
          distance between the closest segment and the point.
      explanatory_rasters {Value Table}:
          A list of rasters that will be used to automatically create
          explanatory training variables in the model whose values are extracted
          from rasters. For each feature (presence and background points) in the
          input point features, the value of the raster cell will be extracted
          at that exact location.Bilinear raster resampling will be used when
          extracting the raster
          value for continuous rasters. Nearest neighbor assignment will be used
          when extracting a raster value from categorical rasters.You can
          specify whether each raster value is categorical or numeric.
          Specify the CATEGORICAL option for each raster that represents a class
          or category (such as land cover).
      basis_expansion_functions {String}:
          Specifies the basis function that will be used to transform the
          provided explanatory variables for use in the model. If multiple basis
          functions are selected, the tool will produce multiple transformed
          variables and attempt to use them in the model.LINEAR-A linear
          transformation to the input variables will be
          applied. This is the defaultPRODUCT-A pairwise multiplication on
          continuous explanatory variables
          will be used, yielding interaction variables. This option is only
          available when multiple explanatory variables have been
          provided.HINGE-The continuous explanatory variable values will be
          converted
          into two segments, a static segment (composed of zeroes or ones) and a
          linear function segment (increasing or decreasing).THRESHOLD-The
          continuous explanatory variable values will be
          converted into a binary variable composed of zeroes and
          ones.QUADRATIC-The square of each continuous explanatory variable
          value
          will be returned.
      number_knots {Long}:
          The number of knots that will be used by the hinge and threshold
          explanatory variable expansions. The value controls how many
          thresholds are created, which are used to create multiple explanatory
          variable expansions using each threshold. The value must be between 2
          and 50. The default is 10.
      study_area_type {String}:
          Specifies the type of study area that will be used to define where
          presence is possible when the input point features do not contain
          background points.CONVEX_HULL-The smallest convex polygon that
          encloses all the
          presence points in the input point features will be used. This is the
          defaultRASTER_EXTENT-The extent of the intersection of the explanatory
          training rasters will be used.STUDY_POLYGON-A custom study area that
          is defined by a polygon feature
          class will be used.
      study_area_polygon {Feature Layer}:
          A feature class containing the polygons that define a custom study
          area. The input point features must be located within the custom study
          area covered by the polygon features. A study area can be composed of
          multiple polygons.
      spatial_thinning {Boolean}:
          Specifies whether spatial thinning will be applied to presence and
          background points before training the model.Spatial thinning helps to
          reduce sampling bias by removing points and
          ensuring that remaining points have a minimum nearest-neighbor
          distance, set in the thinning_distance_band parameter. Spatial
          thinning is also applied to background points whether they are
          provided in input point features or generated by the
          tool.THINNING-Spatial thinning will be applied.NO_THINNING-Spatial
          thinning
          will not be applied. This is the default.
      thinning_distance_band {Linear Unit}:
          The minimum distance between any two presence points or any two
          background points when spatial thinning is applied.
      number_of_iterations {Long}:
          The number of runs that will be used to find the optimal spatial
          thinning solution, seeking to maintain as many presence and background
          points as possible while ensuring that no two presence or two
          background points are within the specified thinning_distance_band
          parameter value. The minimum possible is 1 iteration and the maximum
          possible is 50 iterations. The default is 10.This parameter is only
          applicable for spatial thinning applied to
          presence and background points in the input point features. Spatial
          thinning that is applied to background points generated from raster
          cells undergo spatial thinning by resampling the raster cells to the
          specified thinning_distance_band parameter value, without needing to
          iterate for an optimal solution.
      relative_weight {Long}:
          A value between 1 and 100 that specifies the relative information
          weight of presence points to background points. The default is 100.A
          higher value indicates that presence points are the primary source
          of information; it is unknown whether background points represent
          presence or absence and background points receive lower weight in the
          model. A lower value indicates that background points also contribute
          valuable information that can be used in conjunction with presence
          points; there is greater confidence that background points represent
          absence and their information can be used in the model as absence
          locations.
      link_function {String}:
          Specifies the function that will convert the unbounded outputs of the
          model to a number between 0 and 1. This value can be interpreted as
          the probability of presence at the location. Each option converts the
          same continuous value to a different probability.CLOGLOG-The C-log-
          log link function will be used to convert the
          predictions to probabilities. This option is recommended when the
          presence and location of a phenomenon is unambiguous, for example,
          when modeling the presence of an immobile plant species. This is the
          default.LOGISTIC-The logistic link function will be used to convert
          predictions to probabilities. This option is recommended when the
          presence and location of a phenomenon is ambiguous, for example, when
          modeling the presence of a migratory animal species.
      presence_probability_cutoff {Double}:
          A cutoff value between 0.01 and 0.99 that establishes which
          probabilities correspond with presence in the resulting
          classification. The cutoff value is used to help evaluate the model's
          performance using training data and known presence points.
          Classification diagnostics are provided in geoprocessing messages and
          in the output trained features.
      features_to_predict {Feature Layer}:
          The feature class representing locations where predictions will be
          made. The feature class must contain any provided explanatory variable
          fields that were used from the input point features.When using spatial
          thinning, you can use the original input point
          features as input prediction features to receive a prediction for the
          entire dataset.
      explanatory_variable_matching {Value Table}:
          The matching explanatory variable fields for the input point features
          and input prediction features.
      explanatory_distance_matching {Value Table}:
          The matching distance features for the training and prediction.
      explanatory_rasters_matching {Value Table}:
          The matching rasters for the training and prediction.
      allow_predictions_outside_of_data_ranges {Boolean}:
          ALLOWED-The prediction will allow extrapolation beyond the range of
          values used in training. This is the default.NOT_ALLOWED-The
          prediction will not allow extrapolation beyond the
          range of values used in training.
      resampling_scheme {String}:
          Specifies the method that will be used to perform cross validation of
          the prediction model. Cross validation excludes a portion of the data
          during training of the model and uses it to test the model's
          performance after it is trained.NONE-Cross validation will not be
          performed. This is the
          defaultRANDOM-The points will be randomly divided into groups, and
          each
          group will be left out once when performing cross validation. The
          number of groups is specified in the number_of_groups parameter.
      number_of_groups {Long}:
          The number of groups that will be used in cross validation for the
          random resampling scheme. A field in the output trained features
          indicates the group that each point was assigned to. The default is 3.
          A minimum of 2 groups and a maximum of 10 groups are allowed.

     OUTPUTS:
      output_trained_features {Feature Class}:
          An output feature class that will contain all features and explanatory
          variables used in the training of the model.
      output_trained_raster {Raster Dataset}:
          The output raster with cell values indicating the probability of
          presence using the selected link function. The default cell size is
          the maximum of the cell sizes of the explanatory training rasters. An
          output trained raster can only be created if the input point features
          do not contain background points.
      output_response_curve_table {Table}:
          The output table that will contain diagnostics from the training model
          that indicate the effect of each explanatory variable on the
          probability of presence after accounting for the average effects of
          all other explanatory variables in the model.The table will have up to
          two derived charts of partial dependence
          plots: one set of line charts for continuous variables and one set of
          bar charts for categorical variables.
      output_sensitivity_table {Table}:
          The output table that will contain diagnostics of training model
          accuracy as the probability presence cutoff changes from 0 to 1.
      output_pred_features {Feature Class}:
          The output feature class that will contain the results of the
          prediction model applied to the input prediction features.
      output_pred_raster {Raster Dataset}:
          The output raster containing the prediction results at each cell of
          the matched explanatory rasters. The default cell size is the maximum
          of the cell sizes of the explanatory training rasters.
      output_trained_model {File}:
          An output model file that will save the trained model, which can be
          used later for prediction.

        """