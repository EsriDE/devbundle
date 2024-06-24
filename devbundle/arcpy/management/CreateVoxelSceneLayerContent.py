# Generated documentation for module arcpy.management


class CreateVoxelSceneLayerContent(object):
    """
    Creates a scene layer package (.slpk file) from a voxel layer input.
    """

    @property
    def description(self) -> str:
        return """

        CreateVoxelSceneLayerContent_management(in_dataset, out_slpk)

        Creates a scene layer package (.slpk file) from a voxel layer input.

     INPUTS:
      in_dataset (Layer File / Voxel Layer):
          The input voxel layer or layer file.

     OUTPUTS:
      out_slpk (File):
          The output scene layer package (.slpk file).

        """