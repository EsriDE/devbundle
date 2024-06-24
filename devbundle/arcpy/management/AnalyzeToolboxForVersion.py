# Generated documentation for module arcpy.management


class AnalyzeToolboxForVersion(object):
    """
    Analyzes the contents of a toolbox and identifies compatibility issues with previous versions of ArcGIS software.
    """

    @property
    def description(self) -> str:
        return """

        AnalyzeToolboxForVersion_management(in_toolbox, version, {report})

        Analyzes the contents of a toolbox and identifies compatibility issues
        with previous versions of ArcGIS software.

     INPUTS:
      in_toolbox (Toolbox):
          The input toolbox (.tbx or .atbx file) that will be analyzed.The
          Python toolbox format (.pyt file) is not supported as an input.
      version (String):
          Specifies the software version that will be used for toolbox
          compatibility analysis.10.6.0-ArcGIS Desktop 10.6.0 will be used for
          toolbox compatibility
          issue analysis.10.7.0-ArcGIS Desktop 10.7.0 will be used for toolbox
          compatibility
          issue analysis.10.8.0-ArcGIS Desktop 10.8.0 will be used for toolbox
          compatibility
          issue analysis.10.8.2-ArcGIS Desktop 10.8.2 will be used for toolbox
          compatibility
          issue analysis.2.2-ArcGIS Pro 2.2 will be used for toolbox
          compatibility issue
          analysis.2.3-ArcGIS Pro 2.3 will be used for toolbox compatibility
          issue
          analysis.2.4-ArcGIS Pro 2.4 will be used for toolbox compatibility
          issue
          analysis.2.5-ArcGIS Pro 2.5 will be used for toolbox compatibility
          issue
          analysis.2.6-ArcGIS Pro 2.6 will be used for toolbox compatibility
          issue
          analysis.2.7-ArcGIS Pro 2.7 will be used for toolbox compatibility
          issue
          analysis.2.8-ArcGIS Pro 2.8 will be used for toolbox compatibility
          issue
          analysis.2.9-ArcGIS Pro 2.9 will be used for toolbox compatibility
          issue
          analysis.3.0-ArcGIS Pro 3.0 will be used for toolbox compatibility
          issue
          analysis.

     OUTPUTS:
      report {File}:
          The text file that will be created containing the compatibility issues
          identified by the analyzers.

        """