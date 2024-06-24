# Generated documentation for module arcpy.gapro


class SummarizeCenterAndDispersion(object):
    """
    Finds central features and directional distributions and calculates mean and median locations from the input.
    """

    @property
    def description(self) -> str:
        return """

        SummarizeCenterAndDispersion_gapro(input_layer, {out_central_feature}, {out_mean_center}, {out_median_center}, {out_ellipse}, {ellipse_size}, {weight_field}, {group_by_field})

        Finds central features and directional distributions and calculates
        mean and median locations from the input.

     INPUTS:
      input_layer (Feature Layer):
          The point, line, or polygon layer to be summarized.
      ellipse_size {String}:
          Specifies the size of output ellipses in standard
          deviations.1_STANDARD_DEVIATION-Output ellipses will cover one
          standard deviation
          of the input features. This is the
          default.2_STANDARD_DEVIATIONS-Output ellipses will cover two standard
          deviations of the input features.3_STANDARD_DEVIATIONS-Output ellipses
          will cover three standard
          deviations of the input features.
      weight_field {Field}:
          A numeric field used to weight locations according to their relative
          importance. This applies to all summary types.
      group_by_field {Field}:
          The field used to group similar features. This applies to all
          summary types. For example, if you choose a field namedthat contains
          values of tree, bush, and grass, all of the features with the value
          tree will be analyzed for their own center or dispersion. This example
          will result in three features, one for each group of tree, bush, and
          grass. PlantType

     OUTPUTS:
      out_central_feature {Feature Class}:
          The output feature class that will contain the most centrally located
          feature in the input layer.
      out_mean_center {Feature Class}:
          The output point feature class that will contain features representing
          the mean centers of the input layer.
      out_median_center {Feature Class}:
          The output point feature class that will contain features representing
          the median centers of the input layer.
      out_ellipse {Feature Class}:
          The output polygon feature class that will contain the directional
          ellipse representation of the input layer.

        """