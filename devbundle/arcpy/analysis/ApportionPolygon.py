# Generated documentation for module arcpy.analysis


class ApportionPolygon(object):
    """
    Summarizes the attributes of an input polygon layer based on the spatial overlay of a target polygon layer and assigns the summarized attributes to the target polygons. The target polygons have summed numeric attributes derived from the input polygons that each target overlaps. This process is typically known as apportioning or apportionment.
    """

    @property
    def description(self) -> str:
        return """

        ApportionPolygon_analysis(in_features, apportion_fields;apportion_fields..., target_features, out_features, method, {estimation_features}, {weight_field}, {maintain_geometries})

        Summarizes the attributes of an input polygon layer based on the
        spatial overlay of a target polygon layer and assigns the summarized
        attributes to the target polygons. The target polygons have summed
        numeric attributes derived from the input polygons that each target
        overlaps. This process is typically known as apportioning or
        apportionment.

     INPUTS:
      in_features (Feature Layer):
          The polygon features with numeric attributes that will be summarized
          into the target polygon geometries.
      apportion_fields (Field):
          The numeric fields from the input polygons that will be summarized by
          each target polygon and recorded in the output feature class.
      target_features (Feature Layer):
          The polygon features and their apportioned fields that will be copied
          to the output feature class.
      method (String):
          Specifies the method that will be used to apportion the fields from
          the input polygons to the target polygons.AREA-The amount that each
          input polygon contributes to the summarized
          values for each target feature will be determined by the area of
          overlap between the two features. If an input feature overlaps two
          target features by the same amount, the apportioned fields will be
          divided in two and contribute to both target features by half of the
          total value. This is the default.LENGTH-The attributes from the input
          features will be divided based on
          the percentage of how much of a line is within each target feature.
          Only the line intersecting the input feature is included in the
          calculation. The line outside the input feature is excluded. For
          example, if one target feature covers 750 meters of a line, and
          another target feature covers 250 meters of a line, 75% (750 / 1000)
          of the input feature's attribute values will be aggregated to the
          first target feature, and 25% (250 / 1000) of the input feature's
          attribute values will be aggregated to the second target
          feature.POINTS-The attributes from the input features will be divided
          based on
          the number of points inside each target feature overlapping an input
          feature. Points outside of the input feature are excluded. Optionally,
          a weight field can be specified so that the total weight of all points
          within each target feature will be used to determine how the input
          features' attribute values are divided. For example, if two target
          features overlap one input feature, and there are two points inside
          the first target feature and eight points inside the second target
          feature, 20% (2 / 10) of the input feature's attribute values will be
          aggregated to the first target feature, and 80% (8 / 10) of the input
          feature's attribute values will be aggregated to the second target
          feature.
      estimation_features {Feature Layer}:
          The input point or polyline features that will be used to estimate the
          percent of the input polygon apportion fields to apportion to the
          target polygon. This is the amount of the point or line within the
          intersection divided by the amount within the input feature to create
          a percentage.
      weight_field {Field}:
          A numeric field from the target polygon layer that will be used to
          adjust which target polygons receive larger apportioned values from
          the input polygons' fields to apportion. Targets with higher weight
          are apportioned a higher ratio of the field values.If estimation
          features are specified, the weight field will be a
          numeric field from the estimation features that will adjust the values
          apportioned to the target polygons intersecting the estimation
          features.
      maintain_geometries {Boolean}:
          Specifies whether the output feature class will maintain the original
          geometries from the target polygon layer.MAINTAIN_GEOMETRIES-The
          output feature class will maintain the
          original geometries of the target polygon layer. This is the
          default.INTERSECT_GEOMETRIES-The output feature class will be a
          geometric
          intersection of the target polygons and the input polygons. Only areas
          of the target polygons that overlap an input polygon will be included
          in the output.

     OUTPUTS:
      out_features (Feature Class):
          The output feature class containing the attribute and geometries of
          the target polygons as well as the specified apportion fields from the
          input polygons.

        """