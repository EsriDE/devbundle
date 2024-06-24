# Generated documentation for module arcpy.sa.Functions


class ContourWithBarriers(object):
    """
    Creates contours from a raster surface. The inclusion of barrier features allows you to independently generate contours on either side of a barrier.
    """

    @property
    def description(self) -> str:
        return """

        ContourWithBarriers_sa(in_raster, out_contour_feature_class, {in_barrier_features}, {in_contour_type}, {in_contour_values_file}, {explicit_only}, {in_base_contour}, {in_contour_interval}, {in_indexed_contour_interval}, {in_explicit_contours}, {in_z_factor})

        Creates contours from a raster surface. The inclusion of barrier
        features allows you to independently generate contours on either side
        of a barrier.

     INPUTS:
      in_raster (Mosaic Dataset / Mosaic Layer / Raster Dataset / Raster Layer):
          The input surface raster.
      in_barrier_features {Feature Layer}:
          The input barrier features.The features can be polyline or polygon
          type.
      in_contour_type {String}:
          The type of contour to create.POLYLINES-The contour or isoline
          representation of the input
          raster.POLYGONS-Closed polygons representing the contours.
      in_contour_values_file {File}:
          The base contour, contour interval, indexed contour interval, and
          explicit contour values can also be specified via a text file.
      explicit_only {Boolean}:
          Only explicit contour values are used. Base contour, contour interval,
          and indexed contour intervals are not
          specified.NO_EXPLICIT_VALUES_ONLY-The default, contour interval must
          be
          specified.EXPLICIT_VALUES_ONLY-Only explicit contour values are
          specified.
      in_base_contour {Double}:
          The base contour value.Contours are generated above and below this
          value as needed to cover
          the entire value range of the input raster. The default is zero.
      in_contour_interval {Double}:
          The interval, or distance, between contour lines.This can be any
          positive number.
      in_indexed_contour_interval {Double}:
          Contours will also be generated for this interval and will be flagged
          accordingly in the output feature class.
      in_explicit_contours {Double}:
          Explicit values at which to create contours.
      in_z_factor {Double}:
          The unit conversion factor used when generating contours. The default
          value is 1.The contour lines are generated based on the z-values in
          the input
          raster, which are often measured in units of meters or feet. With the
          default value of 1, the contours will be in the same units as the
          z-values of the input raster. To create contours in a unit other than
          that of the z-values, set an appropriate value for the z-factor. It is
          not necessary to have the ground x,y and surface z-units be consistent
          for this tool.For example, if the elevation values in the input raster
          are in feet,
          but you want the contours to be generated based on units of meters,
          set the z-factor to 0.3048 (1 foot = 0.3048 meter).

     OUTPUTS:
      out_contour_feature_class (Feature Class):
          The output contour features.

        """