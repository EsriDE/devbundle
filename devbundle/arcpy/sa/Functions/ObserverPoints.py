# Generated documentation for module arcpy.sa.Functions


class ObserverPoints(object):
    """
    Identifies which observer points are visible from each raster surface location.
    """

    @property
    def description(self) -> str:
        return """

        ObserverPoints_sa(in_raster, in_observer_point_features, {z_factor}, {curvature_correction}, {refractivity_coefficient}, {out_agl_raster})

        Identifies which observer points are visible from each raster surface
        location.

     INPUTS:
      in_raster (Composite Geodataset):
          The input surface raster.
      in_observer_point_features (Composite Geodataset):
          The point feature class that identifies the observer locations.The
          maximum number of points allowed is 16.
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
      curvature_correction {Boolean}:
          Specifies whether correction for the earth's curvature will be
          applied.FLAT_EARTH-No curvature correction will be applied. This is
          the
          default.CURVED_EARTH-Curvature correction will be applied.
      refractivity_coefficient {Double}:
          The coefficient of the refraction of visible light in air.The default
          value is 0.13.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The output identifies exactly which observer points
          are visible from
          each raster surface location.
      out_agl_raster {Raster Dataset}:
          The output above ground level (AGL) raster.The AGL result is a raster
          where each cell value is the minimum height
          that must be added to an otherwise nonvisible cell to make it visible
          by at least one observer.Cells that were already visible will have a
          value of 0 in this output
          raster.

        """