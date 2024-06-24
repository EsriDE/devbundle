# Generated documentation for module arcpy.gapro


class CalculateDensity(object):
    """
    Calculates a magnitude-per-unit area from point features that fall within a neighborhood around each cell.
    """

    @property
    def description(self) -> str:
        return """

        CalculateDensity_gapro(input_layer, out_feature_class, bin_type, bin_size, weight, neighborhood_size, {fields;fields...}, {area_unit_scale_factor}, {time_step_interval}, {time_step_repeat}, {time_step_reference})

        Calculates a magnitude-per-unit area from point features that fall
        within a neighborhood around each cell.

     INPUTS:
      input_layer (Feature Layer):
          The points that will be used to calculate the density.
      bin_type (String):
          Specifies the bin shape that will be used in the analysis.SQUARE-The
          bin shape will be square. This is the default.HEXAGON-The
          bin shape will be hexagonal.
      bin_size (Linear Unit):
          The size of the bins used to aggregate input features. When generating
          bins for squares, the number and units specified determine the height
          and length of the square. For hexagons, the number and units specified
          determine the distance between parallel sides.
      weight (String):
          Specifies the weighting that will be applied to the density
          function.UNIFORM-A magnitude-per-area calculation in which each bin is
          equally
          weighted will be used. This is the default.KERNEL-A magnitude-per-area
          calculation with a smoothing algorithm
          applied (kernel) that weights bins closer to the points more heavily
          will be used.
      neighborhood_size (Linear Unit):
          The search radius that will be applied to density calculations.
      fields {Field}:
          One or more fields denoting population values for each feature. The
          population field is the count or quantity to be spread across the
          landscape to create a continuous surface.Values in the population
          field must be numeric. By default, the
          density of the count of input points will always be calculated.
      area_unit_scale_factor {String}:
          Specifies the areal units that will be used for the output density
          values. The default unit is based on the units of the output spatial
          reference.ACRES-The areal units will be international
          acres.HECTARES-The areal
          units will be hectares.SQUARE_MILES-The areal units will be square
          statute miles.SQUARE_KILOMETERS-The areal units will be square
          kilometers.SQUARE_METERS-The areal units will be square
          meters.SQUARE_FEET-The areal units will be square
          feet.SQUARE_YARDS-The areal units will be square
          yards.SQUARE_MILES_US-The areal units will be square US survey
          miles.SQUARE_FEET_US-The areal units will be square US survey
          feet.SQUARE_YARDS_US-The areal units will be square US survey
          yards.ACRES_US-The areal units will be US survey acres.
      time_step_interval {Time Unit}:
          A value that specifies the duration of the time step. This parameter
          is only available if the input points are time enabled and represent
          an instant in time.Time stepping can only be applied if time is
          enabled on the input.
      time_step_repeat {Time Unit}:
          A value that specifies how often the time-step interval occurs. This
          parameter is only available if the input points are time enabled and
          represent an instant in time.
      time_step_reference {Date}:
          A date that specifies the reference time with which to align the time
          steps. The default is January 1, 1970, at 12:00 a.m. This parameter is
          only available if the input points are time enabled and represent an
          instant in time.

     OUTPUTS:
      out_feature_class (Feature Class):
          A new feature class with calculated densities.

        """