# Generated documentation for module arcpy.geoai


class TrainTimeSeriesForecastingModel(object):
    """
    Trains a deep learning-based time series forecasting model using time series data from a space-time cube. The trained model can be used for forecasting the values of each location of a space-time cube using the Forecast Using Time Series Model tool.
    """

    @property
    def description(self) -> str:
        return """

        TrainTimeSeriesForecastingModel_geoai(in_cube, out_model, analysis_variable, sequence_length, {explanatory_variables;explanatory_variables...}, {max_epochs}, {validation_timesteps}, {model_type}, {batch_size}, {arguments;arguments...}, {early_stopping}, {out_features}, {out_cube}, {multistep})

        Trains a deep learning-based time series forecasting model using time
        series data from a space-time cube. The trained model can be used for
        forecasting the values of each location of a space-time cube using the
        Forecast Using Time Series Model tool.

     INPUTS:
      in_cube (File):
          The netCDF cube containing the variable that will be used to forecast
          to future time steps. This file must have an .nc file extension and
          must have been created using the Create Space Time Cube By Aggregating
          Points, Create Space Time Cube From Defined Locations, or Create Space
          Time Cube From Multidimensional Raster Layer tool.
      analysis_variable (String):
          The numeric variable in the dataset that will be forecasted to future
          time steps.
      sequence_length (Long):
          The number of previous time steps that will be used when
          training the model. If the data contains seasonality (repeating
          cycles), provide the length corresponding to one season. If the
          multistep parameter value is False, the value of this parameter
          should be less than or equal to the total number of input time steps
          remaining after excluding the validation_timesteps parameter value.If
          the multistep parameter value is True, 1.5 times the value of
          sequence_length should be less than or equal to the total number of
          time steps after excluding the validation_timesteps parameter value.
      explanatory_variables {Value Table}:
          Independent variables from the data that will be used to train the
          model. Use a True value after any variables that represent classes or
          categories.
      max_epochs {Long}:
          The maximum number of epochs for which the model will be trained. The
          default is 20.
      validation_timesteps {Long}:
          The number of time steps that will be excluded for validation. For
          example, if a value of 14 is specified, the last 14 rows in the data
          frame will be used as validation data. The default is 10 percent of
          total timesteps. Ideally it should not be less than 5 percent of the
          total time steps in the input time cube.If the multistep parameter
          value is False, this parameter value should
          be less than 25 percent of the total number of records in the input
          space-time cube.If the multistep parameter value is True, this
          parameter value should
          be less than or equal to half of the sequence_length parameter value.
      model_type {String}:
          Specifies the model architecture that will be used for training the
          model.InceptionTime-The InceptionTime architecture that will be used
          for
          training the model. This is the default.ResNet-The ResNet architecture
          that will be used for training the
          model.ResCNN-The ResCNN architecture that will be used for training
          the
          model.FCN-The FCN architecture that will be used for training the
          model.LSTM-The LSTM architecture that will be used for training the
          model.TimeSeriesTransformer-The TimeSeriesTransformer architecture
          that will
          be used for training the model.
      batch_size {Long}:
          The number of samples that will be processed at one time. The default
          is 64.Depending on the computer's GPU, this number can be changed to
          8, 16,
          32, 64, and so on.
      arguments {Value Table}:
          Additional model arguments that will be used specific to each model.
          These arguments can be used to adjust the model complexity and size.
          See How Time Series forecasting models work to understand the model
          architecture, the supported model arguments, and their default values.
      early_stopping {Boolean}:
          Specifies whether the model training will stop when validation loss
          does not register improvement after five consecutive epochs.TRUE-The
          model training will stop when validation loss does not
          register improvement after five consecutive epochs. This is the
          default.FALSE-The model training will continue until the maximum
          number of
          epochs has been reached.
      multistep {Boolean}:
          Specifies whether a one-step or multistep approach will be used for
          training the multivariate time series forecasting model.TRUE-The model
          training will use a multistep approach.FALSE-The model
          training will use the traditional one-step approach.
          This is the default.

     OUTPUTS:
      out_model (Folder):
          The output folder location that will store the trained model. The
          trained model will be saved as a deep learning package file (.dlpk).
      out_features {Feature Class}:
          The output feature class of all locations in the space-time cube with
          forecasted values stored as fields. The feature class will be created
          using prediction of the trained model on the validation dataset. The
          output displays the forecast for the final time step and contains pop-
          up charts showing the time series forecast on the validation set.
      out_cube {File}:
          An output space-time cube (.nc file) containing the values of the
          input space-time cube with the forecasted values for the corresponding
          validation time steps replaced.

        """