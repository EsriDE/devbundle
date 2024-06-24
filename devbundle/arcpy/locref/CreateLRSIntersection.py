# Generated documentation for module arcpy.locref


class CreateLRSIntersection(object):
    """
    Creates an intersection feature class for an existing LRS Network.
    """

    @property
    def description(self) -> str:
        return """

        CreateLRSIntersection_locref(parent_network, network_description_field, intersection_feature_class_name, intersecting_layers;intersecting_layers..., {consider_z}, {z_tolerance})

        Creates an intersection feature class for an existing LRS Network.

     INPUTS:
      parent_network (Feature Layer):
          The network to which the intersection will be registered.
      network_description_field (Field):
          The field in the network layer that will be used to name the
          intersections with other intersecting layers.
      intersection_feature_class_name (String):
          The name of the new intersection point feature class.
      intersecting_layers (Value Table):
          The feature class that intersects the LRS Network and contains the
          following information:Intersection Layer-The feature class that
          intersects the LRS
          Network.ID Field-The field in the intersecting layer used to uniquely
          identify
          the feature that intersects the network.Description Field-The field
          that provides the description, such as
          town or county name, of the intersecting feature.Name Separator-The
          name separator for the intersection, such as AND,
          INTERSECT, +, or |.
      consider_z {Boolean}:
          Specifies whether z-values will be used when generating
          intersections.CONSIDER_Z-Z-values will be used when generating
          intersections.DO_NOT_CONSIDER_Z-Z-values will not be used when
          generating
          intersections. This is the default.
      z_tolerance {Double}:
          The z-tolerance that will be used to generate intersections.

        """