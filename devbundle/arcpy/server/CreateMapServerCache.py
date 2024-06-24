# Generated documentation for module arcpy.server


class CreateMapServerCache(object):
    """
    Creates the tiling scheme and preparatory folders for a map or image service cache. After running this tool, use the Manage Map Server Cache Tiles tool to add tiles to the cache.
    """

    @property
    def description(self) -> str:
        return """

        CreateMapServerCache_server(input_service, service_cache_directory, tiling_scheme_type, scales_type, num_of_scales, dots_per_inch, tile_size, {predefined_tiling_scheme}, {tile_origin}, {scales;scales...}, {cache_tile_format}, {tile_compression_quality}, {storage_format})

        Creates the tiling scheme and preparatory folders for a map or image
        service cache. After running this tool, use the Manage Map Server
        Cache Tiles tool to add tiles to the cache.

     INPUTS:
      input_service (Image Service / Map Server):
          The map or image layer to be cached.
      service_cache_directory (String):
          The parent directory for the cache. This must be a registered ArcGIS
          Server cache directory.
      tiling_scheme_type (String):
          Specifies how the tiling scheme will be defined. You can define a new
          tiling scheme with this tool or browse to a predefined tiling scheme
          file (.xml). A predefined scheme can be created by running the
          Generate Map Server Cache Tiling Scheme tool.NEW-The tiling scheme
          will be defined using other parameters in this
          tool to define scale levels, image format, storage format, and so on.
          This is the default.PREDEFINED-The tiling scheme will be defined using
          an .xml file. You
          can create a tiling scheme file using the Generate Map Server Cache
          Tiling Scheme tool.
      scales_type (String):
          Specifies how the tiles will be scaled. STANDARD-The scales
          will be automatically generated based on
          the number specified in the(num_of_scales in Python) parameter. It
          will use levels that increase or decrease by half from 1:1,000,000 and
          will start with a level closest to the extent of the source map
          document. For example, if the source map document has an extent of
          1:121,000,000 and three scale levels are defined, the map service will
          create a cache with scale levels at 1:128,000,000; 1:64,000,000; and
          1:32,000,000. This is the default. Number of ScalesCUSTOM-The
          cache designer will determine the scales.
      num_of_scales (Long):
          The number of scale levels to create in the cache. This option is
          disabled if you create a custom list of scales.
      dots_per_inch (Long):
          The dots per inch (DPI) of the intended output device. If a DPI is
          chosen that does not match the resolution of the output device, the
          scale of the map tile will appear incorrect. The default value is 96.
      tile_size (String):
          Specifies the width and height of the cache tiles in pixels. For the
          best balance between performance and manageability, avoid deviating
          from standard widths of 256 by 256 or 512 by 512.128 x 128-128 by 128
          pixels.256 x 256-256 by 256 pixels. This is the
          default.512 x 512-512 by 512 pixels.1024 x 1024-1024 by 1024 pixels.
      predefined_tiling_scheme {File}:
          The path to a predefined tiling scheme file (usually named conf.xml).
      tile_origin {Point}:
          The origin (upper left corner) of the tiling scheme in the coordinates
          of the spatial reference of the source map document. The extent of the
          source map document must be within (but does not need to coincide
          with) this region.
      scales {Value Table}:
          The scale levels available for the cache. These are not represented as
          fractions. Instead, use 500 to represent a scale of 1:500, for
          example.
      cache_tile_format {String}:
          Specifies the cache tile format.PNG-A PNG format with varying bit
          depths. The bit depths are optimized
          according to the color variation and transparency values in a tile.
          This is the default.PNG8-A lossless, 8-bit color, image format that
          uses an indexed color
          palette and an alpha table. Each pixel stores a value (0-255) that is
          used to look up the color in the color palette and the transparency in
          the alpha table. 8-bit PNG images are similar to GIF images, and most
          web browsers support transparent backgrounds in PNG images.PNG24-A
          lossless, three-channel image format that supports large color
          variations (16 million colors) and has limited support for
          transparency. Each pixel contains three 8-bit color channels, and the
          file header contains the single color that represents the transparent
          background. Versions of Internet Explorer earlier than version 7 do
          not support this type of transparency. Caches using PNG24 are
          significantly larger than those using PNG8 or JPEG and will use more
          disk space and require greater bandwidth to serve clients.PNG32-A
          lossless, four-channel image format that supports large color
          variations (16 million colors) and transparency. Each pixel contains
          three 8-bit color channels and one 8-bit alpha channel that represents
          the level of transparency for each pixel. While the PNG32 format
          allows for partially transparent pixels in the range from 0 to 255,
          the ArcGIS Server cache generation tool only writes fully transparent
          (0) or fully opaque (255) values in the transparency channel. Caches
          using PNG32 are significantly larger than the other supported formats
          and will use more disk space and require greater bandwidth to serve
          clients.JPEG-A lossy, three-channel image format that supports large
          color
          variations (16 million colors) but does not support transparency. Each
          pixel contains three 8-bit color channels. Caches using JPEG provide
          control over output quality and size.MIXED-The PNG32 format will be
          created anywhere that transparency is
          detected (that is, anywhere that the data frame background is
          visible). The JPEG format will be created for the remaining tiles.
          This keeps the average file size down while providing a clean overlay
          on top of other caches.
      tile_compression_quality {Long}:
          The JPEG compression quality (1-100). The default value is 75 for the
          JPEG tile format and 0 for other formats.Compression is supported only
          for the JPEG format. Choosing a higher
          value will result in a larger file size with a higher-quality image.
          Choosing a lower value will result in a smaller file size with a
          lower-quality image.
      storage_format {String}:
          Specifies the storage format of tiles.COMPACT-Tiles will be grouped
          into large files called bundles. This
          storage format is efficient in terms of storage and mobility. This is
          the default.EXPLODED-Each tile will be stored as a separate file.

        """