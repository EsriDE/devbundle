# Generated documentation for module arcpy.management


class ManageFeatureBinCache(object):
    """
    Manages the feature binning cache for data that has database computed feature binning enabled.
    """

    @property
    def description(self) -> str:
        return """

        ManageFeatureBinCache_management(in_features, {bin_type}, {max_lod}, {add_cache_statistics;add_cache_statistics...}, {delete_cache_statistics;delete_cache_statistics...})

        Manages the feature binning cache for data that has database computed
        feature binning enabled.

     INPUTS:
      in_features (Feature Layer):
          The binned feature class that will have its static cache updated.
      bin_type {String}:
          Specifies the type of feature binning visualization that will be
          enabled.FLAT_HEXAGON-The flat hexagon binning scheme, also known as
          flat
          geohex or flat hexbinning, will be enabled. The tiles are a
          tessellation of hexagons in which the orientation of the hexagons has
          a flat edge of the hexagon on top. This is the default for Microsoft
          SQL Server, Oracle, and PostgreSQL data.POINTY_HEXAGON-The pointy
          hexagon binning scheme, also known as pointy
          geohex or pointy hexbinning, will be enabled. The tiles are a
          tessellation of hexagons in which the orientation of the hexagons has
          a point of the hexagon on top.SQUARE-The square binning scheme in
          which the tiles are a tessellation
          of squares, also known as geosquare or squarebinning, will be enabled.
          This is the default for Db2 data.GEOHASH-The geohash binning scheme in
          which the tiles are a
          tessellation of rectangles will be enabled. Because geohash bins
          always use the WGS84 geographic coordinate system (GCS WGS84, EPSG
          WKID 4326), you cannot specify a bin coordinate system for geohash
          bins.
      max_lod {String}:
          Specifies the maximum level of detail that will be used for the
          cache.Tiling schemes are a continuum of scale ranges. Depending on the
          map,
          you may want to forego caching of some of the extremely large or small
          scales in the tiling scheme. This tool examines the scale dependencies
          in the map and attempts to provide a maximum range of scale for
          caching. Choose a level of detail that most closely matches the
          intended use of the map in which the data will be shown.WORLD-A world
          scale will be used as the maximum level of
          detail.CONTINENTS-Multiple continents scale will be used as the
          maximum level
          of detail.CONTINENT-A single continent scale will be used as the
          maximum level
          of detail.COUNTRIES-Multiple countries scale will be used as the
          maximum level
          of detail.COUNTRY-A single country scale will be used as the maximum
          level of
          detail.STATES-Multiple states scale will be used as the maximum level
          of
          detail.STATE-A single state scale will be used as the maximum level of
          detail.COUNTIES-Multiple counties scale will be used as the maximum
          level of
          detail.COUNTY-A single county scale will be used as the maximum level
          of
          detail.CITIES-Multiple cities scale will be used as the maximum level
          of
          detail.CITY-A single city scale will be used as the maximum level of
          detail.
      add_cache_statistics {Value Table}:
          Specifies the statistics that will be summarized and stored in
          the bin cache. Statistics are used to symbolize bins and provide
          aggregate information for all the points in a bin. One summary
          statistic, shape_count (which is the total feature count), is always
          available. Field-The field on which the summary statistics will
          be calculated.
          Supported field types are short integer, long integer, big integer,
          float, and double. Statistic Type-The type of statistic that
          will be calculated
          for the specified field. Statistics are calculated for all features in
          the bin. Available statistics types are as follows:          Mean
          (AVG)-The mean (average value) for the specified field will be
          calculated.Minimum (MIN)-The minimum (smallest value) of all records
          for the
          specified field will be identified.Maximum (MAX)-The maximum (largest
          value) of all records for the
          specified field will be identified.Standard deviation (STDDEV)-The
          standard deviation value for the field
          will be calculated.Sum (SUM)-The sum of the values for the specified
          field will be
          calculated.
      delete_cache_statistics {String}:
          The summary statistic that will be deleted from the cache. You cannot
          delete the default COUNT summary statistic.

        """