# Generated documentation for module arcpy.management


class TableToDomain(object):
    """
    Creates or updates a coded value domain with values from a table.
    """

    @property
    def description(self) -> str:
        return """

        TableToDomain_management(in_table, code_field, description_field, in_workspace, domain_name, {domain_description}, {update_option})

        Creates or updates a coded value domain with values from a table.

     INPUTS:
      in_table (Table View):
          The database table from which the domain values will be derived.
      code_field (Field):
          The field in the database table from which the domain code values will
          be derived.
      description_field (Field):
          The field in the database table from which the domain description
          values will be derived.
      in_workspace (Workspace):
          The workspace that contains the domain that will be created or
          updated.
      domain_name (String):
          The name of the domain that will be created or updated.
      domain_description {String}:
          The description of the domain that will be created or updated. Domain
          descriptions of existing domains are not updated.
      update_option {String}:
          Specifies how the domain will be updated when you're using an existing
          domain.APPEND-The values from the input table will be appended to the
          existing domain values. This is the default.REPLACE-The existing
          domain values will be replaced with the values
          from the input table.

        """