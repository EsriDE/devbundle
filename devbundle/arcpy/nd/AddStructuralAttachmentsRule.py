# Generated documentation for module arcpy.nd


class AddStructuralAttachmentsRule(object):
    """
    Adds a diagram rule to automatically represent structural attachments during diagram building based on an existing template. This rule applies to structural attachment associations in which both the attached network element and the structure element are currently represented in the diagrams.
    """

    @property
    def description(self) -> str:
        return """

        AddStructuralAttachmentsRule_nd(in_utility_network, template_name, is_active, {description})

        Adds a diagram rule to automatically represent structural attachments
        during diagram building based on an existing template. This rule
        applies to structural attachment associations in which both the
        attached network element and the structure element are currently
        represented in the diagrams.

     INPUTS:
      in_utility_network (Utility Network):
          The utility network containing the diagram template to modify.
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