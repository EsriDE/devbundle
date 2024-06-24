# Generated documentation for module arcpy.stats


class DirectionalDistribution(object):
    """
    Creates standard deviational ellipses or ellipsoids to summarize the spatial characteristics of geographic features: central tendency, dispersion, and directional trends.
    """

    @property
    def description(self) -> str:
        return """

        DirectionalDistribution_stats(Input_Feature_Class, Output_Ellipse_Feature_Class, Ellipse_Size, {Weight_Field}, {Case_Field})

        Creates standard deviational ellipses or ellipsoids to summarize the
        spatial characteristics of geographic features: central tendency,
        dispersion, and directional trends.

     INPUTS:
      Input_Feature_Class (Feature Layer):
          A feature class containing a distribution of features for which the
          standard deviational ellipse or ellipsoid will be calculated.
      Ellipse_Size (String):
          The size of output ellipses in standard deviations. The default
          ellipse size is 1; valid choices are 1, 2, or 3 standard
          deviations.1_STANDARD_DEVIATION-1 standard
          deviation2_STANDARD_DEVIATIONS-2
          standard deviations3_STANDARD_DEVIATIONS-3 standard deviations
      Weight_Field {Field}:
          The numeric field used to weight locations according to their relative
          importance.
      Case_Field {Field}:
          The field used to group features for separate directional distribution
          calculations. The case field can be of integer, date, or string type.

     OUTPUTS:
      Output_Ellipse_Feature_Class (Feature Class):
          A polygon feature class that will contain the output ellipse feature.

        """