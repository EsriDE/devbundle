# Generated documentation for module arcpy.management


class CreateCatalogDataset(object):
    """
    Creates a catalog dataset to which collections of layers, rasters, datasets, and other items can be added.
    """

    @property
    def description(self) -> str:
        return """

        CreateCatalogDataset_management(out_path, out_name, spatial_reference, {template;template...}, {has_z}, {out_alias}, {config_keyword})

        Creates a catalog dataset to which collections of layers, rasters,
        datasets, and other items can be added.

     INPUTS:
      out_path (Workspace / Feature Dataset):
          The enterprise or file geodatabase in which the output catalog dataset
          will be created.
      out_name (String):
          The name of the catalog dataset that will be created.
      spatial_reference (Spatial Reference):
          The spatial reference of the catalog dataset.
      template {Table View}:
          The feature class or table that will be used as a template to define
          the attribute fields of the new catalog dataset.
      has_z {String}:
          Specifies whether the catalog dataset will contain elevation values
          (z-values).DISABLED-The output catalog dataset will not contain
          z-values. This is
          the default.ENABLED-The output catalog dataset will contain
          z-values.SAME_AS_TEMPLATE-The output catalog dataset will contain
          z-values if
          the dataset specified in the template parameter contains z-values.
      out_alias {String}:
          The alias name of the catalog dataset.
      config_keyword {String}:
          The configuration keyword determines the storage parameters of the
          database table. The configuration keyword applies to enterprise data
          only.

        """