# Generated documentation for module arcpy.locref


class CreateLRSIntersectionFromExistingDataset(object):
    """
    Registers an existing intersection feature class as an intersection.
    """

    @property
    def description(self) -> str:
        return """

        CreateLRSIntersectionFromExistingDataset_locref(parent_network, network_description_field, in_feature_class, intersection_id_field, intersection_name_field, route_id_field, feature_id_field, feature_class_name_field, from_date_field, to_date_field, intersecting_layers;intersecting_layers..., {consider_z}, {z_tolerance}, {measure_field})

        Registers an existing intersection feature class as an intersection.

     INPUTS:
      parent_network (Feature Layer):
          The network to which the intersection will be registered.
      network_description_field (Field):
          The field in the network layer that will be used to name the
          intersections with other intersecting layers.
      in_feature_class (Feature Layer):
          The input point feature class to be registered.
      intersection_id_field (Field):
          The ID field in the in_feature_class parameter value. The field must
          have a unique ID for each intersection for a time slice.
      intersection_name_field (Field):
          The field in the in_feature_class parameter value that is a
          concatenated field showing the descriptors for the route and the
          intersecting feature.
      route_id_field (Field):
          The field in the in_feature_class parameter value that contains the
          route ID for the LRS Network.
      feature_id_field (Field):
          The field in the in_feature_class parameter value that contains the ID
          for the intersecting feature.
      feature_class_name_field (Field):
          The field in the in_feature_class parameter value that contains the
          name of the feature class that participated in the intersection.
      from_date_field (Field):
          The from date field in the in_feature_class parameter value.
      to_date_field (Field):
          The to date field in the in_feature_class parameter value.
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
          intersections.CONSIDER_Z-Z-values will be used during generation of
          intersections.DO_NOT_CONSIDER_Z-Z-values will not be used during
          generation of
          intersections. This is the default.
      z_tolerance {Double}:
          The z-tolerance used to generate intersections.
      measure_field {Field}:
          The measure on the base route at the point of intersection.

        """