# Generated documentation for module arcpy.md


class MakeMultidimensionalVoxelLayer(object):
    """
    Creates a voxel layer from a multidimensional voxel dataset. Voxel datasets with a netCDF source are the only supported inputs.
    """

    @property
    def description(self) -> str:
        return """

        MakeMultidimensionalVoxelLayer_md(in_dataset, out_layer, {variables;variables...}, {voxel_position}, {exaggeration_mode}, {exaggeration}, {offset}, {optimize_performance})

        Creates a voxel layer from a multidimensional voxel dataset. Voxel
        datasets with a netCDF source are the only supported inputs.

     INPUTS:
      in_dataset (File):
          The input voxel dataset. Supported voxel datasets include netCDF
          files.
      variables {Value Table}:
          Specifies the names of the variables that will be output to
          the voxel layer and whether they are discrete or continuous. If no
          variables are specified, all variables from the voxel dataset will be
          used with the data types based on the type specified in the voxel
          dataset. For example, an integer will be assumed discrete and a double
          will be assumed continuous. Uncheck thecolumn value to remove the
          variable from the output layer. UseAvailable data types are as
          follows:CONTINUOUS-Use for floating-point values.DISCRETE-Use for
          nonfloating
          point values.
      voxel_position {String}:
          Specifies whether the voxel value will represent the values at the
          center or the origin of a voxel cube.CENTER-The voxel value will
          represent the center of the voxel cube.
          This is the default.ORIGIN-The voxel value will represent the origin
          of the voxel cube.
      exaggeration_mode {String}:
          Specifies the exaggeration mode that will be used for the voxel
          layer.FROM_VOXEL_DATASET_ORIGIN-Only the voxels will be scaled. This
          is the
          default.Z-COORDINATES-All z-positions will be multiplied by the
          exaggeration
          value. Use this option when exaggerating other 3D data with the voxel
          layer.
      exaggeration {Double}:
          The vertical exaggeration of the voxel layer. The default value is
          proportional to the x,y extent of the layer.
      offset {Double}:
          An offset that will be used to raise or lower the voxel layer in the
          z-dimension.
      optimize_performance {Boolean}:
          Specifies whether a .vxc1 file will be created to enhance the display
          performance of the voxel layer. The file will be created in the same
          folder as the netCDF file.OPTIMIZED-A .vxc1 file will be created. This
          is the
          default.NOT_OPTIMIZED-A .vxc1 file will not be created.

     OUTPUTS:
      out_layer (Voxel Layer):
          The output voxel layer.

        """