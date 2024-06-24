# Generated documentation for module arcpy.cartography


class SimplifyBuilding(object):
    """
    Simplifies the boundary or footprint of building polygons while maintaining their essential shape and size.
    """

    @property
    def description(self) -> str:
        return """

        SimplifyBuilding_cartography(in_features, out_feature_class, simplification_tolerance, {minimum_area}, {conflict_option}, {in_barriers;in_barriers...}, {collapsed_point_option})

        Simplifies the boundary or footprint of building polygons while
        maintaining their essential shape and size.

     INPUTS:
      in_features (Feature Layer):
          The building polygons to be simplified.
      simplification_tolerance (Linear Unit):
          The tolerance for building simplification. A tolerance must be
          specified, and it must be greater than zero. You can choose a
          preferred unit; the default is the feature unit.
      minimum_area {Areal Unit}:
          The minimum area for a simplified building to be retained in feature
          units. The default value is zero, that is, to keep all buildings. You
          can specify a preferred unit; the default is the feature unit.
      conflict_option {Boolean}:
          Specifies whether spatial conflicts-that is, overlapping or
          touching among buildings-will be identified. Afield is added to the
          output to store conflict flags. A value of 0 means no conflict; a
          value of 1 means conflict. SimBldFlagNO_CHECK-Spatial conflicts
          will not be identified; the resulting
          buildings may overlap. This is the default.CHECK_CONFLICTS-Spatial
          conflicts will be identified and the
          conflicting buildings will be flagged.
      in_barriers {Feature Layer}:
          The input layers containing features to act as barriers for
          simplification. Resulting simplified buildings will not touch or cross
          barrier features. For example, when simplifying buildings, the
          resulting simplified building areas do not cross road features defined
          as barriers.
      collapsed_point_option {Boolean}:
          Specifies whether an output point feature class will be created to
          store the centers of any buildings that are removed because they are
          smaller than the minimum_area parameter value. The point output is
          derived, is named the same as the output feature class specified in
          the out_feature_class parameter but with a _Pnt suffix, and is located
          in the same folder.KEEP_COLLAPSED_POINTS-A derived output point
          feature class will be
          created to store the centers of buildings that are removed.NO_KEEP-An
          output point feature class will not be created. This is
          the default.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class to be created.

        """