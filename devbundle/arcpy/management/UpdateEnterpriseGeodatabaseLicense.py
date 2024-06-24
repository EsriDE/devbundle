# Generated documentation for module arcpy.management


class UpdateEnterpriseGeodatabaseLicense(object):
    """
    Updates the ArcGIS Server license in an enterprise geodatabase.
    """

    @property
    def description(self) -> str:
        return """

        UpdateEnterpriseGeodatabaseLicense_management(input_database, authorization_file)

        Updates the ArcGIS Server license in an enterprise geodatabase.

     INPUTS:
      input_database (Workspace):
          A database connection (.sde file) to the enterprise geodatabase to
          authorize with a new ArcGIS Server enterprise authorization file.The
          database connection file must connect to the database as the
          geodatabase administrator.
      authorization_file (File):
          The path and file name of the keycodes file generated when ArcGIS
          Server enterprise was authorized. If necessary, copy the file from the
          ArcGIS Server machine to a directory that the tool can access.ArcGIS
          Server creates the keycodes file in the following location:
          \\Program Files\ESRI\License<release#>\sysgen (Microsoft Windows
          servers) or /arcgis/server/framework/runtime/.wine/drive_c/Program
          Files/ESRI/License<release#>/sysgen (Linux servers).

        """