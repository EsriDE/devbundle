# Generated documentation for module arcpy.ga


class GACalculateZValue(object):
    """
    Uses the interpolation model in a geostatistical layer to predict a value at a single location.
    """

    @property
    def description(self) -> str:
        return """

        GACalculateZValue_ga(in_geostat_layer, point_coord)

        Uses the interpolation model in a geostatistical layer to predict a
        value at a single location.

     INPUTS:
      in_geostat_layer (Geostatistical Layer):
          The geostatistical layer to be analyzed.
      point_coord (Point):
          The x,y coordinate of the point for which the Z-value will be
          calculated.

        """