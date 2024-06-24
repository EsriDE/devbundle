# Generated documentation for module arcpy.cartography


class DisperseMarkers(object):
    """
    Finds point symbols that overlap or are too close to one another based on symbology at reference scale and spreads them apart based on a minimum spacing and dispersal pattern.
    """

    @property
    def description(self) -> str:
        return """

        DisperseMarkers_cartography(in_point_features, minimum_spacing, {dispersal_pattern})

        Finds point symbols that overlap or are too close to one another based
        on symbology at reference scale and spreads them apart based on a
        minimum spacing and dispersal pattern.

     INPUTS:
      in_point_features (Layer):
          The input point feature layer to be dispersed.
      minimum_spacing (Linear Unit):
          The minimum separation distance between individual point symbols in
          page units. A distance must be specified and must be greater than or
          equal to zero. When a positive value is specified, markers will be
          separated by that value; when a value of zero is specified, point
          symbols will touch. The default page unit is Points.
      dispersal_pattern {String}:
          Specifies the pattern that will be used to place the dispersed point
          symbols. A group of point symbols will have a center of mass derived
          from the locations of all points in the group. The center of mass is
          used as the anchor point around which the dispersal pattern
          operates.EXPANDED-The general pattern of the point symbols will be
          maintained
          as they are spread apart. Points that were exactly coincident will be
          dispersed to a circle around their center of mass. This is the
          default.RANDOM-Point symbols will be placed around the center of mass
          in a
          random dispersal that respects the minimum spacing.SQUARES-Point
          symbols will be placed in multiple square rings around
          the center of mass, ensuring that all points are placed as closely
          together as allowable by the minimum spacing parameter.RINGS-Point
          symbols will be placed in multiple circular rings around
          the center of mass, ensuring that all points are placed as closely
          together as allowable by the minimum spacing parameter.SQUARE-Point
          symbols will be placed evenly around the center of mass
          in a single square pattern.RING-Point symbols will be placed evenly
          around the center of mass in
          a single circular pattern.CROSS-Point symbols will be spaced evenly on
          horizontal and vertical
          axes originating from the center of mass.X_CROSS-Point symbols will be
          spaced evenly on 45° axes originating
          from the center of mass.COLUMN-Point symbols will be spaced evenly on
          a vertical axis
          originating from the center of mass.ROW-Point symbols will be spaced
          evenly on a horizontal axis
          originating from the center of mass.

        """