# Generated documentation for module arcpy.sa.Functions


class ContourList(object):
    """
    Creates a feature class of selected contour values from a raster surface.
    """

    @property
    def description(self) -> str:
        return """

        ContourList_sa(in_raster, out_polyline_features, contour_values;contour_values...)

        Creates a feature class of selected contour values from a raster
        surface.

     INPUTS:
      in_raster (Composite Geodataset):
          The input surface raster.
      contour_values (Double):
          List of z-values for which to create contours.

     OUTPUTS:
      out_polyline_features (Feature Class):
          The output contour polyline features.

        """