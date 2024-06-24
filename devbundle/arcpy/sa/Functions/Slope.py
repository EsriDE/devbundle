# Generated documentation for module arcpy.sa.Functions


class Slope(object):
    """
    Identifies the slope (gradient or steepness) from each cell of a raster.
    """

    @property
    def description(self) -> str:
        return """

        Slope_sa(in_raster, {output_measurement}, {z_factor}, {method}, {z_unit}, {analysis_target_device})

        Identifies the slope (gradient or steepness) from each cell of a
        raster.

     INPUTS:
      in_raster (Composite Geodataset):
          The input surface raster.
      output_measurement {String}:
          Specifies the measurement units (degrees or percentages) of the output
          slope raster.DEGREE-The inclination of slope will be calculated in
          degrees.PERCENT_RISE-The inclination of slope will be calculated as
          percent
          rise, also referred to as the percent slope.
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
      method {String}:
          Specifies whether the calculation will be based on a planar (flat
          earth) or a geodesic (ellipsoid) method.PLANAR-The calculation will be
          performed on a projected flat plane
          using a 2D Cartesian coordinate system. This is the default
          method.GEODESIC-The calculation will be performed in a 3D Cartesian
          coordinate system by considering the shape of the earth as an
          ellipsoid.The planar method is appropriate to use on local areas in a
          projection
          that maintains correct distance and area. It is suitable for analyses
          that cover areas such cities, counties, or smaller states in area. The
          geodesic method produces a more accurate result, at the potential cost
          of an increase in processing time.
      z_unit {String}:
          Specifies the linear unit that will be used for vertical z-values.It
          is defined by a vertical coordinate system if it exists. If a
          vertical coordinate system does not exist, define the z-unit using the
          unit list to ensure correct geodesic computation. The default is
          meter.INCH-The linear unit will be inches.FOOT-The linear unit will be
          feet.YARD-The linear unit will be yards.MILE_US-The linear unit will
          be miles.NAUTICAL_MILE-The linear unit will be nautical
          miles.MILLIMETER-The linear unit will be millimeters.CENTIMETER-The
          linear unit will be centimeters.METER-The linear unit will be
          meters.KILOMETER-The linear unit will be kilometers.DECIMETER-The
          linear unit will be decimeters.
      analysis_target_device {String}:
          Specifies the device that will be used to perform the
          calculation.GPU_THEN_CPU-If a compatible GPU is found, it will be used
          to perform
          the calculation. Otherwise, the CPU will be used. This is the
          default.CPU_ONLY-The calculation will only be performed on the
          CPU.GPU_ONLY-The calculation will only be performed on the GPU.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output slope raster.It will be floating-point type.

        """