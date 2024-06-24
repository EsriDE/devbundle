# Generated documentation for module arcpy.conversion


class MobileGdbToFileGdb(object):
    """
    Copies the contents of a mobile geodatabase to a new file geodatabase.
    """

    @property
    def description(self) -> str:
        return """

        MobileGdbToFileGdb_conversion(in_mobile_gdb, out_file_gdb)

        Copies the contents of a mobile geodatabase to a new file geodatabase.

     INPUTS:
      in_mobile_gdb (File):
          The mobile geodatabase with the contents that will be copied to a new
          file geodatabase.

     OUTPUTS:
      out_file_gdb (File):
          The name and location of the output file geodatabase, for example,
          c:\temp\outputGeodatabases\copiedFGDB.gdb.

        """