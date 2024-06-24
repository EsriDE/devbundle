# Generated documentation for module arcpy.management


class CheckGeometry(object):
    """
    Generates a report of geometry problems in a feature class.
    """

    @property
    def description(self) -> str:
        return """

        CheckGeometry_management(in_features;in_features..., {out_table}, {validation_method})

        Generates a report of geometry problems in a feature class.

     INPUTS:
      in_features (Feature Layer):
          The feature class or layer to be processed.A Desktop Basic license
          only allows shapefiles and feature classes
          stored in a file geodatabase, GeoPackage, or SpatiaLite database as
          valid input feature formats. A Desktop Standard or Desktop Advanced
          license also allows feature classes stored in an enterprise database
          or enterprise geodatabase to be used as valid input feature formats.
      validation_method {String}:
          Specifies the geometry validation method that will be used to identify
          geometry problems.ESRI-The Esri geometry validation method will be
          used. This is the
          default.OGC-The OGC geometry validation method will be used.

     OUTPUTS:
      out_table {Table}:
          The report (as a table) of the problems discovered.

        """