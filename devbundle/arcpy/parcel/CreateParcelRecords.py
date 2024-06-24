# Generated documentation for module arcpy.parcel


class CreateParcelRecords(object):
    """
    Creates parcel records for the input parcel fabric features using a record name field or an expression.
    """

    @property
    def description(self) -> str:
        return """

        CreateParcelRecords_parcel(in_parcel_features, {record_field}, {record_expression}, {record_name_method})

        Creates parcel records for the input parcel fabric features using a
        record name field or an expression.

     INPUTS:
      in_parcel_features (Feature Layer):
          The input parcel features (parcel polygons, parcel lines, or
          connection lines) that will be used to create parcel records. The
          input parcel features can be from a parcel fabric in a file,
          enterprise, or mobile geodatabase.
      record_field {Field}:
          The attribute field that contains the record names. The attribute
          field must be a text field and must contain parcel record names.
          Parcel records will be created for features using the provided record
          names.
      record_expression {Calculator Expression}:
          An Arcade expression that uses fields, string operators, and
          mathematical operators to represent the record names. For example, the
          expression Left($feature.Name,4) extracts the first four characters
          from the parcel name field in the parcel fabric polygon feature class
          to create the record names.
      record_name_method {String}:
          Specifies the method that will be used to create parcel
          records.FIELD-Parcel records will be created using record names from a
          text
          field on the input parcel features. This is the
          default.EXPRESSION-Parcel records will be created using an Arcade
          expression.

        """