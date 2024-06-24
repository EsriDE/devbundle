# Generated documentation for module arcpy.defense


class RadialLineOfSight(object):
    """
    Shows areas visible to one or more observer locations.
    """

    @property
    def description(self) -> str:
        return """

        RadialLineOfSight_defense(in_observer_features, in_surface, out_feature_class, {radius}, {observer_height_above_surface})

        Shows areas visible to one or more observer locations.

     INPUTS:
      in_observer_features (Feature Set):
          The input observer points.
      in_surface (Raster Layer / Mosaic Dataset / Mosaic Layer):
          The input elevation raster surface.
      radius {Double}:
          The radius of the analysis area from the observer.
      observer_height_above_surface {Double}:
          The height added to the surface elevation of the observer. The default
          is 2.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output polygon feature class showing visible and nonvisible
          surface areas.

        """