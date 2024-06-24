# Generated documentation for module arcpy.sa.Functions


class CreateAccuracyAssessmentPoints(object):
    """
    Creates randomly sampled points for postclassification accuracy assessment.
    """

    @property
    def description(self) -> str:
        return """

        CreateAccuracyAssessmentPoints_sa(in_class_data, out_points, {target_field}, {num_random_points}, {sampling}, {polygon_dimension_field})

        Creates randomly sampled points for postclassification accuracy
        assessment.

     INPUTS:
      in_class_data (Mosaic Layer / Raster Layer / Feature Layer):
          The input classification image or other thematic GIS reference data.
          The input can be a raster or feature class.Typical data is a
          classification image of a single band, integer data
          type.If using polygons as input, only use those that are not used as
          training samples. They can also be GIS land-cover data in shapefile or
          feature class format.
      target_field {String}:
          Specifies whether the input data is a classified image or ground truth
          data.CLASSIFIED-The input is a classified image. This is the
          default.GROUND_TRUTH-The input is reference data.
      num_random_points {Long}:
          The total number of random points that will be generated.The actual
          number may exceed but never fall below this number,
          depending on sampling strategy and number of classes. The default
          number of randomly generated points is 500.
      sampling {String}:
          Specifies the sampling scheme that will be
          used.STRATIFIED_RANDOM-Randomly distributed points will be created in
          each
          class, in which each class has a number of points proportional to its
          relative area. This is the defaultEQUALIZED_STRATIFIED_RANDOM-Randomly
          distributed points will be
          created in each class, in which each class has the same number of
          points.RANDOM-Randomly distributed points will be created throughout
          the
          image.
      polygon_dimension_field {Field}:
          A field that defines the dimension (time) of the features. This
          parameter is used only if the classification result is a
          multidimensional raster and you want to generate assessment points
          from a feature class, such as land classification polygons for
          multiple years.

     OUTPUTS:
      out_points (Feature Class):
          The output point shapefile or feature class that contains the random
          points to be used for accuracy assessment.

        """