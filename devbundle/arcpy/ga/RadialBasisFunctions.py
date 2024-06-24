# Generated documentation for module arcpy.ga


class RadialBasisFunctions(object):
    """
    Uses one of five basis functions to interpolate a surfaces that passes through the input points exactly.
    """

    @property
    def description(self) -> str:
        return """

        RadialBasisFunctions_ga(in_features, z_field, {out_ga_layer}, {out_raster}, {cell_size}, {search_neighborhood}, {radial_basis_functions}, {small_scale_parameter})

        Uses one of five basis functions to interpolate a surfaces that passes
        through the input points exactly.

     INPUTS:
      in_features (Feature Layer):
          The input point features containing the z-values to be interpolated.
      z_field (Field):
          Field that holds a height or magnitude value for each point. This can
          be a numeric field or the Shape field if the input features contain
          z-values or m-values.
      cell_size {Analysis Cell Size}:
          The cell size at which the output raster will be created. This
          value can be explicitly set in theby theparameter.
          EnvironmentsCell SizeIf not set, it is the shorter of the width or the
          height of the extent
          of the input point features, in the input spatial reference, divided
          by 250.
      search_neighborhood {Geostatistical Search Neighborhood}:
          Defines which surrounding points will be used to control the output.
          Standard is the default.The following are Search Neighborhood classes:
          SearchNeighborhoodStandard and
          SearchNeighborhoodStandardCircular.StandardmajorSemiaxis-The major
          semiaxis value of the searching
          neighborhood.minorSemiaxis-The minor semiaxis value of the searching
          neighborhood.angle-The angle of rotation for the axis (circle) or
          semimajor axis
          (ellipse) of the moving window.nbrMax-The maximum number of neighbors
          that will be used to estimate
          the value at the unknown location.nbrMin-The minimum number of
          neighbors that will be used to estimate
          the value at the unknown location. sectorType-The geometry of
          the neighborhood.
          ONE_SECTOR-Single ellipse.FOUR_SECTORS-Ellipse divided into four
          sectors.FOUR_SECTORS_SHIFTED-Ellipse divided into four sectors and
          shifted 45
          degrees.EIGHT_SECTORS-Ellipse divided into eight sectors.Standard
          Circularradius-The length of the radius of the search circle.Angle-The
          angle
          of rotation for the axis (circle) or semimajor axis
          (ellipse) of the moving window.nbrMax-The maximum number of neighbors
          that will be used to estimate
          the value at the unknown location.nbrMin-The minimum number of
          neighbors that will be used to estimate
          the value at the unknown location. sectorType-The geometry of
          the neighborhood.
          ONE_SECTOR-Single ellipse.FOUR_SECTORS-Ellipse divided into four
          sectors.FOUR_SECTORS_SHIFTED-Ellipse divided into four sectors and
          shifted 45
          degrees.EIGHT_SECTORS-Ellipse divided into eight sectors.
      radial_basis_functions {String}:
          There are five radial basis functions
          available.THIN_PLATE_SPLINE-Thin-plate spline
          functionSPLINE_WITH_TENSION-
          Spline with tension functionCOMPLETELY_REGULARIZED_SPLINE-Completely
          regularized spline functionMULTIQUADRIC_FUNCTION-Multiquadric spline
          functionINVERSE_MULTIQUADRIC_FUNCTION-Inverse multiquadric spline
          function
      small_scale_parameter {Double}:
          Used to calculate the weights assigned to the points located in the
          moving window. Each of the radial basis functions has a parameter that
          controls the degree of small-scale variation of the surface. The
          (optimal) parameter is determined by finding the value that minimizes
          the root mean square prediction error (RMSPE).

     OUTPUTS:
      out_ga_layer {Geostatistical Layer}:
          The geostatistical layer produced. This layer is required output only
          if no output raster is requested.
      out_raster {Raster Dataset}:
          The output raster. This raster is required output only if no output
          geostatistical layer is requested.

        """