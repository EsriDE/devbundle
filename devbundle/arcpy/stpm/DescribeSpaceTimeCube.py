# Generated documentation for module arcpy.stpm


class DescribeSpaceTimeCube(object):
    """
    Summarizes the contents and characteristics of a space-time cube. The tool describes the temporal and spatial extent of the space-time cube, the variables in the space-time cube, the analyses performed on each variable, and the 2D and 3D display themes available for each variable.
    """

    @property
    def description(self) -> str:
        return """

        DescribeSpaceTimeCube_stpm(in_cube, {out_characteristics_table}, {out_spatial_extent})

        Summarizes the contents and characteristics of a space-time cube. The
        tool describes the temporal and spatial extent of the space-time cube,
        the variables in the space-time cube, the analyses performed on each
        variable, and the 2D and 3D display themes available for each
        variable.

     INPUTS:
      in_cube (File):
          The space-time cube to be described. Space-time cubes have an .nc file
          extension and are created using various tools in the Space Time
          Pattern Mining toolbox.

     OUTPUTS:
      out_characteristics_table {Table}:
          The table containing summary information about the input space-time
          cube.
      out_spatial_extent {Feature Class}:
          A feature class with a single rectangle that represents the spatial
          extent of the input space-time cube.

        """