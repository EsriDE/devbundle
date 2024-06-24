# Generated documentation for module arcpy.sa.Functions


class SnapPourPoint(object):
    """
    Snaps pour points to the cell of highest flow accumulation within a specified distance.
    """

    @property
    def description(self) -> str:
        return """

        SnapPourPoint_sa(in_pour_point_data, in_accumulation_raster, snap_distance, {pour_point_field})

        Snaps pour points to the cell of highest flow accumulation within a
        specified distance.

     INPUTS:
      in_pour_point_data (Composite Geodataset):
          The input pour point locations that are to be snapped.For a raster
          input, all cells that are not NoData (that is, have a
          value) will be considered pour points and will be snapped.For a point
          feature input, this specifies the locations of cells that
          will be snapped.
      in_accumulation_raster (Composite Geodataset):
          The input flow accumulation raster.This can be created with the Flow
          Accumulation tool.
      snap_distance (Double):
          Maximum distance, in map units, to search for a cell of higher
          accumulated flow.
      pour_point_field {Field}:
          The field used to assign values to the pour point locations. If
          the pour point dataset is a raster, use. ValueIf the pour point
          dataset is a feature, use a numeric field. If the
          field contains floating-point values, they will be truncated into
          integers.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output pour point raster where the original pour point locations
          have been snapped to locations of higher accumulated flow.This output
          is of integer type.

        """