# Generated documentation for module arcpy.management


class TrimArchiveHistory(object):
    """
    Deletes retired archive records from nonversioned archive-enabled datasets.
    """

    @property
    def description(self) -> str:
        return """

        TrimArchiveHistory_management(in_table, trim_mode, {trim_before_date})

        Deletes retired archive records from nonversioned archive-enabled
        datasets.

     INPUTS:
      in_table (Table View):
          The nonversioned archive-enabled table with the archive history to be
          trimmed.
      trim_mode (String):
          Specifies the trim mode that will be used to trim the archive
          history.At the current version of ArcGIS Pro, only the delete trim
          mode is
          available.DELETE-The archive records will be deleted.
      trim_before_date {Date}:
          Archive records older than this date and time will be deleted. The
          date and time must be in UTC. If no date is provided, all archive
          records will be deleted.

        """