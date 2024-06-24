# Generated documentation for module arcpy.management


class AddIncrementingIDField(object):
    """
    Adds a database-maintained, incrementing ID field to an existing table or feature class in a Dameng, IBM Db2, Microsoft Azure SQL Database, Microsoft SQL Server, Oracle, or PostgreSQL database. A database- maintained ID field is required for all feature classes or tables you plan to edit through a feature service.
    """

    @property
    def description(self) -> str:
        return """

        AddIncrementingIDField_management(in_table, {field_name})

        Adds a database-maintained, incrementing ID field to an existing table
        or feature class in a Dameng, IBM Db2, Microsoft Azure SQL Database,
        Microsoft SQL Server, Oracle, or PostgreSQL database. A database-
        maintained ID field is required for all feature classes or tables you
        plan to edit through a feature service.

     INPUTS:
      in_table (Table View):
          The location and name of the table or feature class to which an ID
          field will be added.
      field_name {String}:
          The name to be used for the ID field. If no input is provided,
          the defaultwill be used. ObjectID

        """