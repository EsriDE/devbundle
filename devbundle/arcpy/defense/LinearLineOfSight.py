# Generated documentation for module arcpy.defense


class LinearLineOfSight(object):
    """
    Creates lines of sight between observers and targets.
    """

    @property
    def description(self) -> str:
        return """

        LinearLineOfSight_defense(in_observer_features, in_target_features, in_surface, out_los_feature_class, out_sight_line_feature_class, out_observer_feature_class, out_target_feature_class, {in_obstruction_features}, {observer_height_above_surface}, {target_height_above_surface}, {add_profile_attachment})

        Creates lines of sight between observers and targets.

     INPUTS:
      in_observer_features (Feature Set):
          The input observer points.
      in_target_features (Feature Set):
          The input target points.
      in_surface (Raster Layer / Mosaic Dataset / Mosaic Layer):
          The input elevation raster surface.
      in_obstruction_features {Feature Layer}:
          The input multipatch feature that may obstruct the lines of sight.
      observer_height_above_surface {Double}:
          The height that will be added to the surface elevation of the
          observer. The default is 2.
      target_height_above_surface {Double}:
          The height that will be added to the surface elevation of the target.
          The default is 0.
      add_profile_attachment {Boolean}:
          Specifies whether the tool will add an attachment to the feature with
          the profile (cross section terrain graph) between observer and
          target.NO_PROFILE_GRAPH-No profile graph will be added. This is the
          default.ADD_PROFILE_GRAPH-A profile graph will be added.

     OUTPUTS:
      out_los_feature_class (Feature Class):
          The output feature class showing lines of visible and nonvisible
          surface areas.
      out_sight_line_feature_class (Feature Class):
          The output line feature class showing the direct line of sight between
          observer and target.
      out_observer_feature_class (Feature Class):
          The output observer point feature class.
      out_target_feature_class (Feature Class):
          The output target point feature class.

        """