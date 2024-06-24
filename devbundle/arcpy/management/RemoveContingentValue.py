# Generated documentation for module arcpy.management


class RemoveContingentValue(object):
    """
    Removes a contingent value from a field group.
    """

    @property
    def description(self) -> str:
        return """

        RemoveContingentValue_management(target_table, id)

        Removes a contingent value from a field group.

     INPUTS:
      target_table (Table View):
          The input geodatabase feature class or table containing the contingent
          value that will be removed.
      id (String):
          The unique contingent value ID. To view the contingent value ID
          in theview, click thebutton on
          the ribbon. In Python, this value can be accessed using the
          arcpy.da.ListContingentValues function. Contingent ValuesToggle
          Value IDs

        """