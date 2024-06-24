# Generated documentation for module arcpy.sfa


class InterpolatePoints(object):
    """
    Predicts values at new locations based on measurements from a collection of points. The tool uses point data with values at each point as input and makes areas classified by predicted values.
    """

    @property
    def description(self) -> str:
        return """

        InterpolatePoints_sfa(inputLayer, outputName, {field}, {interpolateOption}, {outputPredictionError}, {classificationType}, {numClasses}, {classBreaks;classBreaks...}, {boundingPolygonLayer}, {predictAtPointLayer})

        Predicts values at new locations based on measurements from a
        collection of points. The tool uses point data with values at each
        point as input and makes areas classified by predicted values.

     INPUTS:
      inputLayer (Feature Set):
          The point features that will be interpolated to a continuous surface
          layer.
      outputName (String):
          The name of the output layer to create on your portal.
      field {Field}:
          The numeric field containing the values you want to interpolate.
      interpolateOption {String}:
          Controls your preference for speed versus accuracy, from fastest to
          most accurate. More accurate predictions take longer to
          calculate.1-Speed.5-Balanced. This is the default.9-Accuracy.
      outputPredictionError {Boolean}:
          If checked, a polygon layer of standard errors for the interpolation
          predictions will be output.Standard errors are useful because they
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
          range.NO_ERROR-Do not create a prediction error output layer. This is
          the
          default.OUTPUT_ERROR-Create a prediction error output layer.
      classificationType {String}:
          Determines how predicted values will be classified into
          polygons.EQUALINTERVAL-Polygons are created such that the range of
          density
          values is equal for each area.GEOMETRICINTERVAL-Polygons are based on
          class intervals that have a
          geometric series. This method ensures that each class range has
          approximately the same number of values within each class and that the
          change between intervals is consistent. This is the default.EQUALAREA-
          Polygons are created such that the size of each area is
          equal. For example, if the result has more high-density values than
          low-density values, more polygons will be created for high
          densities.MANUAL-You define your own range of values for areas. These
          values
          will be entered as class breaks.
      numClasses {Long}:
          This value is used to divide the range of predicted values into
          distinct classes. The range of values in each class is determined by
          the classification type. Each class defines the boundaries of the
          result polygons.The default is 10 and the maximum is 32.
      classBreaks {Double}:
          To do a manual classification, supply the desired class break values.
          These values define the upper limit of each class, so the number of
          classes will equal the number of entered values. Areas will not be
          created for any locations with predicted values above the largest
          entered break value. You must enter at least 2 values and no more than
          32.
      boundingPolygonLayer {Feature Set}:
          A layer specifying the polygons where you want values to be
          interpolated. For example, if you are interpolating densities of fish
          within a lake, you can use the boundary of the lake in this parameter
          and the output will only contain polygons within the boundary of the
          lake.
      predictAtPointLayer {Feature Set}:
          An optional layer specifying point locations to calculate prediction
          values. This allows you to make predictions at specific locations of
          interest. For example, if the input layer represents measurements of
          pollution levels, you can use this parameter to predict the pollution
          levels of locations with large at-risk populations, such as schools or
          hospitals. You can then use this information to give recommendations
          to health officials in those locations.

        """