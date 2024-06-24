# Generated documentation for module arcpy.maritime


class ExpandCollapsedContours(object):
    """
    Expands (pulls apart) contour lines that are snapped together. This preserves representative depth areas.
    """

    @property
    def description(self) -> str:
        return """

        ExpandCollapsedContours_maritime(target_contours, expansion_distance)

        Expands (pulls apart) contour lines that are snapped together. This
        preserves representative depth areas.

     INPUTS:
      target_contours (Feature Layer):
          The feature class containing the contours to be expanded.
      expansion_distance (Double):
          The distance that contours will be expanded based on the coordinate
          system of the target contours. The default is 5e-7 decimal degrees
          based on the WGS84 geographic coordinate system.

        """