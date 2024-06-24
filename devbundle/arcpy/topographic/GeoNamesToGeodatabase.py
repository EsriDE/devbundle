# Generated documentation for module arcpy.topographic


class GeoNamesToGeodatabase(object):
    """
    Loads GeoNames data into a feature class and table. The feature class is composed of point features, and the table contains fields with information concerning the naming conventions used for the features. The feature class contains the Unique Feature Identifier (UFI) and Unique Name Identifier (UNI) fields, which match the same fields in the GeoNames table.
    """

    @property
    def description(self) -> str:
        return """

        GeoNamesToGeodatabase_topographic(in_source, in_feature_class, in_allow_duplicates, in_table, {match_fields;match_fields...})

        Loads GeoNames data into a feature class and table. The feature class
        is composed of point features, and the table contains fields with
        information concerning the naming conventions used for the features.
        The feature class contains the Unique Feature Identifier (UFI) and
        Unique Name Identifier (UNI) fields, which match the same fields in
        the GeoNames table.

     INPUTS:
      in_source (Text File / Shapefile):
          The path to the source file containing the GeoNames information. This
          must be a properly formatted GeoNames file.
      in_feature_class (Feature Class):
          The GeoNames feature class. This feature class is in the working
          database.
      in_allow_duplicates (Boolean):
          Specifies whether duplicate features will be imported to the GeoNames
          feature class.ALLOW_DUPLICATES-Features with the same geometry and
          attributes will
          be imported.DON'T_ALLOW_DUPLICATES-Features with the same geometry and
          attributes
          will not be imported. This is the default.
      in_table (Table):
          The GeoNames table. This table is in the working database.
      match_fields {Value Table}:
          Specific fields in the GeoNames source file that will be mapped to
          fields in the GeoNames feature class and table.

        """