# Generated documentation for module arcpy.maritime


class ExportGeodatabaseToVPF(object):
    """
    Exports hydrographic data from maritime geodatabases to Vector Product Format (VPF).
    """

    @property
    def description(self) -> str:
        return """

        ExportGeodatabaseToVPF_maritime(in_source_gdb;in_source_gdb..., ntm_date, out_location)

        Exports hydrographic data from maritime geodatabases to Vector Product
        Format (VPF).

     INPUTS:
      in_source_gdb (Workspace):
          The source geodatabases that will be exported.
      ntm_date (String):
          The Notice to Mariners date of the source geodatabases.
      out_location (Folder):
          The location where the export package will be written.

        """