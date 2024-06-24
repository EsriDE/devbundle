# Generated documentation for module arcpy.stats


class AverageNearestNeighbor(object):
    """
    Calculates a nearest neighbor index based on the average distance from each feature to its nearest neighboring feature.
    """

    @property
    def description(self) -> str:
        return """

        AverageNearestNeighbor_stats(Input_Feature_Class, Distance_Method, {Generate_Report}, {Area})

        Calculates a nearest neighbor index based on the average distance from
        each feature to its nearest neighboring feature.

     INPUTS:
      Input_Feature_Class (Feature Layer):
          The feature class, typically a point feature class, for which the
          average nearest neighbor distance will be calculated.
      Distance_Method (String):
          Specifies how distances are calculated from each feature to
          neighboring features.EUCLIDEAN_DISTANCE-The straight-line distance
          between two points (as
          the crow flies)MANHATTAN_DISTANCE-The distance between two points
          measured along axes
          at right angles (city block); calculated by summing the (absolute)
          difference between the x- and y-coordinates
      Generate_Report {Boolean}:
          Specifies whether the tool will create a graphical summary of
          results.NO_REPORT-No graphical summary will be created. This is the
          default.GENERATE_REPORT-A graphical summary will be created as an HTML
          file.
      Area {Double}:
          A numeric value representing the study area size. The default value is
          the area of the minimum enclosing rectangle that would encompass all
          features (or all selected features). Units should match those for the
          Output Coordinate System.

        """