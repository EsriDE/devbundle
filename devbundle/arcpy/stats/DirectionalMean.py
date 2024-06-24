# Generated documentation for module arcpy.stats


class DirectionalMean(object):
    """
    Identifies the mean direction, length, and geographic center for a set of lines.
    """

    @property
    def description(self) -> str:
        return """

        DirectionalMean_stats(Input_Feature_Class, Output_Feature_Class, Orientation_Only, {Case_Field})

        Identifies the mean direction, length, and geographic center for a set
        of lines.

     INPUTS:
      Input_Feature_Class (Feature Layer):
          The feature class containing vectors for which the mean direction will
          be calculated.
      Orientation_Only (Boolean):
          Specifies whether to include direction (From and To nodes) information
          in the analysis.DIRECTION-The From and To nodes are utilized in
          calculating the mean.
          This is the default.ORIENTATION_ONLY-The From and To node information
          is ignored.
      Case_Field {Field}:
          Field used to group features for separate directional mean
          calculations. The case field can be of integer, date, or string type.

     OUTPUTS:
      Output_Feature_Class (Feature Class):
          A line feature class that will contain the features representing the
          mean directions of the input feature class.

        """