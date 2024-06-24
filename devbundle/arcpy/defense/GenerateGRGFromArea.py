# Generated documentation for module arcpy.defense


class GenerateGRGFromArea(object):
    """
    Generates a Gridded Reference Graphic (GRG) over a specified area with a custom size based on a bounding polygon.
    """

    @property
    def description(self) -> str:
        return """

        GenerateGRGFromArea_defense(in_feature, out_feature_class, {cell_width}, {cell_height}, {cell_units}, {label_start_position}, {label_format}, {label_separator})

        Generates a Gridded Reference Graphic (GRG) over a specified area with
        a custom size based on a bounding polygon.

     INPUTS:
      in_feature (Feature Set):
          The input polygon feature on which the GRG will be based.
      cell_width {Double}:
          The width of the cells. Measurement units are specified by
          theparameter. Cell Units
      cell_height {Double}:
          The height of the cells. Measurement units are specified by
          theparameter. Cell Units
      cell_units {String}:
          Specifies the measurement units for cell width and height.METERS-The
          unit will be meters. This is the default.KILOMETERS-The
          unit will be kilometers.MILES-The unit will be
          miles.NAUTICAL_MILES-The unit will be nautical miles.FEET-The unit
          will be feet.US_SURVEY_FEET-The unit will be U.S. survey feet.
      label_start_position {String}:
          Specifies the grid cell where labelling will start.UPPER_LEFT-The
          label position will be the upper left. This is the
          default.LOWER_LEFT-The label position will be the lower
          left.UPPER_RIGHT-The label position will be the upper
          right.LOWER_RIGHT-The label position will be the lower right.
      label_format {String}:
          Specifies the labeling type for each grid cell.ALPHA_NUMERIC-The label
          will use an alpha character, a separator, and
          a number. This is the default.ALPHA_ALPHA-The label will use an alpha
          character, a separator, and an
          additional alpha character.NUMERIC-The label will be numeric.
      label_separator {String}:
          Specifies the separator to be used between x- and y-values when the
          label_format parameter is set to ALPHA_ALPHA, for example, A-A, A-AA,
          AA-A.--The label separator will be a hyphen. This is the default.,-The
          label separator will be a comma..-The label separator will be a
          period./-The label separator will be a forward slash.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output polygon feature class containing the GRG.

        """