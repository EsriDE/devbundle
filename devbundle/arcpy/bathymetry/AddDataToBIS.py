# Generated documentation for module arcpy.bathymetry


class AddDataToBIS(object):
    """
    Registers raster and feature class data to a Bathymetric Information System (BIS).
    """

    @property
    def description(self) -> str:
        return """

        AddDataToBIS_bathymetry(target_workspace, in_data;in_data..., {input_types;input_types...}, {include_subfolders}, {footprint_type}, {vertical_units}, {directionality}, {in_bag_metadata_mapping_file}, {update_overviews})

        Registers raster and feature class data to a Bathymetric Information
        System (BIS).

     INPUTS:
      target_workspace (Workspace):
          The enterprise or file geodatabase where the BIS is located.
      in_data (Workspace / Feature Layer / Image Service / Raster Layer / Mosaic Layer / Layer File / ServerConnection / TIN Layer):
          The input workspaces, datasets, layers, or feature classes that
          contain the data that will be added to the target BIS.
      input_types {String}:
          Specifies the types of data that will be included from any workspaces
          provided in the input_data parameter. All data types are included by
          default.FEATURE_CLASS-Feature classes will be
          included.FEATURE_SERVICE-Feature
          services will be included.IMAGE_SERVICE-Image services will be
          included.LAYER_FILE-Layer files will be included.MAP_SERVICE-Map
          services will be included.MOSAIC_DATASET-Mosaic datasets will be
          included.RASTER_DATASET-Raster datasets will be
          included.SCENE_LAYER_PACKAGE-Scene layer packages will be
          included.TIN-TIN datasets will be included.
      include_subfolders {Boolean}:
          Specifies whether the contents of a workspace subfolder will be added
          to the BIS. This parameter is not applicable to file or enterprise
          geodatabases.INCLUDE_SUBFOLDERS-Valid data found in the subfolders
          will be added to
          the BIS.NOT_INCLUDE_SUBFOLDERS-Subfolder contents will not be added
          to the
          BIS. This is the default.
      footprint_type {String}:
          Specifies whether the footprint will be the full extent of the dataset
          or a convex hull representing the minimum bounding box for all
          features.ENVELOPE-The footprint will be the full extent of the
          dataset. This
          is the default.CONVEX_HULL-The footprint will be a convex polygon
          representing the
          minimum bounding box for all features.
      vertical_units {String}:
          Specifies the vertical units that will be used for the depth
          data.METERS-The vertical units will be meters.FEET-The vertical
          units
          will be feet.FEET_US-The vertical units will be U.S. Survey
          feet.FATHOMS-The vertical units will be fathoms.
      directionality {String}:
          Specifies the directionality of the elevation data.POSITIVE_UP-The
          directionality of elevation data will be positive
          up.POSITIVE_DOWN-The directionality of elevation data will be positive
          down.
      in_bag_metadata_mapping_file {File}:
          The metadata mapping file that contains the XML element tree mapping
          information for Bathymetric Attributed Grid (BAG) internal metadata.
          This metadata mapping file can be used if the
          add_bag_metadata_fields.py script has first been run on the BIS. Both
          the Python script and the mapping file are in the ArcGIS Bathymetry
          product data files at <installation location>\ArcGIS
          Bathymetry\Product Files\<version>\BAGSupport. If the BAG metadata
          mapping file is used, internal BAG metadata will be extracted from
          input BAGs and the values will be populated in the BIS Catalog.
      update_overviews {Boolean}:
          Specifies whether overviews and statistics for a mosaic dataset will
          be calculated and updated.UPDATE_OVERVIEWS-Overviews and statistics
          will be calculated and
          updated. This is the default.NOT_UPDATE_OVERVIEWS-Overviews and
          statistics will not be calculated
          and updated.

        """