# Generated documentation for module arcpy.management


class SetSubtypeField(object):
    """
    Defines the field in the input table or feature class that stores the subtype codes.
    """

    @property
    def description(self) -> str:
        return """

        SetSubtypeField_management(in_table, {field}, {clear_value})

        Defines the field in the input table or feature class that stores the
        subtype codes.

     INPUTS:
      in_table (Table View):
          The input table or feature class that contains the field to set as a
          subtype field.
      field {Field}:
          The integer field that will store the subtype codes.
      clear_value {Boolean}:
          Specifies whether to clear the subtype field.CLEAR_SUBTYPE_FIELD-The
          subtype field will be cleared (set to
          null).DO_NOT_CLEAR-The subtype field will not be cleared. This is the
          default.

        """