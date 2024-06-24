# Generated documentation for module arcpy.management


class ImportXMLWorkspaceDocument(object):
    """
    Imports the contents of an XML workspace document into an existing geodatabase.
    """

    @property
    def description(self) -> str:
        return """

        ImportXMLWorkspaceDocument_management(target_geodatabase, in_file, {import_type}, {config_keyword})

        Imports the contents of an XML workspace document into an existing
        geodatabase.

     INPUTS:
      target_geodatabase (Workspace):
          The existing geodatabase where the contents of the XML workspace
          document will be imported.
      in_file (File):
          The input XML workspace document file containing geodatabase contents
          to be imported. The file can be an .xml file or a compressed .zip or
          .z file containing the .xml file.
      import_type {String}:
          Specifies whether both data (feature class and table records,
          including geometry) and schema will be imported, or only the schema
          will be imported.DATA-Data and schema will be imported. This is the
          default.SCHEMA_ONLY-Only the schema will be imported.
      config_keyword {String}:
          The geodatabase configuration keyword to be applied if
          theparameter value is an enterprise or file geodatabase. Target
          Geodatabase

        """