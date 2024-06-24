# Generated documentation for module arcpy.management


class ExportAttributeRules(object):
    """
    Exports attribute rules from a dataset to a comma-separated values (.csv) file.
    """

    @property
    def description(self) -> str:
        return """

        ExportAttributeRules_management(in_table, out_csv_file)

        Exports attribute rules from a dataset to a comma-separated values
        (.csv) file.

     INPUTS:
      in_table (Table View):
          The table or feature class from which the attribute rules will be
          exported.

     OUTPUTS:
      out_csv_file (File):
          The folder location and name of the .csv file to be created.

        """