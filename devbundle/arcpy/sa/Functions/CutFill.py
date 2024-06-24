# Generated documentation for module arcpy.sa.Functions


class CutFill(object):
    """
    Calculates the volume change between two surfaces. This is typically used for cut and fill operations.
    """

    @property
    def description(self) -> str:
        return """

        CutFill_sa(in_before_surface, in_after_surface, {z_factor})

        Calculates the volume change between two surfaces. This is typically
        used for cut and fill operations.

     INPUTS:
      in_before_surface (Composite Geodataset):
          The input representing the surface before the cut or fill operation.
      in_after_surface (Composite Geodataset):
          The input representing the surface after the cut or fill operation.
      z_factor {Double}:
          The number of ground x,y units in one surface z-unit.The z-factor
          adjusts the units of measure for the z-units when they
          are different from the x,y units of the input surface. The z-values of
          the input surface are multiplied by the z-factor when calculating the
          final output surface.If the x,y units and z-units are in the same
          units of measure, the
          z-factor is 1. This is the default.If the x,y units and z-units are in
          different units of measure, the
          z-factor must be set to the appropriate factor or the results will be
          incorrect. For example, if the z-units are feet and the x,y units are
          meters, you would use a z-factor of 0.3048 to convert the z-units from
          feet to meters (1 foot = 0.3048 meter).

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster defining regions of cut and of fill.The values show
          the locations and amounts where the surface has been
          added to or removed from.

        """