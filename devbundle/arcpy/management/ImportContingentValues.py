# Generated documentation for module arcpy.management


class ImportContingentValues(object):
    """
    Imports multiple contingent values and field groups from a comma- separated values file (.csv) to a dataset.
    """

    @property
    def description(self) -> str:
        return """

        ImportContingentValues_management(target_table, field_group_file, contingent_value_file, {import_type})

        Imports multiple contingent values and field groups from a comma-
        separated values file (.csv) to a dataset.

     INPUTS:
      target_table (Table View):
          The input geodatabase table or feature class to which the field groups
          and contingent values will be imported.
      field_group_file (File):
          A .csv file with specific column names that contains information about
          the field groups.
      contingent_value_file (File):
          A .csv file with specific column names that contains information about
          the contingent values.
      import_type {Boolean}:
          Specifies whether existing values will be replaced or merged when
          imported.REPLACE-Existing values for the target table will be replaced
          with the
          values in the input .csv files.UNION-Existing values will be merged
          with the values in the input .csv
          files. Any duplicates will be excluded. This is the default.

        """