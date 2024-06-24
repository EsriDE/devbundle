# Generated documentation for module arcpy.management


class ApplyBlockAdjustment(object):
    """
    Applies the geographic adjustments to the mosaic dataset items. This tool uses the solution table from the Compute Block Adjustments tool.
    """

    @property
    def description(self) -> str:
        return """

        ApplyBlockAdjustment_management(in_mosaic_dataset, adjustment_operation, {input_solution_table}, {pan_to_ms_scaling_factor}, {DEM}, {zoffset}, {control_point_table}, {adjust_footprints}, {solution_point_table}, {adjust_tiepoints})

        Applies the geographic adjustments to the mosaic dataset items. This
        tool uses the solution table from the Compute Block Adjustments tool.

     INPUTS:
      in_mosaic_dataset (Mosaic Dataset / Mosaic Layer):
          The input mosaic dataset to adjust.
      adjustment_operation (String):
          Specifies whether the mosaic dataset will be adjusted using the
          solution table or whether the mosaic dataset will be reset so there
          are no adjustments applied.ADJUST-The mosaic dataset will be adjusted
          using the input solution
          table.RESET-The mosaic dataset will be reset so there are no
          adjustments
          applied to it. REACTIVATE-Images dropped from the adjustment
          will be
          restored to active status. Images without the
          minimum number of control points required
          for adjustment are dropped from the computation in the standard
          adjustment operation, such that the images are categorized as Inactive
          in the footprints table, thevalue is set to 0, the imagery is not
          visible in the map, and the tie points statuses for the dropped images
          are disabled. This option will restore thestatus to Primary and ensure
          thevalue is resumed. Images that were included in the adjustment
          process are unaffected by this option. maxPSCategorymaxPS
      input_solution_table {Table View}:
          The solution table that will be used when adjusting the mosaic
          dataset. This is the output from the Compute Block Adjustments tool.
      pan_to_ms_scaling_factor {Double}:
          The scaling factor between the pan-sharpened resolution and the
          multispectral resolution that will be used if the mosaic dataset
          contains pan-sharpened rasters.
      DEM {Raster Dataset / Raster Layer / Mosaic Dataset / Mosaic Layer}:
          The DEM that will be used in the block adjustment. This DEM will only
          be used if it is a higher resolution than any existing DEM in the
          mosaic dataset.If this input DEM is used, the geometric function of
          the mosaic
          dataset will be updated using this input.
      zoffset {Double}:
          The vertical offset that will be used to adjust the elevation layer
          within the mosaic dataset's Geometric function.
      control_point_table {Table View}:
          The input control point table that will have the same adjustments
          applied as the solution table adjustments.
      adjust_footprints {Boolean}:
          Specifies whether the footprint geometry will be updated using the
          same transformation that will be applied to the
          image.NO_ADJUST_FOOTPRINTS-The footprint geometry will not be updated.
          This
          is the default.ADJUST_FOOTPRINTS-The footprint geometry will be
          updated. If a control
          point table is provided, it will also be transformed.
      solution_point_table {Table View}:
          The solution point table that will be used to update the status field
          for the control point table. This parameter is only used when the
          control_point_table parameter value is provided.
      adjust_tiepoints {Boolean}:
          Specifies whether the tie points will be updated when a solution point
          table is provided. This parameter is only used when the
          solution_point_table parameter value is
          provided.NO_ADJUST_TIEPOINTS-The tie points will not be updated. This
          is the
          default.ADJUST_TIEPOINTS-The tie points will be updated when a
          solution point
          table is provided.

        """