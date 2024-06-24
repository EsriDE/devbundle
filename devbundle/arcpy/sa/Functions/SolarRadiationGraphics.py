# Generated documentation for module arcpy.sa.Functions


class SolarRadiationGraphics(object):
    """
    Derives raster representations of a hemispherical viewshed, sun map, and sky map, which are used in the calculation of direct, diffuse, and global solar radiation.
    """

    @property
    def description(self) -> str:
        return """

        SolarRadiationGraphics_sa(in_surface_raster, {in_points_feature_or_table}, {sky_size}, {height_offset}, {calculation_directions}, {latitude}, {time_configuration}, {day_interval}, {hour_interval}, {out_sunmap_raster}, {zenith_divisions}, {azimuth_divisions}, {out_skymap_raster})

        Derives raster representations of a hemispherical viewshed, sun map,
        and sky map, which are used in the calculation of direct, diffuse, and
        global solar radiation.

     INPUTS:
      in_surface_raster (Composite Geodataset):
          The input elevation surface raster.
      in_points_feature_or_table {Table View}:
          The input point feature class or table containing the locations where
          solar radiation will be analyzed.
      sky_size {Long}:
          The resolution or sky size for the viewshed, sky map, and sun map
          rasters. The units are cells.The default is a raster of 200 by 200
          cells.
      height_offset {Double}:
          The height (in meters) above the DEM surface for which calculations
          will be performed.The height offset will be applied to all input
          locations.
      calculation_directions {Long}:
          The number of azimuth directions that will be used when calculating
          the viewshed.Valid values must be multiples of 8 (8, 16, 24, 32, and
          so on). The
          default value is 32 directions, which is adequate for complex
          topography.
      latitude {Double}:
          The latitude for the site area. The units are decimal degrees with
          positive values for the northern hemisphere and negative values for
          the southern hemisphere.For input surface rasters containing a spatial
          reference, the mean
          latitude is automatically calculated; otherwise, the latitude default
          is 45 degrees.
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

     OUTPUTS:
      out_viewshed_raster (Raster Dataset):
          The output viewshed raster.The resulting viewshed for a location
          represents which sky directions
          are visible and which are obscured. This is similar to the view
          provided by upward-looking hemispherical (fisheye) photographs.
      out_sunmap_raster {Raster Dataset}:
          The output sun map raster.The output is a representation that
          specifies sun tracks, the apparent
          position of the sun as it varies through time. The output is at the
          same resolution as the viewshed and sky map.
      out_skymap_raster {Raster Dataset}:
          The output sky map raster.The output is constructed by dividing the
          whole sky into a series of
          sky sectors defined by zenith and azimuth divisions. The output is at
          the same resolution as the viewshed and sun map.

        """