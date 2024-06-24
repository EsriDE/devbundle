# Generated documentation for module arcpy.management


class DefineProjection(object):
    """
    Overwrites the coordinate system information (map projection and datum) stored with a dataset. This tool is intended for datasets that have an unknown or incorrect coordinate system defined.
    """

    @property
    def description(self) -> str:
        return """

        DefineProjection_management(in_dataset, coor_system)

        Overwrites the coordinate system information (map projection and
        datum) stored with a dataset. This tool is intended for datasets that
        have an unknown or incorrect coordinate system defined.

     INPUTS:
      in_dataset (Feature Layer / Geodataset):
          The dataset or feature class whose projection will be defined.
      coor_system (Coordinate System):
          The coordinate system that will be applied to the input.Valid values
          are a SpatialReference object, a file with a .prj
          extension, or a string representation of a coordinate system.

        """