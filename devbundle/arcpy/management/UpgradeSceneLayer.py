# Generated documentation for module arcpy.management


class UpgradeSceneLayer(object):
    """
    Upgrades a scene layer package to the current I3S version in SLPK format or output to i3sREST format for use in ArcGIS Enterprise.
    """

    @property
    def description(self) -> str:
        return """

        UpgradeSceneLayer_management(in_dataset, out_folder_path, out_name, {out_log}, {texture_optimization}, {date_format})

        Upgrades a scene layer package to the current I3S version in SLPK
        format or output to i3sREST format for use in ArcGIS Enterprise.

     INPUTS:
      in_dataset (File):
          The input scene layer package.
      out_folder_path (Folder):
          The location where the output scene layer package will be created or
          the cloud connection file (.acs) to output to i3sREST format.
      out_name (String):
          The name of the output scene layer.
      texture_optimization {String}:
          Specifies the textures that will be optimized according to the
          target platform where the scene layer package is used.
          Optimizations that include KTX2 may take significant time to process.
          For fastest results, use the DESKTOP or NONE options.ALL-All texture
          formats will be optimized including JPEG, DXT, and
          KTX2 for use in desktop, web, and mobile platforms.DESKTOP-Windows,
          Linux, and Mac supported textures will be optimized
          including JPEG and DXT for use in ArcGIS Pro clients on Windows and
          ArcGIS Maps SDKs desktop clients on Windows, Linux, and Mac. This is
          the default.MOBILE-Android and iOS supported textures will be
          optimized including
          JPEG and KTX2 for use in ArcGIS Maps SDKs mobile
          applications.NONE-JPEG textures will be optimized for use in desktop
          and web
          platforms.
      date_format {String}:
          The format of the date values in the scene layers date fields. This
          parameter is hidden if no date fields are encountered.

     OUTPUTS:
      out_log {File}:
          The output log file that will summarize the results of the evaluation.

        """