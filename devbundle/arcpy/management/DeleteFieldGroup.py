# Generated documentation for module arcpy.management


class DeleteFieldGroup(object):
    """
    Deletes a field group from a table or feature class.
    """

    @property
    def description(self) -> str:
        return """

        DeleteFieldGroup_management(target_table, name)

        Deletes a field group from a table or feature class.

     INPUTS:
      target_table (Table View):
          The input geodatabase feature class or table that will have the field
          group deleted.
      name (String):
          The name of the field group that will be deleted.

        """