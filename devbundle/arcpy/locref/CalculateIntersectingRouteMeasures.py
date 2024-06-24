# Generated documentation for module arcpy.locref


class CalculateIntersectingRouteMeasures(object):
    """
    Creates a table of all the routes and measures at each intersection location.
    """

    @property
    def description(self) -> str:
        return """

        CalculateIntersectingRouteMeasures_locref(in_intersection_feature_class, out_dataset, {tvd})

        Creates a table of all the routes and measures at each intersection
        location.

     INPUTS:
      in_intersection_feature_class (Feature Layer):
          The input LRS intersection feature class or layer.
      tvd {Date}:
          Filters routes that have been edited after a certain date so that
          intersections can be generated according to that filter.

     OUTPUTS:
      out_dataset (Table):
          The output table to which the results will be posted.

        """