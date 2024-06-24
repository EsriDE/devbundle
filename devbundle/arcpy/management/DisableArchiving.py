# Generated documentation for module arcpy.management


class DisableArchiving(object):
    """
    Disables archiving on a geodatabase feature class, table, or feature dataset.
    """

    @property
    def description(self) -> str:
        return """

        DisableArchiving_management(in_dataset, {preserve_history})

        Disables archiving on a geodatabase feature class, table, or feature
        dataset.

     INPUTS:
      in_dataset (Table / Feature Class / Feature Dataset):
          The geodatabase feature class, table, or feature dataset for which
          archiving will be disabled.
      preserve_history {Boolean}:
          Specifies whether records that are not from the current moment will be
          preserved.If the table or feature class is versioned, the history
          table or
          feature will become enabled.For nonversioned data, a table or feature
          class will be created that
          contains the history information. The name of the new dataset will be
          the same as the input with an appended _h.PRESERVE-Records that are
          not from the current moment will be
          preserved. This is the default.DELETE-Records that are not from the
          current moment will not be
          preserved; they will be deleted.

        """