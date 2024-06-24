# Generated documentation for module arcpy.aviation


class ImportDCDTChangeFile(object):
    """
    Imports an NGA Digital Chart Data Transaction (DCDT) change file into an aviation geodatabase.
    """

    @property
    def description(self) -> str:
        return """

        ImportDCDTChangeFile_aviation(in_change_file, target_gdb, current_cycle_date)

        Imports an NGA Digital Chart Data Transaction (DCDT) change file into
        an aviation geodatabase.

     INPUTS:
      in_change_file (File):
          The NGA DCDT change file is a Microsoft Access .mdb or .accdb file
          with changes to be loaded for the current chart cycle.
      target_gdb (Workspace):
          The Aviation charting schema workspace where the changes will be
          loaded.
      current_cycle_date (Date):
          The date of the current charting cycle.

        """