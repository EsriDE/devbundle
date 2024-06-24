# Generated documentation for module arcpy.maritime


class ExportGeodatabaseToS57(object):
    """
    Exports hydrographic data from an ArcGIS Maritime geodatabase to an S-57 file.
    """

    @property
    def description(self) -> str:
        return """

        ExportGeodatabaseToS57_maritime(in_source_gdb, product, export_type, out_location, {in_product_config}, {clip_data_option}, {sample_export}, {in_scamin_file}, {in_feature_catalogue})

        Exports hydrographic data from an ArcGIS Maritime geodatabase to an
        S-57 file.

     INPUTS:
      in_source_gdb (Workspace):
          The database from which the product will be exported.
      product (String):
          The name of the product that will be exported. This product metadata
          entry must exist in the ProductDefinitions table, and the related
          extents must be present in the ProductCoverage feature class in the
          workspace.
      export_type (String):
          Specifies the type of file that will be created during
          export.NEW_DATASET-A new dataset including information that has not
          been
          previously distributed by updates will be created.NEW_EDITION-A new
          edition of a dataset including information that has
          not been previously distributed by updates will be created.UPDATE-
          Changes to a dataset since the last export will be reflected
          in the file.REISSUE-A reissue of a dataset including all the updates
          applied to
          the original dataset up to the date of reissue will be created. A
          reissue does not contain information that has not been previously
          issued by updates. CANCEL-When a dataset is deleted, an
          updated cell file is
          created containing only the Dataset General Information record with
          thefield. In this case, thesubfield must be set to 0. Dataset
          Identifier (DSID)Edition Number (EDTN)
      out_location (Folder):
          The location containing the output export package.
      in_product_config {File}:
          The configuration file that will be used to export the product.
      clip_data_option {Boolean}:
          Specifies whether the export process will clip data that crosses an
          M_CSCL feature.CLIP-Features in the source database that cross the
          boundary of an
          M_CSCL feature will be clipped to the boundary in the exported
          file.DO_NOT_CLIP-Features in the source database that cross the
          boundary
          of an M_CSCL feature will not be clipped to the boundary in the
          exported file. The features will remain intact in the output. This is
          the default.
      sample_export {Boolean}:
          Specifies whether the product will be exported as a
          sample.SAMPLE_EXPORT-The exported cell is not stored in the
          ProductExports
          table and the metadata information will not be updated in the
          ProductDefinitions table.OFFICIAL_EXPORT-The exported cell is stored
          in the ProductExports
          table as a BLOB, and the edition, update, and other metadata in the
          ProductDefinitions table will be updated. This is the default.
      in_scamin_file {File}:
          A custom configuration file that contains the rules for calculating a
          feature's SCAMIN value that overrides the default value. For
          additional information, refer to Scale Minimum: Radar Range method.
      in_feature_catalogue {File}:
          An .xml file that follows the S-100 Feature Catalogue format as
          defined by the IHO. It describes the content of a data product and its
          specifications. The default file location for S-100 catalogue files is
          <installation location>\ArcGIS Maritime\Product
          Files\<version>\S-101\, provided the Maritime product files are
          installed.

        """