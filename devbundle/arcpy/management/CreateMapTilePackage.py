# Generated documentation for module arcpy.management


class CreateMapTilePackage(object):
    """
    Generates tiles from a map and packages them as a single tile package or multiple smaller tile packages.
    """

    @property
    def description(self) -> str:
        return """

        CreateMapTilePackage_management(in_map, service_type, {output_file}, format_type, level_of_detail, {service_file}, {summary}, {tags}, {extent}, {compression_quality}, {package_type}, {min_level_of_detail}, {area_of_interest}, {create_multiple_packages}, {output_folder})

        Generates tiles from a map and packages them as a single tile package
        or multiple smaller tile packages.

     INPUTS:
      in_map (Map):
          The map from which tiles will be generated and packaged.
      service_type (Boolean):
          Specifies whether the tiling scheme will be generated from an existing
          map service or whether map tiles will be generated for ArcGIS Online,
          Bing Maps, and Google Maps. EXISTING-A tiling scheme from an
          existing map service will be
          used. You must specify a map service in the service_file parameter.
          Choose this option if your organization has created a tiling scheme
          for an existing service on the server and you want to match it.
          Matching tiling schemes ensures that the tiles will overlay correctly
          in your Maps SDKs application.If you choose this option, use the same
          coordinate system for the
          source map as the map with the tiling scheme you're importing.
          ONLINE-The ArcGIS Online/Bing Maps/Google Maps tiling scheme
          will be used. This is the default. The ArcGIS Online/Bing
          Maps/Google Maps tiling scheme allows you to
          overlay cache tiles with tiles from these online mapping services.
          ArcGIS Desktop includes this tiling scheme as a built-in option when
          loading a tiling scheme. When you choose this tiling scheme, the
          source map must use the WGS84 Web Mercator (Auxiliary Sphere)
          projected coordinate system.The ArcGIS Online/Bing Maps/Google Maps
          tiling scheme is required if
          you'll be overlaying the package with ArcGIS Online, Bing Maps, or
          Google Maps. One advantage of the ArcGIS Online/Bing Maps/Google Maps
          tiling scheme is that it is widely known in the web mapping world, so
          the tiles will match those of other organizations that have used this
          tiling scheme. Even if you don't plan to overlay any of these well-
          known map services, you may choose the tiling scheme for its
          interoperability potential.The ArcGIS Online/Bing Maps/Google Maps
          tiling scheme may contain
          scales that will be zoomed in too far to be of use in your map.
          Packaging for large scales can take up time and disk storage space.
          For example, the largest scale in the tiling scheme is about 1:1,000.
          Packaging the entire continental United States at this scale can take
          weeks and require hundreds of gigabytes of storage. If you aren't
          prepared to package at this scale level, remove this scale level when
          you create the tile package.
      format_type (String):
          Specifies the format that will be used for the generated tiles.
          PNG-The correct format (PNG 8, PNG 24, or PNG 32) will be
          used based on the specifiedparameter value. This is the default.
          Maximum Level Of Detail         PNG8-PNG8 format will be used. Use
          this format for overlay
          services that need to have a transparent background, such as roads and
          boundaries. PNG8 creates tiles of very small size on disk with no loss
          of information. Do not use PNG8 if the map contains more than
          256 colors. Imagery,
          hillshades, gradient fills, transparency, and antialiasing can use
          more than 256 colors in a map. Even symbols such as highway shields
          may have subtle antialiasing around the edges that unexpectedly adds
          colors to a map.PNG24-PNG24 format will be used. Use this format for
          overlay services,
          such as roads and boundaries, that have more than 256 colors (if fewer
          than 256 colors, use PNG8).PNG32-PNG32 format will be used. Use this
          format for overlay services,
          such as roads and boundaries, that have more than 256 colors. PNG32
          works well for overlay services that have antialiasing enabled on
          lines or text. PNG32 creates larger tiles on disk than PNG24.
          JPEG-JPEG format will be used. Use this format for basemap
          services that have large color variation and do not need a transparent
          background. For example, raster imagery and detailed vector basemaps
          work well with JPEG. JPEG is a lossy image format. It attempts
          to selectively remove data
          without affecting the appearance of the image. This can cause very
          small tile sizes on disk, but if a map contains vector line work or
          labels, it may produce too much noise or blurry areas around the
          lines. If this is the case, you can raise the compression value from
          the default of 75. A higher value, such as 90, may balance an
          acceptable quality of line work with the small tile size benefit of
          the JPEG.If you are willing to accept a minor amount of noise in the
          images,
          you may save large amounts of disk space with JPEG. The smaller tile
          size also means the application can download the tiles faster.
          MIXED-JPEG format will be used in the center of the package
          and PNG32 will be used on the edge of the package. Use mixed mode when
          you want to cleanly overlay raster packages on other layers.
          When a mixed package is created, PNG32 tiles are created where
          transparency is detected (in other words, where the map background is
          visible). The rest of the tiles are built using JPEG. This keeps the
          average file size down while providing a clean overlay on top of other
          packages. If you do not use the mixed mode package in this scenario, a
          nontransparent collar around the periphery of the image where it
          overlaps the other package will be visible.
      level_of_detail (Long):
          The integer representation corresponding to the number of scales used
          to define a cache tiling scheme. This scale value defines the maximum
          level up to which the cache tiles will be generated in the tile
          package. Larger values reflect larger scales that show more detail but
          require more storage space. Smaller values reflect smaller scales that
          show less detail and require less storage space. Possible values are
          from 1 to 23. The default value is 1. The maximum level of detail
          value must be greater than the minimum level of detail value.
      service_file {Map Server / File}:
          The name of the map service or the .xml files that will be used for
          the tiling scheme. This parameter is required only when the
          service_type parameter is set to EXISTING.
      summary {String}:
          The summary information that will be added to the properties of the
          package.
      tags {String}:
          The tag information that will be added to the properties of the
          package. Multiple tags can be added, separated by a comma or
          semicolon.
      extent {Extent}:
          Specifies the extent that will be used to select or clip
          features.MAXOF-The maximum extent of all inputs will be used.MINOF-The
          minimum
          area common to all inputs will be used.DISPLAY-The extent is equal to
          the visible display.Layer name-The extent of the specified layer will
          be used.Extent object-The extent of the specified object will be
          used.Space delimited string of coordinates-The extent of the specified
          string will be used. Coordinates are expressed in the order of x-min,
          y-min, x-max, y-max.
      compression_quality {Long}:
          A value between 1 and 100 for the JPEG compression quality. The
          default value is 75 for JPEG tile format and zero for other
          formats.Compression is supported only for JPEG and mixed formats.
          Choosing a
          higher value will result in a larger file size with a higher-quality
          image. Choosing a lower value will result in a smaller file size with
          a lower-quality image.
      package_type {String}:
          Specifies the type of tile package that will be created.tpk-A .tpk
          file will be created. Tiles will be stored using Compact
          storage format. This format is supported across ArcGIS.tpkx-A .tpkx
          file will be created. Tiles will be stored using
          CompactV2 storage format, which provides better performance on network
          shares and cloud store directories. This package structure type is
          supported by newer versions of ArcGIS products such as ArcGIS Online
          7.1, ArcGIS Enterprise 10.7, and ArcGIS Runtime 100.5. This is the
          default.
      min_level_of_detail {Long}:
          The integer representation corresponding to the number of scales used
          to define a cache tiling scheme. This scale value defines the level at
          which the cache tiles begin to be available and generated in the tile
          package. Possible values are from 0 to 23. The default value is 0. The
          minimum level of detail value must be less than or equal to the
          maximum level of detail value.
      area_of_interest {Feature Set}:
          A feature set that constrains where tiles will be created. Use an area
          of interest to create tiles for irregularly shaped areas or multipart
          features. The areas outside the bounding box of area of interest
          features will not be cached. If no value is provided for this
          parameter, the area of interest will be the full extent of the input
          map.
      create_multiple_packages {Boolean}:
          Specifies whether a single large tile package or multiple small tile
          packages will be generated. This parameter is not available when the
          parallelProcessingFactor environment variable is 0 or when the
          package_type parameter is set to tpk.CREATE_MULTIPLE_PACKAGES-Multiple
          tile packages (each approximately 1
          GB in size) will be generated in the location defined in the
          output_folder parameter.CREATE_SINGLE_PACKAGE-A single tile package
          will be generated in the
          location defined in the output_file parameter. This is the default.
      output_folder {Folder}:
          The output folder where the multiple tile packages will be generated.
          If the output folder is not empty, a subfolder will be with created in
          the output folder to store the tiles. An automatically generated GUID
          will be used as the folder name.

     OUTPUTS:
      output_file {File}:
          The output path and file name for the map tile package.

        """