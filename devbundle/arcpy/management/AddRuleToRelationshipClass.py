# Generated documentation for module arcpy.management


class AddRuleToRelationshipClass(object):
    """
    Adds a rule to a relationship class.
    """

    @property
    def description(self) -> str:
        return """

        AddRuleToRelationshipClass_management(in_rel_class, {origin_subtype}, {origin_minimum}, {origin_maximum}, {destination_subtype}, {destination_minimum}, {destination_maximum})

        Adds a rule to a relationship class.

     INPUTS:
      in_rel_class (Relationship Class):
          The relationship class to which a rule will be added.
      origin_subtype {String}:
          Specifies the subtype of the origin class. If the origin class has
          subtypes, choose the subtype to which you want to associate a
          relationship class rule. If the origin class has no subtypes, the
          relationship rule will apply to all features.
      origin_minimum {Long}:
          Specifies the minimum range cardinality for the origin class if the
          relationship class is many-to-many.
      origin_maximum {Long}:
          Specifies the maximum range cardinality for the origin class if the
          relationship class is many-to-many or one-to-many.
      destination_subtype {String}:
          Specifies the subtype of the destination class. If the destination
          class has subtypes, choose the subtype to which you want to associate
          a relationship class rule. If the destination class has no subtypes,
          the relationship rule will apply to all features.
      destination_minimum {Long}:
          Specifies the minimum range cardinality for the destination class if
          the relationship class is many-to-many or one-to-many.
      destination_maximum {Long}:
          Specifies the maximum range cardinality for the destination class if
          the relationship class is many-to-many or one-to-many.

        """