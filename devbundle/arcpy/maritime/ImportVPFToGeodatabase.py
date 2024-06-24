# Generated documentation for module arcpy.maritime


class ImportVPFToGeodatabase(object):
    """
    Imports Vector Product Format (VPF) data in Digital Nautical Chart (DNC) and Tactical Ocean Data (TOD) formats into an ArcGIS Maritime geodatabase. Sources that can be imported include DNC and TOD0, TOD2, and TOD4.
    """

    @property
    def description(self) -> str:
        return """

        ImportVPFToGeodatabase_maritime(in_vpf_features;in_vpf_features..., target_workspace)

        Imports Vector Product Format (VPF) data in Digital Nautical Chart
        (DNC) and Tactical Ocean Data (TOD) formats into an ArcGIS Maritime
        geodatabase. Sources that can be imported include DNC and TOD0, TOD2,
        and TOD4.

     INPUTS:
      in_vpf_features (Folder):
          The VPF data to be imported into the geodatabase from a folder that
          contains one or more libraries. Point, line, polygon, and Ecrtext
          annotation features can be imported.
      target_workspace (Workspace):
          The geodatabase to which the VPF data will be imported. This can be an
          empty template or existing geodatabase.

        """