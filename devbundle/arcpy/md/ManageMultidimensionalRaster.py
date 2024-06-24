# Generated documentation for module arcpy.md


class ManageMultidimensionalRaster(object):
    """
    Edits a multidimensional raster by adding or deleting variables or dimensions.
    """

    @property
    def description(self) -> str:
        return """

        ManageMultidimensionalRaster_md(target_multidimensional_raster, {manage_mode}, {variables;variables...}, {in_multidimensional_rasters;in_multidimensional_rasters...}, {dimension_name}, {dimension_value}, {dimension_description}, {dimension_unit}, {update_statistics}, {update_transpose})

        Edits a multidimensional raster by adding or deleting variables or
        dimensions.

     INPUTS:
      target_multidimensional_raster (Raster Dataset / Mosaic Dataset / Raster Layer / Mosaic Layer / Image Service):
          The multidimensional raster in CRF to modify.
      manage_mode {String}:
          Specifies the type of modification that will be performed on the
          target raster.ADD_DIMENSION-A dimension will be added to the input
          multidimensional
          raster.APPEND_SLICES-Slices from the input multidimensional rasters
          will be
          added to the end of the slices for a dimension. This is the
          default.APPEND_VARIABLES-The variables from the input multidimensional
          rasters
          will be added.REPLACE_SLICES-Existing slices will be replaced by
          slices from another
          multidimensional raster, at specific dimension
          values.DELETE_VARIABLES-One or more variables will be deleted from the
          multidimensional raster.REMOVE_DIMENSION-A single slice
          multidimensional raster will be
          converted to a dimensionless raster.
      variables {String}:
          The variable or variables that will be modified in the target
          multidimensional raster. This parameter is required if the operation
          being performed is a modification of an existing variable.If no
          variable is specified, the first variable in the target
          multidimensional raster will be modified.
      in_multidimensional_rasters {Raster Layer / Image Service}:
          The multidimensional raster datasets that contain the slices or
          variables to be added to the target multidimensional raster. This
          parameter is required when the manage_mode parameter is set to
          APPEND_SLICES, REPLACE_SLICES, or APPEND_VARIABLES.
      dimension_name {String}:
          The name of the dimension to be added to or removed from the raster
          properties. This parameter is required when the manage_mode is set to
          ADD_DIMENSION. If the manage_mode parameter is set to
          REMOVE_DIMENSION, the specified dimension can only contain a single
          value. If the dimension_name parameter is not specified and the input
          only contains a single slice, all dimensions will be removed.
      dimension_value {String}:
          The value of the dimension to be added. The value can be a single
          value or a range of values. For a range of values, provide the minimum
          and maximum values separated by a comma. For example, for a new height
          dimension, enter 0,10 to generate a dimension in which the first slice
          contains information for the first 10 meters of height.This parameter
          is required when the manage_mode parameter is set to
          ADD_DIMENSION.
      dimension_description {String}:
          The description of the new dimension to be added to the raster
          properties for metadata purposes. This parameter is enabled when the
          manage_mode parameter is set to ADD_DIMENSION.
      dimension_unit {String}:
          The unit of the new dimension to be added to the raster properties for
          metadata purposes. This parameter is enabled when the manage_mode
          parameter is set to ADD_DIMENSION.
      update_statistics {Boolean}:
          Specifies whether the statistics will be recalculated for the
          multidimensional raster dataset.UPDATE_STATISTICS-Statistics will be
          recalculated. This is the
          default.NO_UPDATE_STATISTICS-Statistics will not be recalculated.
      update_transpose {Boolean}:
          Specifies whether the transpose will be rebuilt for the
          multidimensional raster dataset.UPDATE_TRANSPOSE-The transpose will be
          rebuilt. If no transpose
          exists, a new transpose will be built. This is the
          default.NO_UPDATE_TRANSPOSE-The transpose will not be rebuilt.

        """