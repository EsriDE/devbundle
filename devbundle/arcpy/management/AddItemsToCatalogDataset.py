# Generated documentation for module arcpy.management


class AddItemsToCatalogDataset(object):
    """
    Adds workspace items and layers-such as geodatabase datasets, raster layers, feature layers, mosaic layers, and other items-to an existing catalog dataset.
    """

    @property
    def description(self) -> str:
        return """

        AddItemsToCatalogDataset_management(target_catalog_dataset, input_items;input_items..., {input_item_types;input_item_types...}, {include_subfolders}, {footprint_type})

        Adds workspace items and layers-such as geodatabase datasets, raster
        layers, feature layers, mosaic layers, and other items-to an existing
        catalog dataset.

     INPUTS:
      target_catalog_dataset (Catalog Layer):
          The catalog dataset to which the items will be added.
      input_items (Workspace / Feature Layer / Image Service / Raster Layer / Mosaic Layer / LAS Dataset Layer / Layer File / CAD Drawing Dataset / ServerConnection / BIM File Workspace / TIN Layer):
          The workspace items, layers, and files from which items will be added
          to the catalog dataset. The workspace can be a folder, file
          geodatabase, feature dataset, enterprise database, or a service from a
          server connection.
      input_item_types {String}:
          Specifies the item types that will be added to the catalog dataset
          from any input workspaces. All supported item types will be added by
          default.BIM_FILE_WORKSPACE-BIM file workspaces will be
          added.BIM_FILE_FLOORPLAN-BIM file floor plans will be
          added.CAD_DRAWING-CAD drawings will be added.FEATURE_CLASS-Feature
          classes will be added.FEATURE_SERVICE-Feature services will be
          added.IMAGE_SERVICE-Image services will be added.LAS_DATASET-LAS
          datasets will be added.LAS_FILE-LAS files will be
          added.LAYER_FILE-Layer files will be added.MAP_SERVICE-Map services
          will be added.MOSAIC_DATASET-Mosaic datasets will be
          added.RASTER_DATASET-Raster datasets will be
          added.SCENE_LAYER_PACKAGE-Scene layer packages will be added.TIN-TIN
          datasets will be added.
      include_subfolders {Boolean}:
          Specifies whether the contents of folders or workspaces specified in
          the input_items parameter value will be recursively searched and added
          to the catalog dataset. This setting is not applicable to file or
          enterprise geodatabases.INCLUDE_SUBFOLDERS-The contents of folders or
          workspaces will be
          recursively searched and added to the catalog dataset. This is the
          default.NOT_INCLUDE_SUBFOLDERS-The contents of folders or workspaces
          will not
          be recursively searched and added to the catalog dataset.
      footprint_type {String}:
          Specifies whether the reference item's footprint will be the full
          extent or a convex hull representing the smallest convex polygon for
          all features.ENVELOPE-The footprint will be a rectangle covering the
          full extent of
          the reference item. This is the default.CONVEX_HULL-The footprint will
          be a convex hull enclosing all features
          from the reference item.

        """