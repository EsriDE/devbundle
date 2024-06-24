# Generated documentation for module arcpy.sa.Functions


class SpaceTimeKernelDensity(object):
    """
    Expands kernel density calculations from analyzing the relative position and magnitude of the input features to include other dimensions such as time and depth (elevation). The resulting output identifies the magnitude-per-unit area using the multiple kernel functions to fit a smoothly tapered surface to each input point.
    """

    @property
    def description(self) -> str:
        return """

        SpaceTimeKernelDensity_sa(in_features, population_field, {elevation_field}, {elevation_field_unit}, {time_field}, {cell_size}, {kernel_search_radius_xy}, {kernel_search_radius_z}, {kernel_search_time_window}, {resultant_values}, {method}, {min_elevation}, {max_elevation}, {elevation_interval}, {elevation_unit}, {start_time}, {end_time}, {time_interval}, {time_interval_unit})

        Expands kernel density calculations from analyzing the relative
        position and magnitude of the input features to include other
        dimensions such as time and depth (elevation). The resulting output
        identifies the magnitude-per-unit area using the multiple kernel
        functions to fit a smoothly tapered surface to each input point.

     INPUTS:
      in_features (Composite Geodataset):
          The input point features for which density will be calculated.
      population_field (Field):
          The field denoting population values for each feature. The population
          is the count or quantity to be spread across the landscape to create a
          continuous surface.Values in the population field can be integer or
          floating point.Use '' if no item or special value will be used and
          each feature will
          be counted once.
      elevation_field {Field}:
          The field denoting elevation values for each feature.Values in the
          elevation field can be integer or floating point.Use '' to support 3D
          kernel density with time. For 3D features, a pseudo field,,
          will be added to the field
          list. Shape.Z
      elevation_field_unit {String}:
          The unit of measure that will be used for the input elevation field
          value. The default is meters.Use the appropriate unit to represent the
          values in the
          elevation_field parameter value.INCH-Inches will be used.FOOT-Feet
          will be used.YARD-Yards will be
          used.MILE_US-U.S. miles will be used.NAUTICAL_MILE-Nautical miles will
          be used.MILLIMETER-Millimeters will be used.CENTIMETER-Centimeters
          will be used.METER-Meters will be used.KILOMETER-Kilometers will be
          used.DECIMETER-Decimeters will be used.
      time_field {Field}:
          The field denoting time values for each feature.
      cell_size {Analysis Cell Size}:
          The cell size of the multidimensional raster output that will be
          created.The value can be defined by a numeric value or obtained from
          an
          existing raster dataset. If the cell size isn't provided as the
          parameter value, the environment cell size value will be used if
          specified; otherwise, additional rules will be used to calculate it
          from the other inputs. See the tool usage for details.
      kernel_search_radius_xy {Linear Unit}:
          The search radius on the x,y plane within which density will be
          calculated.Define the units to be used. For example, to include all
          features
          within a 1-mile neighborhood when the units are meters, set the search
          radius to 1609.344 (1 mile = 1609.344 meters).
      kernel_search_radius_z {Linear Unit}:
          The vertical search distance in the z-direction within which density
          will be calculated. This vertical distance will be used to search for
          features in the upward and downward directions along the z-axis.Define
          the units to be used.
      kernel_search_time_window {Time Unit}:
          The search range of time within which density will be
          calculated.Define the units to be used.
      resultant_values {String}:
          Specifies what the values in the output raster represent.Since the
          output cell value is linked to the specified cell size, the
          resulting raster cannot be resampled to a different cell
          size.DENSITIES-The output values represent the calculated density
          value per
          unit area for each cell. This is the default.EXPECTED_COUNTS-The
          output values represent the calculated density
          value per cell area.
      method {String}:
          Specifies whether the flat earth (planar) or the shortest path on a
          spheroid (geodesic) method will be used.PLANAR-The planar distance
          between features will be used. This is the
          default.GEODESIC-The geodesic distance between features will be used.
      min_elevation {Double}:
          The start elevation that will be used for the multidimensional raster
          output.
      max_elevation {Double}:
          The end elevation that will be used for the multidimensional raster
          output.
      elevation_interval {Double}:
          The elevation interval between slices in the multidimensional raster
          output.
      elevation_unit {String}:
          Specifies the unit of elevation interval that will be used for the
          multidimensional raster output. The default is meter.INCH-Inches will
          be used.FOOT-Feet will be used.YARD-Yards will be
          used.MILE_US-U.S. miles will be used.NAUTICAL_MILE-Nautical miles will
          be used.MILLIMETER-Millimeters will be used.CENTIMETER-Centimeters
          will be used.METER-Meters will be used.KILOMETER-Kilometers will be
          used.DECIMETER-Decimeters will be used.
      start_time {Date}:
          The start time that will be used for the multidimensional raster
          output.
      end_time {Date}:
          The end time that will be used for the multidimensional raster output.
      time_interval {Double}:
          The time interval between slices in the multidimensional raster
          output.
      time_interval_unit {String}:
          Specifies the unit of time interval that will be used for the
          multidimensional raster output. The default is day.SECOND-The time
          interval unit will be seconds.MINUTE-The time interval
          unit will be minutes.HOUR-The time interval unit will be hours.DAY-The
          time interval unit will be days.WEEK-The time interval unit will be
          weeks.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output kernel density multidimensional raster dataset in Cloud
          Raster Format (.crf). Currently, no other output formats are
          supported.It is always a floating point raster.

        """