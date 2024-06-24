# Generated documentation for module arcpy.management


class ExportXMLWorkspaceDocument(object):
    """
    Creates a readable XML document of the geodatabase contents.
    """

    @property
    def description(self) -> str:
        return """

        ExportXMLWorkspaceDocument_management(in_data;in_data..., out_file, {export_type}, {storage_type}, {export_metadata})

        Creates a readable XML document of the geodatabase contents.

     INPUTS:
      in_data (Table / Feature Class / Feature Dataset / Raster Dataset / Workspace):
          The input datasets that will be exported and represented in an XML
          workspace document. The input data can be a geodatabase, feature
          dataset, feature class, table, raster, or raster catalog. If there are
          multiple inputs, the inputs must be from the same workspace. Multiple
          input workspaces are not supported.
      export_type {String}:
          Specifies whether the output XML workspace document will contain all
          of the data from the input (table and feature class records, including
          geometry) or only the schema.DATA-The schema and the data will be
          exported. This is the
          default.SCHEMA_ONLY-Only the schema will be exported.
      storage_type {String}:
          Specifies how feature geometry will be stored when data is exported
          from a feature class.BINARY-The geometry will be stored in a
          compressed base64 binary
          format. This binary format will produce a smaller XML workspace
          document. Use this option when the XML workspace document will be read
          by a custom program that uses ArcObjects. This is the
          default.NORMALIZED-The geometry will be stored in an uncompressed
          format.
          Using this option will result in a larger file. Use this option when
          the XML workspace document will be read by a custom program that does
          not use ArcObjects.
      export_metadata {Boolean}:
          Specifies whether the metadata will be exported.METADATA-If the input
          contains metadata, it will be exported. This is
          the default.NO_METADATA-Metadata will not be exported.

     OUTPUTS:
      out_file (File):
          The XML workspace document file that will be created. The output can
          be XML (with an .xml file extension) or compressed XML (with a .zip or
          .z file extension).

        """