# Generated documentation for module arcpy.stats


class CentralFeature(object):
    """
    Identifies the most centrally located feature in a point, line, or polygon feature class.
    """

    @property
    def description(self) -> str:
        return """

        CentralFeature_stats(Input_Feature_Class, Output_Feature_Class, Distance_Method, {Weight_Field}, {Self_Potential_Weight_Field}, {Case_Field})

        Identifies the most centrally located feature in a point, line, or
        polygon feature class.

     INPUTS:
      Input_Feature_Class (Feature Layer):
          The feature class containing a distribution of features from which to
          identify the most centrally located feature.
      Distance_Method (String):
          Specifies how distances are calculated from each feature to
          neighboring features.EUCLIDEAN_DISTANCE-The straight-line distance
          between two points (as
          the crow flies)MANHATTAN_DISTANCE-The distance between two points
          measured along axes
          at right angles (city block); calculated by summing the (absolute)
          difference between the x- and y-coordinates
      Weight_Field {Field}:
          The numeric field used to weight distances in the origin-destination
          distance matrix.
      Self_Potential_Weight_Field {Field}:
          The field representing self-potential-the distance or weight between a
          feature and itself.
      Case_Field {Field}:
          Field used to group features for separate central feature
          computations. The case field can be of integer, date, or string type.

     OUTPUTS:
      Output_Feature_Class (Feature Class):
          The feature class that will contain the most centrally located
          feature in the. Input Feature Class

        """