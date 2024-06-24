# Generated documentation for module arcpy.management


class SetDefaultSubtype(object):
    """
    Sets the default value or code for the input table's subtype.
    """

    @property
    def description(self) -> str:
        return """

        SetDefaultSubtype_management(in_table, subtype_code)

        Sets the default value or code for the input table's subtype.

     INPUTS:
      in_table (Table View):
          The input table or feature class whose subtype default value will be
          set.
      subtype_code (Long):
          The unique default value for a subtype.

        """