# Generated documentation for module arcpy.management


class RemoveFieldConflictFilter(object):
    """
    Removes a field conflict filter for a given field in a geodatabase table or feature class.
    """

    @property
    def description(self) -> str:
        return """

        RemoveFieldConflictFilter_management(table, fields;fields...)

        Removes a field conflict filter for a given field in a geodatabase
        table or feature class.

     INPUTS:
      table (Table View):
          Table or feature class containing the field or fields to be removed as
          conflict filters.
      fields (Field):
          Field or list of fields to be removed as conflict filters.

        """