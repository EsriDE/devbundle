# Generated documentation for module arcpy.management


class MigrateObjectIDTo64Bit(object):
    """
    Migrates a dataset's or multiple datasets' ObjectID field to 64-bit object IDs.
    """

    @property
    def description(self) -> str:
        return """

        MigrateObjectIDTo64Bit_management(in_datasets;in_datasets...)

        Migrates a dataset's or multiple datasets' ObjectID field to 64-bit
        object IDs.

     INPUTS:
      in_datasets (Table View / Feature Dataset / Layer):
          The datasets that will have theirfield migrated to 64 bit.
          ObjectID

        """