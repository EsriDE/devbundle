# Generated documentation for module arcpy.management


class CreateFileGDB(object):
    """
    Creates a file geodatabase in a folder.
    """

    @property
    def description(self) -> str:
        return """

        CreateFileGDB_management(out_folder_path, out_name, {out_version})

        Creates a file geodatabase in a folder.

     INPUTS:
      out_folder_path (Folder):
          The folder where the file geodatabase will be created.
      out_name (String):
          The name of the file geodatabase to be created.
      out_version {String}:
          Specifies the ArcGIS version for the new geodatabase.CURRENT-A
          geodatabase compatible with the currently installed version
          of ArcGIS will be created. This is the default.10.0-A geodatabase
          compatible with ArcGIS version 10 will be created.9.3-A geodatabase
          compatible with ArcGIS version 9.3 will be created.9.2-A geodatabase
          compatible with ArcGIS version 9.2 will be created.

        """