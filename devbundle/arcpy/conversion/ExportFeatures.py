# Generated documentation for module arcpy.conversion


class ExportFeatures(object):
    """
    Converts a feature class or feature layer to a new feature class.
    """

    @property
    def description(self) -> str:
        return """

        ExportFeatures_conversion(in_features, out_features, {where_clause}, {use_field_alias_as_name}, {field_mapping}, {sort_field;sort_field...})

        Converts a feature class or feature layer to a new feature class.

     INPUTS:
      in_features (Feature Layer):
          The input features that will be exported to a new feature class.
      where_clause {SQL Expression}:
          An SQL expression used to select a subset of features. For more
          information on SQL syntax see the help topic SQL reference for query
          expressions used in ArcGIS.
      use_field_alias_as_name {Boolean}:
          Specifies whether the input's field names or field aliases will be
          used as the output field name.NOT_USE_ALIAS-The input's field names
          will be used as the output field
          names. This is the default.USE_ALIAS-The input's field aliases will be
          used as the output field
          names.
      field_mapping {Field Mappings}:
          The fields that will be transferred to the output dataset with their
          respective properties and source fields. By default, the output
          includes all fields from the input dataset.Use the field map to add,
          delete, rename, and reorder fields, as well
          as change other field properties.The field map can also be used to
          combine values from two or more
          input fields into a single output field.
      sort_field {Value Table}:
          The field or fields whose values will be used to reorder the input
          records and the direction the records will be sorted.ASCENDING-Records
          will be sorted from low value to high
          value.DESCENDING-Records will be sorted from high value to low value.

     OUTPUTS:
      out_features (Feature Class):
          The output feature class containing the exported features.

        """