# Generated documentation for module arcpy.management


class MigrateStorage(object):
    """
    Migrates the data from a binary, spatial, or spatial attribute column of one data type to a new column of a different data type in geodatabases in Oracle and SQL Server. The configuration keyword you specify when migrating determines the data type used for the new column.
    """

    @property
    def description(self) -> str:
        return """

        MigrateStorage_management(in_datasets;in_datasets..., config_keyword)

        Migrates the data from a binary, spatial, or spatial attribute column
        of one data type to a new column of a different data type in
        geodatabases in Oracle and SQL Server. The configuration keyword you
        specify when migrating determines the data type used for the new
        column.

     INPUTS:
      in_datasets (Table View / Raster Layer / Feature Dataset):
          The datasets to be migrated. The connection you use to access the
          datasets must be connecting as the dataset owner.
      config_keyword (String):
          The configuration keyword containing the appropriate parameter values
          for the migration. Parameter values are set by the geodatabase
          administrator. Contact your geodatabase administrator if you are
          unsure which configuration keyword to use.

        """