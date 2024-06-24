# Generated documentation for module arcpy.management


class RecoverFileGDB(object):
    """
    Recovers data from a file geodatabase that has become corrupt.
    """

    @property
    def description(self) -> str:
        return """

        RecoverFileGDB_management(input_file_gdb, output_location, out_name)

        Recovers data from a file geodatabase that has become corrupt.

     INPUTS:
      input_file_gdb (Workspace):
          Input corrupt file geodatabase.
      output_location (Folder):
          Output folder location for the recovered file geodatabase.
      out_name (String):
          Name for the output file geodatabase.

        """