# Generated documentation for module arcpy.geoai


class PredictUsingAutoML(object):
    """
    Predicts continuous variables (regression) or categorical variables (classification) on unseen compatible datasets using a trained .dlpk model produced by the Train Using AutoML tool.
    """

    @property
    def description(self) -> str:
        return """

        PredictUsingAutoML_geoai(in_model_definition, prediction_type, in_features, {explanatory_rasters;explanatory_rasters...}, {distance_features;distance_features...}, {out_prediction_features}, {out_prediction_surface}, {match_explanatory_variables;match_explanatory_variables...}, {match_distance_variables;match_distance_variables...}, {match_explanatory_rasters;match_explanatory_rasters...}, {get_prediction_explanations})

        Predicts continuous variables (regression) or categorical variables
        (classification) on unseen compatible datasets using a trained .dlpk
        model produced by the Train Using AutoML tool.

     INPUTS:
      in_model_definition (File):
          The .dlpk file or the .emd file.
      prediction_type (String):
          Specifies the output file type that will be created.
          PREDICT_FEATURE-A feature layer containing the prediction
          values will be created. Thevalue is required for this option.
          Output Prediction Features         PREDICT_RASTER-A raster layer
          containing the prediction
          values will be created. Thevalue is required for this option.
          Output Prediction Surface
      in_features (Feature Layer / Table View / Feature Class):
          The features for which the prediction will be obtained. The input
          should include some or all the fields necessary to determine the
          dependent variable value. This parameter is required if the
          prediction_type parameter is set to PREDICT_FEATURE.
      explanatory_rasters {Raster Layer}:
          A list of rasters that contain the explanatory rasters necessary to
          determine the dependent variable value. This parameter is required if
          the prediction_type parameter is set to PREDICT_RASTER.
      distance_features {Feature Layer}:
          The point or polygon features whose distances from the input training
          features will be estimated automatically and added as explanatory
          variables. Distances will be calculated from each of the input
          explanatory training distance features to the nearest input training
          features. If the input explanatory training distance features are
          polygons, the distance attributes will be calculated as the distance
          between the closest segments of the pair of features.
      match_explanatory_variables {Value Table}:
          The mapping of field names from the prediction set to the training
          set. Use this parameter if the field names of the training and
          prediction sets are different. The values are the field names in the
          prediction dataset that match the field names in the input feature
          class.
      match_distance_variables {Value Table}:
          The mapping of distance feature names from the prediction set to the
          training set. Use this parameter if the distance feature names used in
          the training and prediction sets are different. The string values are
          the feature names that were used for prediction that match the
          distance features names used for training.
      match_explanatory_rasters {Value Table}:
          The mapping of names from the prediction rasters to the training
          rasters. Use this parameter if the names of the explanatory rasters
          used for prediction and the names of the corresponding rasters used
          during training are different. The string values are the explanatory
          raster names that were used for prediction that match the explanatory
          raster names used for training.
      get_prediction_explanations {Boolean}:
          Specifies whether fields representing feature importance will be
          added.TRUE-Fields representing feature importance will be added.
          Fields will
          be generated for every predicted sample along with the prediction
          values.FALSE-Fields representing feature importance will not be
          generated.
          This is the default.

     OUTPUTS:
      out_prediction_features {Feature Class / Table}:
          The output table or feature class.
      out_prediction_surface {Folder}:
          The path to where the output prediction raster will be saved.

        """