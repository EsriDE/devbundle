# Generated documentation for module arcpy.stats


class PredictUsingSSMFile(object):
    """
    Predicts continuous or categorical values using a trained spatial statistics model (.ssm file).
    """

    @property
    def description(self) -> str:
        return """

        PredictUsingSSMFile_stats(input_model, prediction_type, {features_to_predict}, {output_features}, {output_raster}, {explanatory_variable_matching;explanatory_variable_matching...}, {explanatory_distance_matching;explanatory_distance_matching...}, {explanatory_rasters_matching;explanatory_rasters_matching...})

        Predicts continuous or categorical values using a trained spatial
        statistics model (.ssm file).

     INPUTS:
      input_model (File):
          The spatial statistics model file that will be used to make new
          predictions.
      prediction_type (String):
          Specifies the operation mode that will be used. The tool can predict
          new features or create a prediction raster
          surface.PREDICT_FEATURES-Predictions or classifications will be
          generated for
          features. Explanatory variables must be provided to match variables
          used to train the input model file. The output of this option will be
          a feature class and model diagnostics in the messages
          window.PREDICT_RASTER-A prediction raster will be generated for the
          area
          where the explanatory rasters intersect. Explanatory rasters must be
          provided to match the rasters used to train the input model file. The
          output of this option will be a prediction surface and model
          diagnostics in the messages window
      features_to_predict {Feature Layer}:
          The feature class representing locations where predictions will be
          made. This feature class must also contain any explanatory variables
          provided as fields that correspond to those used to train the input
          model.
      explanatory_variable_matching {Value Table}:
          A list of the explanatory variables of the input model and
          corresponding fields of the input prediction features. For each
          explanatory variable in thecolumn, provide the corresponding
          prediction field in thecolumn. Thecolumn specifies whether the
          variable is categorical or continuous.
          TrainingPredictionCategorical
      explanatory_distance_matching {Value Table}:
          A list of the explanatory distance features of the input model
          and corresponding prediction distance features. For each explanatory
          distance feature in thecolumn, provide the corresponding prediction
          distance feature in thecolumn. TrainingPrediction
      explanatory_rasters_matching {Value Table}:
          A list of the explanatory rasters of the input model and
          corresponding prediction rasters. For each explanatory raster in
          thecolumn, provide the corresponding prediction raster in thecolumn.
          Thecolumn specifies whether the raster is categorical or continuous.
          TrainingPredictionCategorical

     OUTPUTS:
      output_features {Feature Class}:
          The output feature class containing the prediction results.
      output_raster {Raster Dataset}:
          The output raster containing the prediction results. The default cell
          size will be the maximum cell size of the input rasters.

        """