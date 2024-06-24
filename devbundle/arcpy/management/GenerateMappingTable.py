# Generated documentation for module arcpy.management


class GenerateMappingTable(object):
    """
    Generates the Mapping Table based on a configured data loading workspace. The table includes a list of predefined datasets, fields, and attribute domain coded value descriptions. This output table is used as input to the Create Data Loading Workspace tool.
    """

    @property
    def description(self) -> str:
        return """

        GenerateMappingTable_management(in_workbook, out_table)

        Generates the Mapping Table based on a configured data loading
        workspace. The table includes a list of predefined datasets, fields,
        and attribute domain coded value descriptions. This output table is
        used as input to the Create Data Loading Workspace tool.

     INPUTS:
      in_workbook (File):
          The Data Reference Workbook that will be used to generate a Mapping
          Table.

     OUTPUTS:
      out_table (Table):
          The output table, which will include a list of datasets, fields, and
          attribute domain coded value descriptions based on the source and
          target mapping from a Data Loading Workspace. Use this table in the
          Create Data Loading Workspace tool to refine a future iteration of a
          Data Loading Workspace.

        """