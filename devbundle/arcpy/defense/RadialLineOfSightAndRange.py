# Generated documentation for module arcpy.defense


class RadialLineOfSightAndRange(object):
    """
    Shows areas visible to one or more observer locations given a specified distance and viewing angle.
    """

    @property
    def description(self) -> str:
        return """

        RadialLineOfSightAndRange_defense(in_observer_features, in_surface, out_viewshed_feature_class, out_fov_feature_class, out_range_radius_feature_class, {observer_height_offset}, {inner_radius}, {outer_radius}, {horizontal_start_angle}, {horizontal_end_angle})

        Shows areas visible to one or more observer locations given a
        specified distance and viewing angle.

     INPUTS:
      in_observer_features (Feature Set):
          The input observer points.
      in_surface (Raster Layer / Mosaic Dataset / Mosaic Layer):
          The input elevation raster surface. The elevation surface must be
          projected.
      observer_height_offset {Double}:
          The height added to the surface elevation of the observer. The default
          is 2.
      inner_radius {Double}:
          The minimum (nearest) distance from observers to consider for analysis
          in meters. The default is 1000.
      outer_radius {Double}:
          The maximum (farthest) distance from observers to consider for
          analysis in meters. The default is 3000.
      horizontal_start_angle {Double}:
          The left bearing limit in degrees. The default is 0.
      horizontal_end_angle {Double}:
          The right bearing limit in degrees. The default is 360.

     OUTPUTS:
      out_viewshed_feature_class (Feature Class):
          The output polygon feature class showing visible and nonvisible areas.
      out_fov_feature_class (Feature Class):
          The output polygon feature class containing the field of view range
          fan.
      out_range_radius_feature_class (Feature Class):
          The output polygon feature class containing the viewing sector created
          by the range radius, start angle, and end angle.

        """