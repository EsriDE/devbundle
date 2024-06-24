# Generated documentation for module arcpy.server


class GenerateMapServerCacheTilingScheme(object):
    """
    Generates a custom tiling scheme file that defines the scale levels, tile dimensions, and other properties for a web tile layer.
    """

    @property
    def description(self) -> str:
        return """

        GenerateMapServerCacheTilingScheme_server(in_map, tile_origin, output_tiling_scheme, num_of_scales, scales;scales..., dots_per_inch, tile_size)

        Generates a custom tiling scheme file that defines the scale levels,
        tile dimensions, and other properties for a web tile layer.

     INPUTS:
      in_map (Map):
          The current map or an existing .mxd document to be used for the tiling
          scheme.
      tile_origin (Point):
          The upper left corner of the tiling scheme, in coordinates of the
          spatial reference of the source data frame.
      num_of_scales (Long):
          Number of scale levels in the tiling scheme.
      scales (Value Table):
          Scale levels to include in the tiling scheme. These are not
          represented as fractions. Instead, use 500 to represent a scale of
          1:500, and so on.
      dots_per_inch (Long):
          The dots per inch of the intended output device. If a DPI is chosen
          that does not match the resolution of the output device, the scale of
          the map tile will appear incorrect. The default value is 96.
      tile_size (String):
          The width and height of the cache tiles in pixels. The default is 256
          by 256. For the best balance between performance and manageability,
          avoid deviating from standard dimensions of 256 by 256 or 512 by
          512.128 x 128-128 by 128 pixels256 x 256-256 by 256 pixels512 x
          512-512 by
          512 pixels1024 x 1024-1024 by 1024 pixels

     OUTPUTS:
      output_tiling_scheme (File):
          Path and file name of the tiling scheme file to create.

        """