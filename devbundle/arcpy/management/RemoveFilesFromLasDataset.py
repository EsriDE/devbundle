# Generated documentation for module arcpy.management


class RemoveFilesFromLasDataset(object):
    """
    Removes one or more LAS files and surface constraint features from a LAS dataset.
    """

    @property
    def description(self) -> str:
        return """

        RemoveFilesFromLasDataset_management(in_las_dataset, {in_files;in_files...}, {in_surface_constraints;in_surface_constraints...}, {delete_pyramid})

        Removes one or more LAS files and surface constraint features from a
        LAS dataset.

     INPUTS:
      in_las_dataset (LAS Dataset Layer):
          The LAS dataset that will be processed.
      in_files {String}:
          The name of the LAS files or folders containing LAS files whose
          reference will be removed from the LAS dataset.
      in_surface_constraints {String}:
          The name of the surface constraint features that will be removed from
          the LAS dataset.
      delete_pyramid {Boolean}:
          Specifies whether the LAS dataset's display pyramid will be
          deleted.DELETE_PYRAMID-The LAS dataset's display pyramid will be
          deleted.NO_DELETE_PYRAMID-The LAS dataset's display pyramid will not
          be
          deleted. This is the default.

        """