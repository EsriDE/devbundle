# Generated documentation for module arcpy.nd


class AddStartIterationRule(object):
    """
    Adds a diagram rule to specify the beginning of a rule sequence during diagram building based on an existing template.
    """

    @property
    def description(self) -> str:
        return """

        AddStartIterationRule_nd(in_utility_network, template_name, is_active, {description})

        Adds a diagram rule to specify the beginning of a rule sequence during
        diagram building based on an existing template.

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