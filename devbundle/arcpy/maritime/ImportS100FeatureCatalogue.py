# Generated documentation for module arcpy.maritime


class ImportS100FeatureCatalogue(object):
    """
    Imports the contents of an S-100 feature catalogue to an existing geodatabase. A feature catalogue is an XML document that describes the content of a data product.
    """

    @property
    def description(self) -> str:
        return """

        ImportS100FeatureCatalogue_maritime(in_feature_catalogue, target_workspace, {admin_connection}, {coordinate_system}, {subtype_mapping}, {config_keyword})

        Imports the contents of an S-100 feature catalogue to an existing
        geodatabase. A feature catalogue is an XML document that describes the
        content of a data product.

     INPUTS:
      in_feature_catalogue (File):
          An .xml file that follows the S-100 Feature Catalogue format as
          defined by the IHO. It describes the content of a data product and its
          specifications. The default file location for S-100 catalogue files is
          <installation location>\ArcGIS Maritime\Product
          Files\<version>\S-101\, provided the Maritime product files are
          installed.
      target_workspace (Workspace):
          The geodatabase to which the schema will be written.
      admin_connection {File}:
          Admin Connection
      coordinate_system {Coordinate System}:
          The coordinate system of the output workspace. The default is WGS84.
      subtype_mapping {File}:
          The subtype mapping .xml file used to specify feature classes that
          each S-100 feature will be subtyped in. If no parameter value is
          specified, the created data model will have separate feature classes
          for each S-100 object type. For S-101, it is recommended that you use
          the S-101FeatureClassMap.xml file. The default file location is
          C:/<ArcGIS Pro installation location>\Pro\Resources\Maritime.
      config_keyword {String}:
          The configuration keyword applies to enterprise geodatabases data
          only. It determines the storage parameters of the database table.

        """