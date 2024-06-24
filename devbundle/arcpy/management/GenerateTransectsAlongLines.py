# Generated documentation for module arcpy.management


class GenerateTransectsAlongLines(object):
    """
    Creates perpendicular transect lines at a regular interval along lines.
    """

    @property
    def description(self) -> str:
        return """

        GenerateTransectsAlongLines_management(in_features, out_feature_class, interval, transect_length, {include_ends})

        Creates perpendicular transect lines at a regular interval along
        lines.

     INPUTS:
      in_features (Feature Layer):
          The line features along which perpendicular transect lines will be
          generated.
      interval (Linear Unit):
          The interval from the beginning of the feature at which transects will
          be placed.
      transect_length (Linear Unit):
          The length or width of the transect line. Each transect will be placed
          in such a way along the input line that half its length falls on one
          side of the line, and half its length falls on the other side of the
          line.This is the overall length of each transect line, not the
          distance
          that the transect extends from the input line. To specify how far the
          transect line should extend from the input line-for example, 100
          meters-double this value to specify the transect length (200 meters).
      include_ends {Boolean}:
          Specifies whether transects will be generated at the start and end of
          the input line.END_POINTS-Transects will be generated at the start and
          end of the
          input line.NO_END_POINTS-Transects will not be generated at the start
          and end of
          the input line. This is the default.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output perpendicular transect lines generated along the input
          features.

        """