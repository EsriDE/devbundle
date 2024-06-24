# Generated documentation for module arcpy.nd


class AddConnectivityAssociationsRule(object):
    """
    Adds a diagram rule to automatically represent connectivity associations during the building of diagrams based on an existing template. This rule processes connectivity associations in which both the from and to junctions are currently represented in the diagrams.
    """

    @property
    def description(self) -> str:
        return """

        AddConnectivityAssociationsRule_nd(in_utility_network, template_name, is_active, {description})

        Adds a diagram rule to automatically represent connectivity
        associations during the building of diagrams based on an existing
        template. This rule processes connectivity associations in which both
        the from and to junctions are currently represented in the diagrams.

     INPUTS:
      in_utility_network (Utility Network / Trace Network):
          The utility network or trace network containing the diagram template
          that will be modified.
      template_name (String):
          The name of the diagram template that will be modified.
      is_active (Boolean):
          Specifies whether the rule will be enabled when generating and
          updating diagrams based on the specified template.ACTIVE-The added
          rule will become enabled during the generation and
          update of any diagrams based on the input template. This is the
          default.INACTIVE-The added rule will not become enabled during the
          generation
          or update of any diagrams based on the input template.
      description {String}:
          The description of the rule.

        """