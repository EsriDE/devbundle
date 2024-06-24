# Generated documentation for module arcpy.management


class CreateVectorTilePackage(object):
    """
    Generates vector tiles from a map or basemap and packages the tiles in a single .vtpk file.
    """

    @property
    def description(self) -> str:
        return """

        CreateVectorTilePackage_management(in_map, output_file, service_type, {tiling_scheme}, {tile_structure}, min_cached_scale, max_cached_scale, {index_polygons}, {summary}, {tags})

        Generates vector tiles from a map or basemap and packages the tiles in
        a single .vtpk file.

     INPUTS:
      in_map (Map):
          The map from which tiles will be generated and packaged. The input map
          must have metadata description and tags.
      service_type (Boolean):
          Specifies whether the tiling scheme will be generated from an existing
          map service or if map tiles will be generated for ArcGIS Online, Bing
          Maps, and Google Maps.ONLINE-The ArcGIS Online/Bing Maps/Google Maps
          tiling scheme will be
          used. This tiling scheme allows you to overlay cache tiles with tiles
          from these online mapping services. ArcGIS Pro includes this tiling
          scheme as a built-in option when loading a tiling scheme. When you
          choose this option, the data frame of the source map must use the WGS
          1984 Web Mercator (Auxiliary Sphere) projected coordinate system. This
          is the default.EXISTING-A tiling scheme from an existing vector tile
          service will be
          used. Only tiling schemes with scales that double in progression
          through levels and have 512-by-512 tile size are supported. You must
          specify a vector tile service or tiling scheme file in the
          tiling_scheme parameter.
      tiling_scheme {Map Server / File}:
          A vector tile service or tiling scheme file that will be used if the
          service_type parameter is set to EXISTING. The tiling scheme tile size
          must be 512 by 512 and must have consecutive scales in a ratio of two.
      tile_structure {String}:
          Specifies whether the tile generation structure will be optimized with
          an indexed structure or as a flat array of all tiles at all levels of
          detail. The optimized indexed structure is the default and results in
          a smaller cache.INDEXED-Tiles that are based on an index of feature
          density that
          optimizes the tile generation and file sizes will be produced. This is
          the default.FLAT-Regular tiles for each level of detail will be
          produced without
          regard to feature density. This cache is larger than that produced
          with an indexed structure.
      min_cached_scale (Double):
          The minimum (smallest) scale at which tiles will be generated. This
          does not need to be the smallest scale in the tiling scheme. The
          minimum cached scale determines which scales will be used to generate
          cache.
      max_cached_scale (Double):
          The maximum (largest) scale at which tiles will be generated. This
          does not need to be the largest scale in the tiling scheme. The
          maximum cached scale determines which scales will be used to generate
          cache.
      index_polygons {Feature Layer}:
          A pregenerated index of tiles based on feature density, applicable
          only when the tile_structure parameter is set to INDEXED. Use the
          Create Vector Tile Index tool to create index polygons. If no index
          polygons are specified for this parameter, optimized index polygons
          will be generated during processing to aid in tile creation, but they
          will not be saved or output. The index polygons must use the same
          coordinate system as the tiling_scheme parameter value.
      summary {String}:
          The summary information that will be added to properties of the output
          vector tile package.
      tags {String}:
          The tag information that will be added to the properties of the output
          vector tile package. Separate multiple tags with commas or semicolons.

     OUTPUTS:
      output_file (File):
          The output vector tile package. The file extension of the package is
          .vtpk.

        """