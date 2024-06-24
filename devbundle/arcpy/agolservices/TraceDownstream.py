# Generated documentation for module arcpy.agolservices


class TraceDownstream(object):
    """
    Determines the path water will take from a particular location to its furthest downhill path.
    """

    @property
    def description(self) -> str:
        return """

        TraceDownstream_agolservices(InputPoints, {PointIDField}, {DataSourceResolution}, {Generalize})

        Determines the path water will take from a particular location to its
        furthest downhill path.

     INPUTS:
      InputPoints (Feature Set):
          The point features used for calculating downstream trace.
      PointIDField {String}:
          An integer or string field used to identify the input points.The
          default is to use the unique ID field.
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
          Specifies whether the output downstream trace lines will be smoothed
          into simpler lines or conform to the cell centers of the original
          DEM.True-The lines will be smoothed into simpler lines.False-The lines
          will not be smoothed. Each trace line of output
          downstream trace have more vertices since they conform to the original
          DEM cell centers. This is the default.

        """