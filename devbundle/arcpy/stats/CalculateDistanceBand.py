# Generated documentation for module arcpy.stats


class CalculateDistanceBand(object):
    """
    Returns the minimum, the maximum, and the average distance to the specified Nth nearest neighbor (N is an input parameter) for a set of features. Results are written as tool execution messages.
    """

    @property
    def description(self) -> str:
        return """

        CalculateDistanceBand_stats(Input_Features, Neighbors, Distance_Method)

        Returns the minimum, the maximum, and the average distance to the
        specified Nth nearest neighbor (N is an input parameter) for a set of
        features. Results are written as tool execution messages.

     INPUTS:
      Input_Features (Feature Layer):
          The feature class or layer used to calculate distance statistics.
      Neighbors (Long):
          The number of neighbors (N) to consider for each feature. This number
          should be any integer between one and the total number of features in
          the feature class. A list of distances between each feature and its
          Nth neighbor is compiled, and the maximum, minimum, and average
          distances are output to the Results window.
      Distance_Method (String):
          Specifies how distances are calculated from each feature to
          neighboring features.EUCLIDEAN_DISTANCE-The straight-line distance
          between two points (as
          the crow flies)MANHATTAN_DISTANCE-The distance between two points
          measured along axes
          at right angles (city block); calculated by summing the (absolute)
          difference between the x- and y-coordinates

        """