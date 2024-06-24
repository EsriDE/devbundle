# Generated documentation for module arcpy.stats


class MeanCenter(object):
    """
    Identifies the geographic center (or the center of concentration) for a set of features.
    """

    @property
    def description(self) -> str:
        return """

        MeanCenter_stats(Input_Feature_Class, Output_Feature_Class, {Weight_Field}, {Case_Field}, {Dimension_Field})

        Identifies the geographic center (or the center of concentration) for
        a set of features.

     INPUTS:
      Input_Feature_Class (Feature Layer):
          A feature class for which the mean center will be calculated.
      Weight_Field {Field}:
          The numeric field used to create a weighted mean center.
      Case_Field {Field}:
          Field used to group features for separate mean center calculations.
          The case field can be of integer, date, or string type.
      Dimension_Field {Field}:
          A numeric field containing attribute values from which an average
          value will be calculated.

     OUTPUTS:
      Output_Feature_Class (Feature Class):
          A point feature class that will contain the features representing the
          mean centers of the input feature class.

        """