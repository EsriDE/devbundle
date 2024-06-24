# Generated documentation for module arcpy.management


class AddFieldConflictFilter(object):
    """
    Adds a field conflict filter for a given field in a geodatabase table or feature class.
    """

    @property
    def description(self) -> str:
        return """

        AddFieldConflictFilter_management(table, fields;fields...)

        Adds a field conflict filter for a given field in a geodatabase table
        or feature class.

     INPUTS:
      table (Table View):
          Table or feature class containing the field or fields to which
          conflict filters will be applied.
      fields (Field):
          Field or list of fields that will have conflict filters applied.

        """