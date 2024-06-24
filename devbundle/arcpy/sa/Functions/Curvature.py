# Generated documentation for module arcpy.sa.Functions


class Curvature(object):
    """
    Calculates the curvature of a raster surface, optionally including profile and plan curvature.
    """

    @property
    def description(self) -> str:
        return """

        Curvature_sa(in_raster, {z_factor}, {out_profile_curve_raster}, {out_plan_curve_raster})

        Calculates the curvature of a raster surface, optionally including
        profile and plan curvature.

     INPUTS:
      in_raster (Composite Geodataset):
          The input surface raster.
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
      out_curvature_raster (Raster Dataset):
          The output curvature raster.It will be floating-point type.
      out_profile_curve_raster {Raster Dataset}:
          Output profile curve raster dataset.This is the curvature of the
          surface in the direction of slope.It will be floating-point type.
      out_plan_curve_raster {Raster Dataset}:
          Output plan curve raster dataset.This is the curvature of the surface
          perpendicular to the slope
          direction.It will be floating-point type.

        """