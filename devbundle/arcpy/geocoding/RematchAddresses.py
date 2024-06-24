# Generated documentation for module arcpy.geocoding


class RematchAddresses(object):
    """
    Rematches addresses in a geocoded feature class.
    """

    @property
    def description(self) -> str:
        return """

        RematchAddresses_geocoding(in_geocoded_feature_class, {in_where_clause})

        Rematches addresses in a geocoded feature class.

     INPUTS:
      in_geocoded_feature_class (Feature Class):
          The geocoded feature class to be rematched.
      in_where_clause {SQL Expression}:
          An SQL expression used to select a subset of features. For more
          information on SQL syntax see the help topic SQL reference for query
          expressions used in ArcGIS.

        """