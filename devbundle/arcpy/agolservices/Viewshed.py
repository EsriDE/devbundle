# Generated documentation for module arcpy.agolservices


class Viewshed(object):
    """
    Returns polygons of visible areas for a given set of input observation points.
    """

    @property
    def description(self) -> str:
        return """

        Viewshed_agolservices(InputPoints, {MaximumDistance}, {MaximumDistanceUnits}, {DEMResolution}, {ObserverHeight}, {ObserverHeightUnits}, {SurfaceOffset}, {SurfaceOffsetUnits}, {GeneralizeViewshedPolygons})

        Returns polygons of visible areas for a given set of input observation
        points.

     INPUTS:
      InputPoints (Feature Set):
          The point features to use as the observer locations.
      MaximumDistance {Double}:
          The maximum distance to calculate the viewshed.
      MaximumDistanceUnits {String}:
          Specifies the units for theparameter. Maximum
          DistanceMeters-The units are meters. This is the
          default.Kilometers-The units
          are kilometers.Feet-The units are feet.Yards-The units are
          yards.Miles-The units are miles.
      DEMResolution {String}:
          Specifies the approximate spatial resolution (cell size) of the source
          elevation data used for the calculation.The resolution keyword is an
          approximation of the spatial resolution
          of the digital elevation model. Many elevation sources are distributed
          in units of arc seconds; the keyword is an approximation in meters for
          easier understanding.FINEST-The finest units available for the extent
          are used.10m-The
          elevation source resolution is 1/3 arc second or approximately
          10 meters.24m-The elevation source is the Airbus WorldDEM4Ortho
          dataset at 24
          meters resolution.30m-The elevation source resolution is 1 arc second
          or approximately
          30 meters.90m-The elevation source resolution is 3 arc seconds or
          approximately
          90 meters. This is the default.
      ObserverHeight {Double}:
          The height above the surface of the observer. The default value of
          1.75 meters is an average height of a person. If you are looking from
          an elevated location such as an observation tower or a tall building,
          use that height instead.
      ObserverHeightUnits {String}:
          Specifies the units for theparameter. Observer
          HeightMeters-The units are meters. This is the default.Kilometers-The
          units
          are kilometers.Feet-The units are feet.Yards-The units are
          yards.Miles-The units are miles.
      SurfaceOffset {Double}:
          The height above the surface of the object you are viewing. The
          default value is 0. If you are viewing buildings or wind turbines, use
          their height.
      SurfaceOffsetUnits {String}:
          Specifies the units for theparameter. Surface
          OffsetMeters-The units are meters. This is the default.Kilometers-The
          units
          are kilometers.Feet-The units are feet.Yards-The units are
          yards.Miles-The units are miles.
      GeneralizeViewshedPolygons {Boolean}:
          Specifies whether the viewshed polygons will be generalized.The
          viewshed calculation is based on a raster elevation model that
          creates a result with stair-stepped edges. To create a more pleasing
          appearance and improve performance, the default behavior generalizes
          the polygons. This generalization will not change the accuracy of the
          result for any location more than one half of the DEM
          resolution.GENERALIZE-The viewshed polygons will be generalized. This
          is the
          default.NO_GENERALIZE-The viewshed polygons will not be generalized.

        """