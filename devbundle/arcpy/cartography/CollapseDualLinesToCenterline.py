# Generated documentation for module arcpy.cartography


class CollapseDualLinesToCenterline(object):
    """
    Derives centerlines from dual-line (double-line) features, such as road casings, based on specified width tolerances.
    """

    @property
    def description(self) -> str:
        return """

        CollapseDualLinesToCenterline_cartography(in_features, out_feature_class, maximum_width, {minimum_width})

        Derives centerlines from dual-line (double-line) features, such as
        road casings, based on specified width tolerances.

     INPUTS:
      in_features (Feature Layer):
          The input dual-line features, such as road casings, from which
          centerlines will be derived.
      maximum_width (Linear Unit):
          The maximum width of the dual-line features that will be used to
          derive a centerline. A value must be specified, and it must be greater
          than zero. You can specify a unit; the default is the feature unit.
      minimum_width {Linear Unit}:
          The minimum width of the dual-line features that will be used to
          derive a centerline. The minimum width must be greater than or equal
          to zero, and it must be less than the maximum width. The default value
          is zero. You can specify a unit; the default is the feature unit.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class that will be created.

        """