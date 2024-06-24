# Generated documentation for module arcpy.cartography


class MapServerCacheTilingSchemeToPolygons(object):
    """
    Creates a polygon feature class from an existing tiling scheme.
    """

    @property
    def description(self) -> str:
        return """

        MapServerCacheTilingSchemeToPolygons_cartography(input_map, tiling_scheme, output_feature_class, use_map_extent, clip_to_horizon, {antialiasing}, {levels;levels...})

        Creates a polygon feature class from an existing tiling scheme.

     INPUTS:
      input_map (Map):
          The current map with the extent that will be used.
      tiling_scheme (File):
          A predefined tiling scheme .xml file.
      use_map_extent (Boolean):
          Specifies whether polygon features will be created for the entire
          extent of the tiling scheme or only those tiles that intersect the
          full extent of the map.USE_MAP_EXTENT-Polygon features will be created
          for the full extent of
          the map. This is the default.FULL_TILING_SCHEME-Polygon features will
          be created for the full
          extent of the tiling scheme.
      clip_to_horizon (Boolean):
          Specifies whether polygons will be constrained to the valid area of
          use for the geographic or projected coordinate system of the
          map.CLIP_TO_HORIZON-Polygon features will only be created within the
          valid
          area of use for the geographic or projected coordinate system of the
          map. Tiles that are within the extent of the tiling scheme but outside
          the extent of the coordinate system horizon will be clipped. This is
          the default.UNIFORM_TILE_SIZE-Polygon features will be created for the
          full extent
          of the tiling scheme. Within each scale level, polygons will be of a
          uniform size and will not be clipped at the coordinate system horizon.
          This may create data that is outside the valid area of use for the
          geographic or projected coordinate system. If a scale within the
          tiling scheme would generate a tile that is larger than the spatial
          domain of the feature class, null geometry will be created for that
          feature.
      antialiasing {Boolean}:
          Specifies whether polygons that match map service caches with
          antialiasing enabled will be generated. A map service cache supertile
          is 2048 x 2048 pixels with antialiasing or 4096 x 4096 pixels without.
          To determine whether antialiasing was used in an existing cache, open
          the tiling scheme file (conf.xml) and see if the <Antialiasing> tag is
          set to true.ANTIALIASING-Polygon tiles will be generated to match the
          supertile
          extent of a map service cache with antialiasing enabled.NONE-Polygon
          tiles will be generated to match the supertile extent of
          a map service cache without antialiasing enabled. This is the default.
      levels {Double}:
          The scale levels at which polygons will be created. To create polygons
          for all scale levels included in a tiling scheme, leave this parameter
          blank. You can create polygons for some or all of the scale levels
          that are included in the tiling scheme. To add more scale levels,
          however, you must modify the tiling scheme file or create a new one.

     OUTPUTS:
      output_feature_class (Feature Class):
          The output polygon feature class.

        """