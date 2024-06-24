# Generated documentation for module arcpy.agolservices


class Watershed(object):
    """
    Determines the contributing area above each input point. A watershed is the upslope area that contributes flow.
    """

    @property
    def description(self) -> str:
        return """

        Watershed_agolservices(InputPoints, {PointIDField}, {SnapDistance}, {SnapDistanceUnits}, {DataSourceResolution}, {Generalize}, {ReturnSnappedPoints})

        Determines the contributing area above each input point. A watershed
        is the upslope area that contributes flow.

     INPUTS:
      InputPoints (Feature Set):
          The point features used for calculating watersheds. These are referred
          to as pour points, because it is the location at which water pours out
          of the watershed.
      PointIDField {String}:
          An integer or string field used to identify to the input points.The
          default is to use the unique ID field.
      SnapDistance {String}:
          The maximum distance to move the location of an input
          point.Interactive input points and documented gage locations may not
          exactly
          align with the stream location in the DEM. This parameter allows the
          service to move the point to a nearby location with the largest
          contributing area.By default, the snapping distance is calculated as
          the resolution of
          the source data multiplied by 5.
      SnapDistanceUnits {String}:
          The linear units specified for the snap distance.Meters-The units are
          meters. This is the default.Kilometers-The units
          are kilometers.Feet-The units are feet.Yards-The units are
          yards.Miles-The units are miles.
      DataSourceResolution {String}:
          Specifies the source data resolution that will be used in the
          analysis. The values are an approximation of the spatial resolution of
          the digital elevation model used to build the foundation hydrologic
          database. Since many elevation sources are distributed in units of arc
          seconds, an approximation is provided in meters for easier
          understanding.Blank-The hydrologic source, built from a 3-arc second
          data source,
          which is approximately 90-meter resolution elevation data, will be
          used. This is the default.FINEST-The finest resolution available at
          each location from all
          possible data sources will be used.10m-The hydrologic source, built
          from a 1/3 arc second data source,
          which is approximately 10-meter resolution elevation data, will be
          used.30m-The hydrologic source, built from a 1-arc second data source,
          which is approximately 30-meter resolution elevation data, will be
          used.90m-The hydrologic source, built from a 3-arc second data source,
          which is approximately 90-meter resolution elevation data, will be
          used.
      Generalize {Boolean}:
          Specifies whether the output watersheds will be smoothed into simpler
          shapes or conform to the cell edges of the original DEM.True-The
          polygon boundaries will be smoothed into simpler
          shapes.False-The edges of the polygons will conform to the cell edges
          of the
          original DEM. This is the default.
      ReturnSnappedPoints {Boolean}:
          Determines if a point feature at the watershed's pour point will be
          returned. If snapping is enabled, this might not be the same as the
          input point.True-A point feature will be returned.False-No point
          features will be
          returned. This is the default.

        """