# Generated documentation for module arcpy.sa.Functions


class Aspect(object):
    """
    Derives the aspect from each cell of a raster surface.
    """

    @property
    def description(self) -> str:
        return """

        Aspect_sa(in_raster, {method}, {z_unit}, {project_geodesic_azimuths}, {analysis_target_device})

        Derives the aspect from each cell of a raster surface.

     INPUTS:
      in_raster (Composite Geodataset):
          The input surface raster.
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
      project_geodesic_azimuths {Boolean}:
          Specifies whether geodesic azimuths will be projected to correct the
          angle distortion caused by the output spatial
          reference.GEODESIC_AZIMUTHS-Geodesic azimuths will not be projected.
          This is the
          default.PROJECT_GEODESIC_AZIMUTHS-Geodesic azimuths will be projected.
      analysis_target_device {String}:
          Specifies the device that will be used to perform the
          calculation.GPU_THEN_CPU-If a compatible GPU is found, it will be used
          to perform
          the calculation. Otherwise, the CPU will be used. This is the
          default.CPU_ONLY-The calculation will only be performed on the
          CPU.GPU_ONLY-The calculation will only be performed on the GPU.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output aspect raster.It will be floating-point type.

        """