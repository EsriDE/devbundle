# Generated documentation for module arcpy.rm


class ComputeDepthMap(object):
    """
    Computes a more accurate CenterZ field value based on the depth map for each image comprising a mosaic dataset. Control points and solution points are used to compute a depth map for each image comprising a mosaic dataset to improve image-to-ground (map) transformation, especially in high oblique cases.
    """

    @property
    def description(self) -> str:
        return """

        ComputeDepthMap_rm(in_mosaic_dataset, control_point_table, solution_point_table, {where_clause}, {skip_existing}, {adjust_footprints})

        Computes a more accurate CenterZ field value based on the depth map
        for each image comprising a mosaic dataset. Control points and
        solution points are used to compute a depth map for each image
        comprising a mosaic dataset to improve image-to-ground (map)
        transformation, especially in high oblique cases.

     INPUTS:
      in_mosaic_dataset (Mosaic Dataset / Mosaic Layer):
          The block adjusted input mosaic dataset. The mosaic dataset must be
          adjusted before it is used as input for this tool. You can use an
          ortho mapping workflow in ArcGIS Pro, or a Reality for ArcGIS Pro
          workflow, to adjust the mosaic dataset.
      control_point_table (Feature Class / Feature Layer):
          The input control point feature class. This point feature class is the
          output of the Compute Camera Model tool or the Compute Tie Points
          tool.
      solution_point_table (Feature Class / Feature Layer):
          The input solution point feature class. This point feature class is
          the output of the Compute Camera Model tool or the Compute Tie Points
          tool.
      where_clause {SQL Expression}:
          An SQL expression that will be used to select items in the mosaic
          dataset to include in the depth map.
      skip_existing {Boolean}:
          Specifies whether a depth mapvalue will be computed only for
          rasters without avalue, or computed for all mosaic dataset items
          including those with an existingvalue. CenterZCenterZCenterZ
          NO_SKIP_EXISTING-A depth mapvalue will be computed for every
          mosaic dataset item, including items with an existingvalue. This is
          the default. CenterZCenterZ         SKIP_EXISTING-A depth
          mapvalue will only be computed for
          rasters that do not have avalue. CenterZCenterZ
      adjust_footprints {Boolean}:
          Specifies whether the footprint geometry will be updated using the
          same transformation that was applied to the
          image.NO_ADJUST_FOOTPRINTS-The footprint geometry will not be updated.
          This
          is the default.ADJUST_FOOTPRINTS-The footprint geometry will be
          updated to the image
          geometry.

        """