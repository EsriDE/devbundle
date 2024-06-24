# Generated documentation for module arcpy.management


class GenerateTileCacheTilingScheme(object):
    """
    Creates a tiling scheme file based on the information from the source dataset. The tiling scheme file will then be used in the Manage Tile Cache tool when creating cache tiles.
    """

    @property
    def description(self) -> str:
        return """

        GenerateTileCacheTilingScheme_management(in_dataset, out_tiling_scheme, tiling_scheme_generation_method, number_of_scales, {predefined_tiling_scheme}, {scales;scales...}, {scales_type}, {tile_origin}, {dpi}, {tile_size}, {tile_format}, {tile_compression_quality}, {storage_format}, {lerc_error})

        Creates a tiling scheme file based on the information from the source
        dataset. The tiling scheme file will then be used in the Manage Tile
        Cache tool when creating cache tiles.

     INPUTS:
      in_dataset (Raster Layer / Mosaic Layer / Map):
          The source to be used to generate the tiling scheme. It can be a
          raster dataset, a mosaic dataset, or a map.
      tiling_scheme_generation_method (String):
          Choose to use a new or predefined tiling scheme. You can define a new
          tiling scheme with this tool or browse to a predefined tiling scheme
          file (.xml).NEW-Define a new tiling scheme using other parameters in
          this tool to
          define scale levels, image format, storage format, and so on. This is
          the default.PREDEFINED-Use a tiling scheme .xml file that already
          exists on disk.
      number_of_scales (Long):
          The number of scale levels to be created in the tiling scheme.
      predefined_tiling_scheme {File}:
          Path to a predefined tiling scheme file (usually named
          conf.xml). This parameter is enabled only when theoption is chosen as
          the tiling scheme generation method. Predefined
      scales {Value Table}:
          Scale levels to be included in the tiling scheme. By default,
          these are not represented as fractions. Instead, use 500 to represent
          a scale of 1:500, and so on. The value entered in theparameter
          generates a set of default scale levels. Number of Scales
      scales_type {Boolean}:
          Determines the units of the scales parameter.CELL_SIZE-Indicates the
          values of the scales parameter are pixel
          sizes. This is the default.SCALE-Indicates the values of the scales
          parameter are scale levels.
      tile_origin {Point}:
          The origin (upper left corner) of the tiling scheme in the coordinates
          of the spatial reference of the source dataset. The extent of the
          source dataset must be within (but does not need to coincide) this
          region.
      dpi {Long}:
          The dots per inch of the intended output device. If a DPI is chosen
          that does not match the resolution of the output device, typically a
          display monitor, the scale of the tile will appear incorrect. The
          default value is 96.
      tile_size {String}:
          The width and height of the cache tiles in pixels. The default is 256
          by 256.For the best balance between performance and manageability,
          avoid
          deviating from widths of 256 or 512.128 x 128-Tile width and height
          of 128 pixels.256 x 256-Tile width
          and height of 256 pixels.512 x 512-Tile width and height of 512
          pixels.1024 x 1024-Tile width and height of 1024 pixels.
      tile_format {String}:
          The file format for the tiles in the cache.PNG-Creates PNG format with
          varying bit depths. The bit depths are
          optimized according to the color variation and transparency values in
          each tile.PNG8-A lossless, 8-bit color, image format that uses an
          indexed color
          palette and an alpha table. Each pixel stores a value (0 to 255) that
          is used to look up the color in the color palette and the transparency
          in the alpha table. 8-bit PNGs are similar to GIF images and provide
          the best support for a transparent background by most web
          browsers.PNG24-A lossless, three-channel image format that supports
          large color
          variations (16 million colors) and has limited support for
          transparency. Each pixel contains three 8-bit color channels, and the
          file header contains the single color that represents the transparent
          background. The color representing the transparent background color
          can be set in the application. Versions of Internet Explorer prior to
          version 7 do not support this type of transparency. Caches using PNG24
          are significantly larger than those using PNG8 or JPEG, so will take
          more disk space and require greater bandwidth to serve clients.PNG32-A
          lossless, four-channel image format that supports large color
          variations (16 million colors) and transparency. Each pixel contains
          three 8-bit color channels and one 8-bit alpha channel that represents
          the level of transparency for each pixel. While the PNG32 format
          allows for partially transparent pixels in the range from 0 to 255,
          the ArcGIS Server cache generation tool only writes fully transparent
          (0) or fully opaque (255) values in the transparency channel. Caches
          using PNG32 are significantly larger than the other supported formats,
          so will take more disk space and require greater bandwidth to serve
          clients.JPEG-A lossy, three-channel image format that supports large
          color
          variations (16 million colors) but does not support transparency. Each
          pixel contains three 8-bit color channels. Caches using JPEG provide
          control over output quality and size.MIXED-Creates PNG32 anywhere that
          transparency is detected (in other
          words, anyplace where the data frame background is visible), but
          creates JPEG for the remaining tiles. This keeps the average file size
          down while providing you with a clean overlay on top of other caches.
          This is the default.LERC-Limited Error Raster Compression (LERC) is an
          efficient lossy
          compression method recommended for single-band or elevation data with
          a large pixel depth (12 bit to 32 bit). Compresses between 10:1 and
          20:1.
      tile_compression_quality {Long}:
          Enter a value between 1 and 100 for theorcompression quality.
          The default value is 75. JPEGMixed        Compression is
          supported only forandformat. Choosing a higher
          value will result in higher-quality images, but the file sizes will be
          larger. Using a lower value will result in lower-quality images with
          smaller file sizes. MixedJPEG
      storage_format {String}:
          Determines the storage format of tiles.COMPACT-Group tiles into large
          files called bundles. This storage
          format is more efficient in terms of storage and mobility. This is the
          default. EXPLODED-Each tile is stored as an individual file.
          Note that this format cannot be used with tile packages.
      lerc_error {Double}:
          Set the maximum tolerance in pixel values when compressing
          with. LERC

     OUTPUTS:
      out_tiling_scheme (File):
          The path and file name for the output tiling scheme to be created.

        """