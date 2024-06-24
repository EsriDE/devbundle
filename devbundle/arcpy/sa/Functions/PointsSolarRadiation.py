# Generated documentation for module arcpy.sa.Functions


class PointsSolarRadiation(object):
    """
    Derives incoming solar radiation for specific locations in a point feature class or location table.
    """

    @property
    def description(self) -> str:
        return """

        PointsSolarRadiation_sa(in_surface_raster, in_points_feature_or_table, out_global_radiation_features, {height_offset}, {latitude}, {sky_size}, {time_configuration}, {day_interval}, {hour_interval}, {each_interval}, {z_factor}, {slope_aspect_input_type}, {calculation_directions}, {zenith_divisions}, {azimuth_divisions}, {diffuse_model_type}, {diffuse_proportion}, {transmittivity}, {out_direct_radiation_features}, {out_diffuse_radiation_features}, {out_direct_duration_features})

        Derives incoming solar radiation for specific locations in a point
        feature class or location table.

     INPUTS:
      in_surface_raster (Composite Geodataset):
          The input elevation surface raster.
      in_points_feature_or_table (Table View):
          The input point feature class or table containing the locations where
          solar radiation will be analyzed.
      height_offset {Double}:
          The height (in meters) above the DEM surface for which calculations
          will be performed.The height offset will be applied to all input
          locations.
      latitude {Double}:
          The latitude for the site area. The units are decimal degrees with
          positive values for the northern hemisphere and negative values for
          the southern hemisphere.For input surface rasters containing a spatial
          reference, the mean
          latitude is automatically calculated; otherwise, the latitude default
          is 45 degrees.
      sky_size {Long}:
          The resolution or sky size for the viewshed, sky map, and sun map
          rasters. The units are cells.The default is a raster of 200 by 200
          cells.
      time_configuration {Time configuration}:
          Specifies the time configuration (period) that will be used for
          calculating solar radiation.The Time class objects will be used to
          specify the time configuration.The different types of time
          configurations available are
          TimeWithinDay, TimeMultipleDays, TimeSpecialDays, and
          TimeWholeYear.The following are the forms:TimeWithinDay({day},{startTi
          me},{endTime})TimeMultipleDays({year},{sta
          rtDay},{endDay})TimeSpecialDays()TimeWholeYear({year})The default time
          configuration is TimeMultipleDays with the startDay
          value of 5 and the endDay value of 160 for the current Julian year.
      day_interval {Long}:
          The time interval through the year (units: days) that will be used to
          calculate sky sectors for the sun map.The default value is 14
          (biweekly).
      hour_interval {Double}:
          The time interval through the day (units: hours) that will be used to
          calculate sky sectors for the sun map.The default value is 0.5.
      each_interval {Boolean}:
          Specifies whether a single total insolation value will be calculated
          for all locations or multiple values will be calculated for the
          specified hour and day interval.NOINTERVAL-A single total radiation
          value will be calculated for the
          entire time configuration. This is the default.INTERVAL-Multiple
          radiation values will be calculated for each time
          interval over the entire time configuration. The number of outputs
          depends on the hour or day interval. For example, for a whole year
          with monthly intervals, the result will contain 12 output radiation
          values for each location.
      z_factor {Double}:
          The number of ground x,y units in one surface z-unit.The z-factor
          adjusts the units of measure for the z-units when they
          are different from the x,y units of the input surface. The z-values of
          the input surface are multiplied by the z-factor when calculating the
          final output surface.If the x,y units and z-units are in the same
          units of measure, the
          z-factor is 1. This is the default.If the x,y units and z-units are in
          different units of measure, the
          z-factor must be set to the appropriate factor or the results will be
          incorrect.For example, if the z-units are feet and the x,y units are
          meters, use
          a z-factor of 0.3048 to convert the z-units from feet to meters (1
          foot = 0.3048 meter).
      slope_aspect_input_type {String}:
          Specifies how slope and aspect information will be derived for
          analysis.FROM_DEM-The slope and aspect rasters will be calculated from
          the
          input surface raster. This is the default.FLAT_SURFACE-Constant values
          of zero will be used for slope and
          aspect.FROM_POINTS_TABLE-The slope and aspect values will be specified
          along
          with the x,y coordinates in the locations file.
      calculation_directions {Long}:
          The number of azimuth directions that will be used when calculating
          the viewshed.Valid values must be multiples of 8 (8, 16, 24, 32, and
          so on). The
          default value is 32 directions, which is adequate for complex
          topography.
      zenith_divisions {Long}:
          The number of zenith divisions that will be used to create sky sectors
          in the sky map.The default is eight divisions (relative to zenith).
          Values must be
          greater than zero and less than half the sky size value.
      azimuth_divisions {Long}:
          The number of azimuth divisions that will be used to create sky
          sectors in the sky map.The default is eight divisions (relative to
          north). Valid values must
          be multiples of 8. Values must be greater than zero and less than 160.
      diffuse_model_type {String}:
          Specifies the type of diffuse radiation model that will be
          used.UNIFORM_SKY-The uniform diffuse model will be used. The incoming
          diffuse radiation is the same from all sky directions. This is the
          default.STANDARD_OVERCAST_SKY-The standard overcast diffuse model will
          be
          used. The incoming diffuse radiation flux varies with the zenith
          angle.
      diffuse_proportion {Double}:
          The proportion of global normal radiation flux that is diffuse. Values
          range from 0 to 1.Set this value according to atmospheric conditions.
          The default value
          is 0.3 for generally clear sky conditions.
      transmittivity {Double}:
          The fraction of radiation that passes through the atmosphere (averaged
          overall wavelengths). Values range from 0 (no transmission) to 1 (all
          transmission).The default is 0.5 for a generally clear sky.

     OUTPUTS:
      out_global_radiation_features (Feature Class):
          The output feature class representing the global radiation or amount
          of incoming solar insolation (direct + diffuse) calculated for each
          location. The output has units of watt hours per square meter
          (WH/m).
          2
      out_direct_radiation_features {Feature Class}:
          The output feature class representing the direct incoming solar
          radiation for each location. The output has units of watt hours
          per square meter (WH/m).
          2
      out_diffuse_radiation_features {Feature Class}:
          The output feature class representing the incoming solar radiation for
          each location that is diffuse. The output has units of watt
          hours per square meter (WH/m).
          2
      out_direct_duration_features {Feature Class}:
          The output feature class representing the duration of direct incoming
          solar radiation.The output has units of hours.

        """