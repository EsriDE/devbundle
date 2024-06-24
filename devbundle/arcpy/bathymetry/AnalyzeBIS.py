# Generated documentation for module arcpy.bathymetry


class AnalyzeBIS(object):
    """
    Analyzes a Bathymetric Information System (BIS).
    """

    @property
    def description(self) -> str:
        return """

        AnalyzeBIS_bathymetry(in_bis, {bis_checks;bis_checks...}, {repair_operations;repair_operations...})

        Analyzes a Bathymetric Information System (BIS).

     INPUTS:
      in_bis (Workspace):
          The input BIS.
      bis_checks {String}:
          Specifies the checks that will be performed on the
          BIS.BIS_STRUCTURE-The structure of the BIS will be analyzed to ensure
          it
          is a valid BIS.BISCATALOG_LINKS-The BisCatalog will be analyzed for
          broken links.BISBDI_LINKS-The BisBDI will be analyzed for broken
          links.BISCATALOG_BISBDI_SYNC-The catalog dataset will be compared to
          the
          mosaic dataset to detect entries that do not
          match.PROXY_RASTER_CHECK-Identifies proxy raster problems.
      repair_operations {String}:
          Specifies the repair operations that will be
          performed.REMOVE_EXCESS_PROXY_RASTERS-Unused proxy rasters will be
          deleted.

        """