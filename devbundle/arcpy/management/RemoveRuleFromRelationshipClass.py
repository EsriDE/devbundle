# Generated documentation for module arcpy.management


class RemoveRuleFromRelationshipClass(object):
    """
    Removes a rule from a relationship class.
    """

    @property
    def description(self) -> str:
        return """

        RemoveRuleFromRelationshipClass_management(in_rel_class, {origin_subtype}, {destination_subtype}, {remove_all})

        Removes a rule from a relationship class.

     INPUTS:
      in_rel_class (Relationship Class):
          The relationship class with the rule to remove.
      origin_subtype {String}:
          If the origin class has subtypes, the subtype that is associated with
          the relationship class rule to be deleted.
      destination_subtype {String}:
          If the destination class has subtypes, the subtype that is associated
          with the relationship class rule to be deleted.
      remove_all {Boolean}:
          Specifies the relationship rules to be removed from the relationship
          class.REMOVE-All relationship rules will be removed from the input
          relationship class.NOT_ALL-Only rules from the origin and destination
          subtypes specified
          will be removed. This is the default.

        """