# Generated documentation for module arcpy.management


class GenerateLicensedFgdb(object):
    """
    Generates a license definition file (.licdef) that defines and restricts the display of contents in a file geodatabase. The contents of the licensed file geodatabase can be viewed by creating a license file (*.sdlic) and configuring the ArcGIS clients to recognize it. The license file is created using the Generate File Geodatabase License tool.
    """

    @property
    def description(self) -> str:
        return """

        GenerateLicensedFgdb_management(in_fgdb, out_fgdb, out_lic_def)

        Generates a license definition file (.licdef) that defines and
        restricts the display of contents in a file geodatabase. The contents
        of the licensed file geodatabase can be viewed by creating a license
        file (*.sdlic) and configuring the ArcGIS clients to recognize it. The
        license file is created using the Generate File Geodatabase License
        tool.

     INPUTS:
      in_fgdb (Workspace):
          The unlicensed file geodatabase that will be licensed.

     OUTPUTS:
      out_fgdb (Workspace):
          The name and location of the generated licensed file geodatabase.
      out_lic_def (File):
          The license definition file.

        """