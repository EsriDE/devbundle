# Generated documentation for module arcpy.sa.Functions


class Contour(object):
    """
    Creates a feature class of contours from a raster surface.
    """

    @property
    def description(self) -> str:
        return """

        Contour_sa(in_raster, out_polyline_features, contour_interval, {base_contour}, {z_factor}, {contour_type}, {max_vertices_per_feature})

        Creates a feature class of contours from a raster surface.

     INPUTS:
      in_raster (Composite Geodataset):
          The input surface raster.
      contour_interval (Double):
          The interval, or distance, between contour lines.This can be any
          positive number.
      base_contour {Double}:
          The base contour value.Contours are generated above and below this
          value as needed to cover
          the entire value range of the input raster. The default is zero.
      z_factor {Double}:
          The unit conversion factor used when generating contours. The default
          value is 1.The contour lines are generated based on the z-values in
          the input
          raster, which are often measured in units of meters or feet. With the
          default value of 1, the contours will be in the same units as the
          z-values of the input raster. To create contours in a unit other than
          that of the z-values, set an appropriate value for the z-factor. It is
          not necessary to have the ground x,y and surface z-units be consistent
          for this tool.For example, if the elevation values in the input raster
          are in feet,
          but you want the contours to be generated based on units of meters,
          set the z-factor to 0.3048 (1 foot = 0.3048 meter).For another
          example, consider an input raster in WGS84 geographic
          coordinates and elevation units of meters for which you want to
          generate contour lines every 100 feet with a base of 50 feet (so the
          contours will be 50 ft, 150 ft, 250 ft, and so on). To do this, set
          contour_interval to 100, base_contour to 50, and z_factor to 3.2808 (1
          meter = 3.2808 feet).
      contour_type {String}:
          Specifies the type of output. The output can represent the contours as
          either lines or polygons. There are several options for
          polygons.CONTOUR-A polyline feature class of contours (isolines). This
          is the
          default.CONTOUR_POLYGON-A polygon feature class of filled
          contours.CONTOUR_SHELL-A polygon feature class in which the upper
          bound of the
          polygon increases cumulatively by the interval value. The lower bound
          remains constant at the raster minimum.CONTOUR_SHELL_UP-A polygon
          feature class in which the lower bound of
          the polygon increases cumulatively, from the raster minimum, by the
          interval value. The upper bound remains constant at the raster
          maximum.
      max_vertices_per_feature {Long}:
          The vertex limit when subdividing a feature. This should only be used
          when output features contain a very large number of vertices (many
          millions).This parameter is intended as a way to subdivide extremely
          large
          features that can cause issues later on, for example, when storing,
          analyzing, or drawing the features.If left empty, the output features
          will not be split. The default is
          empty.

     OUTPUTS:
      out_polyline_features (Feature Class):
          The output contour features.

        """