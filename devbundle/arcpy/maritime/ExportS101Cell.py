# Generated documentation for module arcpy.maritime


class ExportS101Cell(object):
    """
    Exports S-101 hydrographic data from a geodatabase to an S-101 file.
    """

    @property
    def description(self) -> str:
        return """

        ExportS101Cell_maritime(in_feature_catalogue, in_s101_workspace, product, export_type, output_location)

        Exports S-101 hydrographic data from a geodatabase to an S-101 file.

     INPUTS:
      in_feature_catalogue (File):
          An .xml file that follows the S-100 Feature Catalogue format as
          defined by the IHO. It describes the content of a data product and its
          specifications. The default file location for S-100 catalogue files is
          <installation location>\ArcGIS Maritime\Product
          Files\<version>\S-101\, provided the Maritime product files are
          installed.
      in_s101_workspace (Workspace):
          The workspace that contains the product.
      product (String):
          The name of the product that will be exported.This information must
          exist in the ProductCoverage feature class and
          ProductDefinition table before using this tool.
      export_type (String):
          The type of file that will be created during export.NEW_EDITION-A new
          edition of a dataset, including new information that
          has not been previously distributed by updates. This is the default.
      output_location (Folder):
          The location where the export package will be written.

        """