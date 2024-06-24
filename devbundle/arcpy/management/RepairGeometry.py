# Generated documentation for module arcpy.management


class RepairGeometry(object):
    """
    Inspects features for geometry problems and repairs them. If a problem is found, a repair will be performed, and a one-line description will identify the feature, as well as the geometry problem that was repaired.
    """

    @property
    def description(self) -> str:
        return """

        RepairGeometry_management(in_features, {delete_null}, {validation_method})

        Inspects features for geometry problems and repairs them. If a problem
        is found, a repair will be performed, and a one-line description will
        identify the feature, as well as the geometry problem that was
        repaired.

     INPUTS:
      in_features (Feature Layer):
          The feature class or layer to be processed.A Desktop Basic license
          only allows shapefiles and feature classes
          stored in a file geodatabase, GeoPackage, or SpatiaLite database as
          valid input feature formats. A Desktop Standard or Desktop Advanced
          license also allows feature classes stored in an enterprise database
          or enterprise geodatabase to be used as valid input feature formats.
      delete_null {Boolean}:
          Specifies whether features with null geometries will be
          deleted.DELETE_NULL-Features with null geometry will be deleted from
          the
          input. This is the default.KEEP_NULL-Features with null geometry will
          not be deleted from the
          input. Only KEEP_NULL is valid for inputs from an enterprise
          database, enterprise geodatabase, GeoPackage, or SpatiaLite database.
      validation_method {String}:
          Specifies the geometry validation method that will be used to identify
          geometry problems.ESRI-The Esri geometry validation method will be
          used. This is the
          default.OGC-The OGC geometry validation method will be used.

        """