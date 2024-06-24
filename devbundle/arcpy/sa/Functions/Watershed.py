# Generated documentation for module arcpy.sa.Functions


class Watershed(object):
    """
    Determines the contributing area above a set of cells in a raster.
    """

    @property
    def description(self) -> str:
        return """

        Watershed_sa(in_flow_direction_raster, in_pour_point_data, {pour_point_field})

        Determines the contributing area above a set of cells in a raster.

     INPUTS:
      in_flow_direction_raster (Composite Geodataset):
          The input raster that shows the direction of flow out of each cell.The
          flow direction raster can be created using the Flow Direction
          tool, run using the default flow direction type D8.
      in_pour_point_data (Composite Geodataset):
          The input pour point locations.For a raster, this represents cells
          above which the contributing area,
          or catchment, will be determined. All cells that are not NoData will
          be used as source cells.For a point feature dataset, this represents
          locations above which the
          contributing area, or catchment, will be determined.
      pour_point_field {Field}:
          The field used to assign values to the pour point locations. If
          the pour point dataset is a raster, use. ValueIf the pour point
          dataset is a feature, use a numeric field. If the
          field contains floating-point values, they will be truncated into
          integers.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster that shows the contributing area.This output is of
          integer type.

        """