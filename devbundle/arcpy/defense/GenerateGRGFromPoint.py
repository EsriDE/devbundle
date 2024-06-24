# Generated documentation for module arcpy.defense


class GenerateGRGFromPoint(object):
    """
    Generates a Gridded Reference Graphic (GRG) as a polygon feature class over a specified area with a custom size.
    """

    @property
    def description(self) -> str:
        return """

        GenerateGRGFromPoint_defense(in_feature, out_feature_class, {horizontal_cells}, {vertical_cells}, {cell_width}, {cell_height}, {cell_units}, {label_start_position}, {label_format}, {label_separator}, {grid_angle}, {grid_angle_units})

        Generates a Gridded Reference Graphic (GRG) as a polygon feature class
        over a specified area with a custom size.

     INPUTS:
      in_feature (Feature Set):
          The center point for the GRG starting point.
      horizontal_cells {Long}:
          The number of horizontal grid cells.
      vertical_cells {Long}:
          The number of vertical grid cells.
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
      grid_angle {Double}:
          The angle used to rotate the grid.
      grid_angle_units {String}:
          The angular units for grid rotation.DEGREES-The angle will be degrees.
          This is the default.MILS-The angle
          will be mils.RADS-The angle will be radians.GRADS-The angle will be
          gradians.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output polygon feature class containing the GRG to be created.

        """