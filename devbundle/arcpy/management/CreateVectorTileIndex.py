# Generated documentation for module arcpy.management


class CreateVectorTileIndex(object):
    """
    Creates a multiscale mesh of polygons that can be used as index polygons when creating vector tile packages.
    """

    @property
    def description(self) -> str:
        return """

        CreateVectorTileIndex_management(in_map, out_featureclass, service_type, {tiling_scheme}, {vertex_count})

        Creates a multiscale mesh of polygons that can be used as index
        polygons when creating vector tile packages.

     INPUTS:
      in_map (Map):
          The input map with the feature distribution and vertex density that
          dictate the size and arrangement of output polygons. The input map is
          typically one that you will subsequently use to create vector tiles
          using the Create Vector Tile Package tool.
      service_type (Boolean):
          Specifies whether the tiling scheme will be generated from an existing
          map service or for ArcGIS Online, Bing Maps, and Google
          Maps.ONLINE-The ArcGIS Online/Bing Maps/Google Maps tiling scheme will
          be
          used. The ArcGIS Online/Bing Maps/Google Maps tiling scheme allows you
          to overlay cache tiles with tiles from these online mapping services.
          ArcGIS Pro includes this tiling scheme as a built-in option when
          loading a tiling scheme. When you choose this tiling scheme, the data
          frame of your source map must use the WGS 1984 Web Mercator (Auxiliary
          Sphere) projected coordinate system. This is the default.EXISTING-The
          tiling scheme from an existing vector tile service will
          be used. Only tiling schemes with scales that double in progression
          through levels and have 512-by-512 tile size are supported. You must
          specify a vector tile service or tiling scheme file in the
          tiling_scheme parameter.
      tiling_scheme {Map Server / File}:
          The vector tile service or tiling scheme file to be used if the
          service_type parameter is set to EXISTING. The tiling scheme tile size
          must be 512 by 512 and must have consecutive scales in a ratio of two.
      vertex_count {Long}:
          The ideal number of vertices from all visible layers to be enclosed by
          each polygon in the output feature class. The default value is the
          recommended count of 10,000 vertices.

     OUTPUTS:
      out_featureclass (Feature Class):
          The output polygon feature class of indexed tiles at each level of
          detail. Each tile encloses a manageable number of input vertices not
          exceeding the number specified by the vertex_count parameter.

        """