# Generated documentation for module arcpy.management


class EnableEnterpriseGeodatabase(object):
    """
    Creates geodatabase system tables, stored procedures, functions, and types in an existing database, which enable geodatabase functionality in the database.
    """

    @property
    def description(self) -> str:
        return """

        EnableEnterpriseGeodatabase_management(input_database, authorization_file)

        Creates geodatabase system tables, stored procedures, functions, and
        types in an existing database, which enable geodatabase functionality
        in the database.

     INPUTS:
      input_database (Workspace):
          The path and database connection file (.sde) name for the database in
          which geodatabase functionality will be enabled. The database
          connection must connect as a user that qualifies as a geodatabase
          administrator.
      authorization_file (File):
          The keycodes file that was created when ArcGIS Server was authorized.
          If you have not done so, authorize ArcGIS Server to create this file.
          This file is in the <drive>\Program
          Files\ESRI\License<release#>\sysgen folder on Windows or the
          /arcgis/server/framework/runtime/.wine/drive_c/Program
          Files/ESRI/License<release#>/sysgen directory on Linux. The
          /.wine directory is a hidden directory.You may need to copy the
          keycodes file from the ArcGIS Server machine
          to a location that is accessible to the tool.

        """