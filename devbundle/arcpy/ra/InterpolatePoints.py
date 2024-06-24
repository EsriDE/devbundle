# Generated documentation for module arcpy.ra


class InterpolatePoints(object):
    """
    Predicts values at new locations based on measurements from a collection of points. The tool takes point data with values at each point and returns a raster of predicted values.
    """

    @property
    def description(self) -> str:
        return """

        InterpolatePoints_ra(inputPointFeatures, interpolateField, outputName, {optimizeFor}, {transformData}, {sizeOfLocalModels}, {numberOfNeighbors}, {outputCellSize}, {outputPredictionError})

        Predicts values at new locations based on measurements from a
        collection of points. The tool takes point data with values at each
        point and returns a raster of predicted values.

     INPUTS:
      inputPointFeatures (Feature Set):
          The input point features you want to interpolate.
      interpolateField (Field):
          The field containing the data values you want to interpolate. The
          field must be numeric.
      outputName (String):
          The name of the output raster service.The default name is based on the
          tool name and the input layer name.
          If the layer name already exists, you will be prompted to provide
          another name.
      optimizeFor {String}:
          Choose your preference for speed versus accuracy. More accurate
          predictions will take longer to calculate.SPEED-The operation is
          optimized for speed.BALANCE-A balance between
          speed and accuracy. This is the default.ACCURACY-The operation is
          optimized for accuracy.
      transformData {Boolean}:
          Choose whether to transform your data to a normal distribution before
          performing analysis. If your data values do not appear to be normally
          distributed (bell-shaped), it is recommended to perform a
          transformation.NO_TRANSFORM-No transformation is applied. This is the
          default.TRANSFORM-A transformation to the normal distribution is
          applied.
      sizeOfLocalModels {Long}:
          Choose the number of points in each of the local models. A larger
          value will make the interpolation more global and stable, but small-
          scale effects may be missed. Smaller values will make the
          interpolation more local, so small-scale effects are more likely to be
          captured, but the interpolation may be unstable.
      numberOfNeighbors {Long}:
          The number of neighbors to use when calculating the prediction at a
          particular cell.
      outputCellSize {Linear Unit}:
          Set the cell size and units of the output raster. If a prediction
          error raster is created, it will also use this cell size.The unit
          values are Kilometers, Meters, MilesInt, FeetInt, Miles, and
          Feet.The default units are meters.
      outputPredictionError {Boolean}:
          Choose whether to output a raster of standard errors of the
          interpolated predictions.Standard errors are useful because they
          provide information about the
          reliability of the predicted values. A simple rule of thumb is that
          the true value will fall within two standard errors of the predicted
          value 95 percent of the time. For example, suppose a new location gets
          a predicted value of 50 with a standard error of 5. This means that
          this task's best guess is that the true value at that location is 50,
          but it reasonably could be as low as 40 or as high as 60. To calculate
          this range of reasonable values, multiply the standard error by 2, add
          this value to the predicted value to get the upper end of the range,
          and subtract it from the predicted value to get the lower end of the
          range. If a raster of standard errors for the interpolated
          predictions is requested, it will have the same name as thebut with
          Errors appended. Result layer nameOUTPUT_ERROR-Create a
          prediction error raster.NO_OUTPUT_ERROR-Do not
          create a prediction error raster. This is the
          default.

        """