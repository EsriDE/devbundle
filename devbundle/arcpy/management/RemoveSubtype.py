# Generated documentation for module arcpy.management


class RemoveSubtype(object):
    """
    Removes a subtype from the input table using its code.
    """

    @property
    def description(self) -> str:
        return """

        RemoveSubtype_management(in_table, subtype_code;subtype_code...)

        Removes a subtype from the input table using its code.

     INPUTS:
      in_table (Table View):
          The feature class or table containing the subtype definition.
      subtype_code (String):
          The subtype code to remove a subtype from the input table or feature
          class.

        """