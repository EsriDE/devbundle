# Generated documentation for module arcpy.locref


class ModifyLRSIntersection(object):
    """
    Modifies the properties of an intersection feature class, such as fields and intersecting layers, that compose the intersection feature class and can be added or removed.
    """

    @property
    def description(self) -> str:
        return """

        ModifyLRSIntersection_locref(in_feature_class, {intersection_id_field}, {intersection_name_field}, {route_id_field}, {feature_id_field}, {feature_class_name_field}, {from_date_field}, {to_date_field}, {intersecting_layers;intersecting_layers...}, {measure_field})

        Modifies the properties of an intersection feature class, such as
        fields and intersecting layers, that compose the intersection feature
        class and can be added or removed.

     INPUTS:
      in_feature_class (Feature Layer):
          The input LRS intersection feature layer. This feature class cannot be
          a service.
      intersection_id_field {Field}:
          The field in theto use as the intersection unique ID field.
          Intersection Feature Class
      intersection_name_field {Field}:
          The concatenated field in thethat contains the descriptors for
          the route and the intersecting feature. Intersection Feature
          Class
      route_id_field {Field}:
          The field in thethat contains the unique route ID.
          Intersection Feature Class
      feature_id_field {Field}:
          The field in thethat contains the ID of the intersecting
          feature. Intersection Feature Class
      feature_class_name_field {Field}:
          The field in thethat contains the name of the feature class
          that participated in the intersection. Intersection Feature
          Class
      from_date_field {Field}:
          The field in thethat contains the from date of the route.
          Intersection Feature Class
      to_date_field {Field}:
          The field in thethat contains the to date of the route.
          Intersection Feature Class
      intersecting_layers {Value Table}:
          Thefields that compose the intersecting layer.
          Intersection Feature ClassIntersection Layer-The feature class that
          intersects the LRS
          Network.ID Field-The field in the intersecting layer used to uniquely
          identify
          the feature that intersects the network.Description Field-The field
          that provides the description, such as
          town or county name, of the intersecting feature.Name Separator-The
          name separator for the intersection, such as AND,
          INTERSECT, +, or |.
      measure_field {Field}:
          The field in thethat contains the measure on the base route at
          the point of intersection. Intersection Feature Class

        """