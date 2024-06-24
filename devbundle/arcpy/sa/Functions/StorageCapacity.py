# Generated documentation for module arcpy.sa.Functions


class StorageCapacity(object):
    """
    Creates a table and a chart of elevations and corresponding storage capacities for an input surface raster. The tool calculates the surface area and total volume of the underlying region at a series of elevation increments.
    """

    @property
    def description(self) -> str:
        return """

        StorageCapacity_sa(in_surface_raster, out_table, {in_zone_data}, {zone_field}, {analysis_type}, {min_elevation}, {max_elevation}, {increment_type}, {increment}, {z_unit}, {out_chart})

        Creates a table and a chart of elevations and corresponding storage
        capacities for an input surface raster. The tool calculates the
        surface area and total volume of the underlying region at a series of
        elevation increments.

     INPUTS:
      in_surface_raster (Raster Layer):
          The input raster representing a continuous surface.
      in_zone_data {Raster Layer / Feature Layer}:
          The dataset that defines the zones.The zones can be defined by an
          integer raster or a feature layer.
      zone_field {Field}:
          The field that contains the values that define each zone.It can be an
          integer or a string field of the zone dataset.
      analysis_type {String}:
          Specifies the analysis type.AREA_VOLUME-Both surface areas and total
          volumes are calculated at
          each elevation increment. This is the default.AREA-Surface area is
          calculated at each elevation increment.VOLUME-Total volume is
          calculated at each elevation increment.
      min_elevation {Double}:
          The minimum elevation from which storage capacities are assessed.By
          default, the tool uses the minimum surface raster value in each
          zone as the minimum elevation for that zone. If a value is provided,
          it is used as the minimum elevation across all zones.
      max_elevation {Double}:
          The maximum elevation from which storage capacities are assessed.By
          default, the tool uses the maximum surface raster value in each
          zone as the maximum elevation for that zone. If a value is provided,
          it is used as the maximum elevation across all zones.
      increment_type {String}:
          Specifies the increment type to use when computing elevation
          increments between minimum and maximum
          elevations.NUMBER_OF_INCREMENTS-The number of increments between
          minimum and
          maximum elevations is used. This is the default.VALUE_OF_INCREMENT-The
          elevation difference between each increment is
          used.
      increment {Double}:
          An incremental value that is either the number of increments or the
          difference in elevation between increments. The value is determined
          based on the increment type parameter value.
      z_unit {String}:
          Specifies the linear unit that will be used for vertical
          z-values.INCH-The linear unit will be inches.FOOT-The linear unit will
          be
          feet.YARD-The linear unit will be yards.MILE_US-The linear unit will
          be miles.NAUTICAL_MILE-The linear unit will be nautical
          miles.MILLIMETER-The linear unit will be millimeters.CENTIMETER-The
          linear unit will be centimeters.METER-The linear unit will be
          meters.KILOMETER-The linear unit will be kilometers.DECIMETER-The
          linear unit will be decimeters.
      out_chart {String}:
          The name of the output chart for display.

     OUTPUTS:
      out_table (Table):
          The output table that contains for each zone the surface area and
          total volumes for each increment in elevation.

        """