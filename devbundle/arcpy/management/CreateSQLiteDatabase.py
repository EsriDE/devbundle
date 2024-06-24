# Generated documentation for module arcpy.management


class CreateSQLiteDatabase(object):
    """
    Creates a GeoPackage or an SQLite database that contains the ST_Geometry or SpatiaLite spatial type.
    """

    @property
    def description(self) -> str:
        return """

        CreateSQLiteDatabase_management(out_database_name, {spatial_type})

        Creates a GeoPackage or an SQLite database that contains the
        ST_Geometry or SpatiaLite spatial type.

     INPUTS:
      spatial_type {String}:
          Specifies the spatial type that will be installed with the new SQLite
          database or the GeoPackage version that will be
          created.ST_GEOMETRY-The Esri spatial storage type will be installed.
          This is
          the default.SPATIALITE-SpatiaLite spatial storage type will be
          installed.GEOPACKAGE-The latest version of OGC GeoPackage that is
          supported by
          ArcGIS will be created.GEOPACKAGE_1.0-An OGC GeoPackage 1.0 dataset
          will be created.GEOPACKAGE_1.1-An OGC GeoPackage 1.1 dataset will be
          created.GEOPACKAGE_1.2-An OGC GeoPackage 1.2.1 dataset will be
          created.GEOPACKAGE_1.3-An OGC GeoPackage 1.3 dataset will be
          created.GEOPACKAGE_1.4-An OGC GeoPackage 1.4 dataset will be created.

     OUTPUTS:
      out_database_name (File):
          The location of the SQLite database or GeoPackage that will be created
          and the name of the file. The .sqlite extension will be automatically
          assigned if the spatial_type parameter value is ST_GEOMETRY or
          SPATIALITE. If the spatial_type parameter value is GEOPACKAGE, the
          .gpkg extension will be automatically assigned.

        """