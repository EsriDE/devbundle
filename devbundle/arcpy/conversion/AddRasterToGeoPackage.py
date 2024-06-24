# Generated documentation for module arcpy.conversion


class AddRasterToGeoPackage(object):
    """
    Loads raster datasets into an OGC GeoPackage raster pyramid.
    """

    @property
    def description(self) -> str:
        return """

        AddRasterToGeoPackage_conversion(in_dataset, target_geopackage, raster_name, {tiling_scheme}, {tiling_scheme_file}, {area_of_interest})

        Loads raster datasets into an OGC GeoPackage raster pyramid.

     INPUTS:
      in_dataset (Raster Layer / Mosaic Layer):
          The raster dataset to load into the OGC GeoPackage raster pyramid.
      target_geopackage (Workspace):
          The GeoPackage into which the raster dataset will be loaded.
      raster_name (String):
          The name of the output GeoPackage raster pyramid.
      tiling_scheme {String}:
          Specifies the tiling scheme.TILED-The spatial reference of the input
          raster will be maintained and
          tiles will be generated consistent with the GeoPackage standard. This
          is the default.ARCGISONLINE_SCHEME-Raster tiles will be generated in
          a Web Mercator
          coordinate reference (the same scheme developed for the Army
          Geospatial Center).NSGPROFILE_SCALED_TRANSVERSE_MERCATOR-A scaled
          transverse Mercator
          will be used.NSGPROFILE_WGS84_GEOGRAPHIC-WGS84 Geographic will be
          used.GOOGLE_EARTH_WEB_MERCATOR-Raster tiles will be created using the
          parameters in the Web Mercator coordinate reference.FROM_FILE-A custom
          tiling scheme from a file with an XML schema
          definition created using the Generate Tile Cache Tiling Scheme tool
          will be used.
      tiling_scheme_file {File}:
          A custom tiling scheme file that is required when tiling_scheme is set
          to FROM_FILE.
      area_of_interest {Feature Set}:
          An area of interest used to limit the area of the raster to be loaded,
          rather than the entire dataset.

        """