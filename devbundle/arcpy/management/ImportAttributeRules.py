# Generated documentation for module arcpy.management


class ImportAttributeRules(object):
    """
    Imports attribute rules from a comma-separated values (.csv) file to a dataset.
    """

    @property
    def description(self) -> str:
        return """

        ImportAttributeRules_management(target_table, csv_file)

        Imports attribute rules from a comma-separated values (.csv) file to a
        dataset.

     INPUTS:
      target_table (Table View):
          The table or feature class to which the attribute rules will be
          applied. The dataset must have all the features specified in the rule
          definition.
      csv_file (File):
          The .csv file containing the rules to import.

        """