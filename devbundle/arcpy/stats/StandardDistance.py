# Generated documentation for module arcpy.stats


class StandardDistance(object):
    """
    Measures the degree to which features are concentrated or dispersed around the geometric mean center.
    """

    @property
    def description(self) -> str:
        return """

        StandardDistance_stats(Input_Feature_Class, Output_Standard_Distance_Feature_Class, Circle_Size, {Weight_Field}, {Case_Field})

        Measures the degree to which features are concentrated or dispersed
        around the geometric mean center.

     INPUTS:
      Input_Feature_Class (Feature Layer):
          A feature class containing a distribution of features for which the
          standard distance will be calculated.
      Circle_Size (String):
          Specifies the size of output circles in standard
          deviations.1_STANDARD_DEVIATION-The output circles will be 1 standard
          deviation.
          This is the default.2_STANDARD_DEVIATIONS-The output circles will be 2
          standard
          deviations.3_STANDARD_DEVIATIONS-The output circles will be 3 standard
          deviations.
      Weight_Field {Field}:
          The numeric field used to weight locations according to their relative
          importance.
      Case_Field {Field}:
          The field used to group features for separate standard distance
          calculations. The case field can be of integer, date, or string type.

     OUTPUTS:
      Output_Standard_Distance_Feature_Class (Feature Class):
          A polygon feature class that will contain a circle polygon for each
          input center. These circle polygons graphically portray the standard
          distance at each center point.

        """