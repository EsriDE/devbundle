# Generated documentation for module arcpy.management


class ExportContingentValues(object):
    """
    Exports field groups and contingent values to a .csv file.
    """

    @property
    def description(self) -> str:
        return """

        ExportContingentValues_management(target_table, field_groups_file, contingent_values_file)

        Exports field groups and contingent values to a .csv file.

     INPUTS:
      target_table (Table View):
          The input geodatabase table or feature class from which the field
          groups and contingent values will be exported.

     OUTPUTS:
      field_groups_file (File):
          The location and name of the output .csv file that will be created
          with specific column names containing information about the field
          groups of the target table.
      contingent_values_file (File):
          The location and name of the output .csv file that will be created
          with specific column names containing information about the contingent
          values of the target table.

        """