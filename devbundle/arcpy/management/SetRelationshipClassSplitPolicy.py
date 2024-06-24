# Generated documentation for module arcpy.management


class SetRelationshipClassSplitPolicy(object):
    """
    Defines the split policy for related features.
    """

    @property
    def description(self) -> str:
        return """

        SetRelationshipClassSplitPolicy_management(in_rel_class, split_policy)

        Defines the split policy for related features.

     INPUTS:
      in_rel_class (Relationship Class):
          The relationship class on which the split policy will be set. The
          origin feature class must be a polyline or polygon feature class and
          the destination must be a nonspatial table.
      split_policy (String):
          Specifies the split policy to apply to the relationship
          class.DEFAULT_COMPOSITE-If the feature class split model is
          Delete/Insert/Insert, the relationships and the part objects will be
          deleted. If the feature class split model is Update/Insert, the
          relationships on the largest resulting feature will be preserved. This
          is the default split policy for composite relationship
          classes.DEFAULT_SIMPLE-The relationships on the largest resulting
          feature
          will be preserved. This is the default split policy for simple
          relationship classes.DUPLICATE_RELATED_OBJECTS-Copies of the related
          objects will be
          generated and assigned to both resulting parts. The relationship class
          must be Global ID based to use this split policy.

        """