# Generated documentation for module arcpy.stats


class MedianCenter(object):
    """
    Identifies the location that minimizes overall Euclidean distance to the features in a dataset.
    """

    @property
    def description(self) -> str:
        return """

        MedianCenter_stats(Input_Feature_Class, Output_Feature_Class, {Weight_Field}, {Case_Field}, {Attribute_Field;Attribute_Field...})

        Identifies the location that minimizes overall Euclidean distance to
        the features in a dataset.

     INPUTS:
      Input_Feature_Class (Feature Layer):
          A feature class for which the median center will be calculated.
      Weight_Field {Field}:
          The numeric field used to create a weighted median center.
      Case_Field {Field}:
          Field used to group features for separate median center calculations.
          The case field can be of integer, date, or string type.
      Attribute_Field {Field}:
          Numeric field(s) for which the data median value will be computed.

     OUTPUTS:
      Output_Feature_Class (Feature Class):
          A point feature class that will contain the features representing the
          median centers of the input feature class.

        """