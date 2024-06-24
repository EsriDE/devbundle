# Generated documentation for module arcpy.management


class AddSubtype(object):
    """
    Adds a new subtype to the subtypes in the input table.
    """

    @property
    def description(self) -> str:
        return """

        AddSubtype_management(in_table, subtype_code, subtype_description)

        Adds a new subtype to the subtypes in the input table.

     INPUTS:
      in_table (Table View):
          The feature class or table containing the subtype definition to be
          updated.
      subtype_code (Long):
          A unique integer value for the subtype to be added.
      subtype_description (String):
          A description of the subtype code.

        """