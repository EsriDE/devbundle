# Generated documentation for module arcpy.management


class AssignDefaultToField(object):
    """
    Creates a default value for a specified field. When a new row is added to the table or feature class, the specified field will be set to this default value.
    """

    @property
    def description(self) -> str:
        return """

        AssignDefaultToField_management(in_table, field_name, {default_value}, {subtype_code;subtype_code...}, {clear_value})

        Creates a default value for a specified field. When a new row is added
        to the table or feature class, the specified field will be set to this
        default value.

     INPUTS:
      in_table (Table View / Raster Layer / Mosaic Layer):
          The input table or feature class that will have a default value added
          to one of its fields.
      field_name (Field):
          The field to which the default value will be added each time a new row
          is added to the table or feature class.
      default_value {String}:
          The default value to be added to each new table or feature class. The
          value entered must match the data type of the field.
      subtype_code {String}:
          The subtypes that can participate in the default value.
      clear_value {Boolean}:
          Specifies whether the default value for either the field or the
          subtype will be cleared. To clear the default value, the default_value
          parameter must be passed in as an empty string. To clear the default
          value for the subtype, you must also specify the subtype to be
          cleared.CLEAR_VALUE-The default value will be cleared (set to
          null).DO_NOT_CLEAR-The default value will not be cleared. This is the
          default.

        """