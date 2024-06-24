# Generated documentation for module arcpy.management


class DomainToTable(object):
    """
    Creates a table from an attribute domain.
    """

    @property
    def description(self) -> str:
        return """

        DomainToTable_management(in_workspace, domain_name, out_table, code_field, description_field, {configuration_keyword})

        Creates a table from an attribute domain.

     INPUTS:
      in_workspace (Workspace):
          The workspace containing the attribute domain to be converted to a
          table.
      domain_name (String):
          The name of the existing attribute domain.
      code_field (String):
          The name of the field in the created table that will store code
          values.
      description_field (String):
          The name of the field in the created table that will store code value
          descriptions.
      configuration_keyword {String}:
          For geodatabase tables, the custom storage keywords for creating the
          table.

     OUTPUTS:
      out_table (Table):
          The table to be created.

        """