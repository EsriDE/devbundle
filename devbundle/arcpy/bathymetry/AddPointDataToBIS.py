# Generated documentation for module arcpy.bathymetry


class AddPointDataToBIS(object):
    """
    Registers point cloud or elevation point data to a Bathymetric Information System (BIS).
    """

    @property
    def description(self) -> str:
        return """

        AddPointDataToBIS_bathymetry(target_workspace, in_data;in_data..., vertical_units, directionality, {depth_field}, {footprint_type}, {cell_size}, {update_overviews})

        Registers point cloud or elevation point data to a Bathymetric
        Information System (BIS).

     INPUTS:
      target_workspace (Workspace):
          The enterprise or file geodatabase where the BIS is located.
      in_data (LAS Dataset Layer / Feature Layer):
          The input LAS, LASD, point feature class (z-enabled and not
          z-enabled), shapefile, or multipoint features that will be added to
          the target workspace.
      vertical_units (String):
          Specifies the vertical units that will be used for the depth
          data.METERS-The vertical units will be meters.FEET-The vertical
          units
          will be feet.FEET_US-The vertical units will be U.S. Survey
          feet.FATHOMS-The vertical units will be fathoms.
      directionality (String):
          Specifies the directionality of the elevation data.POSITIVE_UP-The
          directionality of elevation data will be positive
          up.POSITIVE_DOWN-The directionality of elevation data will be positive
          down.
      depth_field {String}:
          The field where the depth is stored. It is either a numeric field or
          the shape field specified in the in_data parameter value.
      footprint_type {String}:
          Specifies whether the footprint will be the full extent of the dataset
          or a convex hull representing the minimum bounding box for all
          features.ENVELOPE-The footprint will be the full extent of the
          dataset. This
          is the default.CONVEX_HULL-The footprint will be a convex polygon
          representing the
          minimum bounding box for all features.
      cell_size {Double}:
          The cell size of the proxy raster. The horizontal unit is the same as
          that of the input datasets.If no cell size is specified, additional
          rules will be used to
          calculate it from the other inputs.
      update_overviews {Boolean}:
          Specifies whether overviews and statistics for a mosaic dataset will
          be calculated and updated.UPDATE_OVERVIEWS-Overviews and statistics
          will be calculated and
          updated. This is the default.NOT_UPDATE_OVERVIEWS-Overviews and
          statistics will not be calculated
          and updated.

        """