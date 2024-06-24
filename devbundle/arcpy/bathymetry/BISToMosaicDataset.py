# Generated documentation for module arcpy.bathymetry


class BISToMosaicDataset(object):
    """
    Creates a mosaic dataset from a Bathymetric Information System (BIS).
    """

    @property
    def description(self) -> str:
        return """

        BISToMosaicDataset_bathymetry(in_bis_workspace, out_mosaic, {coordinate_system}, {in_query_file}, {create_overviews}, {force_overview_tiles})

        Creates a mosaic dataset from a Bathymetric Information System (BIS).

     INPUTS:
      in_bis_workspace (Workspace):
          The enterprise or file geodatabase where the BIS workspace is located.
      coordinate_system {Coordinate System}:
          The coordinate system that will be used for all items in the mosaic
          dataset.If no coordinate system is provided, WGS84 Web Mercator
          (auxiliary
          sphere) will be used by default.
      in_query_file {File}:
          The model or rule file that defines the datasets and sorting order
          that will be applied to the rasters included in the output mosaic
          dataset.Model file (*.model)-Defines the data to be exported from the
          BIS.
          Only the specified rasters will be exported to the mosaic dataset.Rule
          file (*.rule)-Defines the sorting order rules for the output
          data. All rasters in the BIS will be exported to the mosaic dataset.If
          no query file is provided, all rasters in the BIS will be exported.
      create_overviews {Boolean}:
          Specifies whether overviews for a mosaic dataset will be defined and
          generated.CREATE_OVERVIEWS-Overviews will be defined and
          generated.NO_OVERVIEWS-Overviews will not be defined or generated.
          This is the
          default.
      force_overview_tiles {Boolean}:
          Specifies whether overviews will be created at all levels or only
          above existing pyramid levels.FORCE_OVERVIEW_TILES-Overviews will be
          created at all
          levels.NO_FORCE_OVERVIEW_TILES-Overviews will only be created above
          the
          raster pyramid levels. This is the default.

     OUTPUTS:
      out_mosaic (Mosaic Dataset):
          The output mosaic dataset.

        """