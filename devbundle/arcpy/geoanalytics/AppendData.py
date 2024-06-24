# Generated documentation for module arcpy.geoanalytics


class AppendData(object):
    """
    Appends features to an existing hosted feature layer.
    """

    @property
    def description(self) -> str:
        return """

        AppendData_geoanalytics(input_layer, append_layer, append_method, {append_fields;append_fields...}, {append_expressions;append_expressions...})

        Appends features to an existing hosted feature layer.

     INPUTS:
      input_layer (Record Set):
          The hosted feature layer to which features will be appended.
      append_layer (Record Set):
          The layer containing features to append to the input layer.
      append_method (String):
          Specifies how fields from thewill be appended with values from
          the. Input LayerAppend LayerMATCHING_ONLY-Input layer fields
          will only be appended if they have a
          matching field in the append layer. Fields without a match will be
          appended with null values.FIELD_MAPPING-Input layer fields can be
          appended with append layer
          fields of the same name and different type, or with values calculated
          from Arcade expressions.
      append_fields {Value Table}:
          The append layer fields of the same type and different name as
          the input layer fields to be appended. Select theyou want to append
          to, and thecontaining the values you want to append. Input
          FieldAppend Field
      append_expressions {Value Table}:
          The Arcade expression used to calculate field values for the input
          field. Expressions are written in Arcade and can include mathematical
          operators and multiple fields.

        """