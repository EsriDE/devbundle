# Generated documentation for module arcpy.management


class DeleteSchemaGeodatabase(object):
    """
    Deletes a geodatabase from a user's schema in Oracle.
    """

    @property
    def description(self) -> str:
        return """

        DeleteSchemaGeodatabase_management(input_database)

        Deletes a geodatabase from a user's schema in Oracle.

     INPUTS:
      input_database (Workspace):
          The database connection file (.sde) of the user-schema geodatabase to
          be deleted. You must connect as the schema owner.

        """