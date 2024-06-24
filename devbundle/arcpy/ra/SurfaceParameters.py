# Generated documentation for module arcpy.ra


class SurfaceParameters(object):
    """
    Determines parameters of a surface raster such as aspect, slope, and several types of curvatures using geodesic methods.
    """

    @property
    def description(self) -> str:
        return """

        SurfaceParameters_ra(inputSurfaceRaster, outputRasterName, {parameterType}, {localSurfaceType}, {neighborhoodDistance}, {useAdaptiveNeighborhood}, {zUnit}, {outputSlopeMeasurement}, {projectGeodesicAzimuths}, {useEquatorialAspect}, {inputAnalysisMask})

        Determines parameters of a surface raster such as aspect, slope, and
        several types of curvatures using geodesic methods.

     INPUTS:
      inputSurfaceRaster (Image Service / Raster Layer / String):
          The input surface raster. It can be integer or floating point type.
      outputRasterName (String):
          The name of the output raster service.
      parameterType {String}:
          Specifies the output surface parameter type that will be
          computed.SLOPE-The rate of change in elevation will be computed. This
          is the
          default.ASPECT-The downslope direction of the maximum rate of change
          for each
          cell will be computed.MEAN_CURVATURE-The overall curvature of the
          surface will be measured.
          It is computed as the average of the minimum and maximum curvature.
          This curvature describes the intrinsic convexity or concavity of the
          surface, independent of direction or gravity
          influence.TANGENTIAL_CURVATURE-The geometric normal curvature
          perpendicular to
          the slope line, tangent to the contour line will be measured. This
          curvature is typically applied to characterize the convergence or
          divergence of flow across the surface.PROFILE_CURVATURE-The geometric
          normal curvature along the slope line
          will be measured. This curvature is typically applied to characterize
          the acceleration and deceleration of flow down the
          surface.CONTOUR_CURVATURE-The curvature along contour lines will be
          measured.CONTOUR_GEODESIC_TORSION-The rate of change in slope angle
          along
          contour lines will be measured.GAUSSIAN_CURVATURE-The overall
          curvature of the surface will be
          measured. It is computed as the product of the minimum and maximum
          curvature.CASORATI_CURVATURE-The general curvature of the surface will
          be
          measured. It can be zero or any other positive number.
      localSurfaceType {String}:
          Specifies the type of surface function that will be fitted around the
          target cell.QUADRATIC-A quadratic surface function will be fitted to
          the
          neighborhood cells. This is the default.BIQUADRATIC-A biquadratic
          surface function will be fitted to the
          neighborhood cells.
      neighborhoodDistance {Linear Unit}:
          The output will be calculated over this distance from the target cell
          center. It determines the neighborhood size.The default value is the
          input raster cell size, resulting in a 3 by 3
          neighborhood.
      useAdaptiveNeighborhood {Boolean}:
          Specifies whether neighborhood distance will vary with landscape
          changes (adaptive). The maximum distance is determined by the
          neighborhood distance. The minimum distance is the input raster cell
          size.FIXED_NEIGHBORHOOD-A single (fixed) neighborhood distance will be
          used
          at all locations. This is the default.ADAPTIVE_NEIGHBORHOOD-An
          adaptive neighborhood distance will be used
          at all locations.
      zUnit {String}:
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
      outputSlopeMeasurement {String}:
          The measurement units (degrees or percentages) that will be used for
          the output slope raster. This parameter is only enabled when
          parameterType = "SLOPE".DEGREE-The inclination of slope will be
          calculated in
          degrees.PERCENT_RISE-The inclination of slope will be calculated as
          percent
          rise, also referred to as the percent slope.
      projectGeodesicAzimuths {Boolean}:
          Specifies whether geodesic azimuths will be projected to correct the
          angle distortion caused by the output spatial
          reference.GEODESIC_AZIMUTHS-Geodesic azimuths will not be projected.
          This is the
          default.PROJECT_GEODESIC_AZIMUTHS-Geodesic azimuths will be projected.
      useEquatorialAspect {Boolean}:
          Specifies whether aspect will be measured from a point on the equator
          or from the north pole.NORTH_POLE_ASPECT-Aspect will be measured from
          the north pole. This is
          the default.EQUATORIAL_ASPECT-Aspect will be measured from a point on
          the equator.
      inputAnalysisMask {Image Service / Feature Layer / Raster Layer / String}:
          The input data defining the locations where the analysis will
          occur.This can be an image service or a feature service. If the input
          is an
          image service, it can be integer or floating-point type. If the input
          is a feature service, it can be point, line, or polygon type.When the
          input mask data is an image service, the analysis will occur
          at locations that have a valid value, including zero. Cells that are
          NoData in the mask input will be NoData in the output.

        """