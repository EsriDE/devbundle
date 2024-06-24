# Generated documentation for module arcpy.management


class CreateDatabaseView(object):
    """
    Creates a view in a database based on an SQL expression.
    """

    @property
    def description(self) -> str:
        return """

        CreateDatabaseView_management(input_database, view_name, view_definition)

        Creates a view in a database based on an SQL expression.

     INPUTS:
      input_database (Workspace):
          The database that contains the tables or feature classes used to
          construct the view. This database is also where the view will be
          created.
      view_name (String):
          The name of the view that will be created in the database.
      view_definition (String):
          An SQL statement that will be used to construct the view.

        """