# Generated documentation for module arcpy.sa.Functions


class LeastCostCorridor(object):
    """
    Calculates the sum of two accumulative cost distance rasters with the option to apply a threshold based on percentage or accumulative cost.
    """

    @property
    def description(self) -> str:
        return """

        LeastCostCorridor_sa(in_accumulative_cost_distance_raster1, in_back_direction_raster1, in_accumulative_cost_distance_raster2, in_back_direction_raster2, {threshold_method}, {threshold})

        Calculates the sum of two accumulative cost distance rasters with the
        option to apply a threshold based on percentage or accumulative cost.

     INPUTS:
      in_accumulative_cost_distance_raster1 (Raster Layer):
          The input raster representing the accumulative cost distance from the
          first source.Use the distance accumulation output from the Distance
          Accumulation or
          Distance Allocation tool.
      in_back_direction_raster1 (Raster Layer):
          The input back direction raster from the first source. The units are
          degrees identifying the next cell along the least-cost path back to
          the first source.Use the back direction output from the Distance
          Accumulation or
          Distance Allocation tool. The range of values is from 0 degrees to 360
          degrees, with 0 reserved for the source cells. Due east (right) is 90,
          and the values increase clockwise (180 is south, 270 is west, and 360
          is north).
      in_accumulative_cost_distance_raster2 (Raster Layer):
          The input raster representing the accumulative cost distance from the
          second source.Use the distance accumulation output from the Distance
          Accumulation or
          Distance Allocation tool.
      in_back_direction_raster2 (Raster Layer):
          The input back direction raster from the second source. The units are
          degrees identifying the next cell along the least-cost path back to
          the second source.Use the back direction output from the Distance
          Accumulation or
          Distance Allocation tool. The range of values is from 0 degrees to 360
          degrees, with 0 reserved for the source cells. Due east (right) is 90,
          and the values increase clockwise (180 is south, 270 is west, and 360
          is north).
      threshold_method {String}:
          Specifies how the threshold will be defined.NO_THRESHOLD-No threshold
          will be applied, and the resulting corridor
          will cover the full extent of the input rasters. This is the
          default.PERCENT_OF_LEAST_COST-The threshold will be defined as a
          percent of
          the minimum value of the summed accumulative cost distance
          rasters.ACCUMULATIVE_COST-The threshold will be defined in
          accumulative cost
          distance units.
      threshold {Double}:
          A percent or accumulative cost threshold that determines whether a
          given cell will be included in the output corridor raster.When the
          threshold_method parameter is set to PERCENT_OF_LEAST_COST,
          the specified value indicates the percent increase to apply from the
          minimum value of the summed accumulative cost distance rasters. When
          the threshold_method parameter is set to ACCUMULATIVE_COST, the value
          indicates cells that have a summed accumulative cost equal to or below
          the value will be included in the corridor.This parameter is only
          enabled if the threshold_method parameter is
          set to PERCENT_OF_LEAST_COST or ACCUMULATIVE_COST.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output corridor raster containing cells with values below the
          threshold in accumulative cost distance units.The output raster is
          floating-point type.

        """