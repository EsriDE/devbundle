# Generated documentation for module arcpy.nd


class AddDiagramFeatureCapabilityByCategoryRule(object):
    """
    Adds a diagram rule to assign a particular capability to diagram features according to network categories. This assignment occurs during the building of diagrams based on an existing template. This capability is used by other rules that are run later in the rule sequence. The diagram features that will be processed depend on whether they are tagged with specific network categories.
    """

    @property
    def description(self) -> str:
        return """

        AddDiagramFeatureCapabilityByCategoryRule_nd(in_utility_network, template_name, is_active, inverse_category_selection, category;category..., capability, {description})

        Adds a diagram rule to assign a particular capability to diagram
        features according to network categories. This assignment occurs
        during the building of diagrams based on an existing template. This
        capability is used by other rules that are run later in the rule
        sequence. The diagram features that will be processed depend on
        whether they are tagged with specific network categories.

     INPUTS:
      in_utility_network (Utility Network):
          The utility network containing the diagram template that will be
          modified.
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
      inverse_category_selection (String):
          Specifies how the network features or network objects that are tagged
          with the specified network categories will be
          processed.EXCLUDE_CATEGORIES-The network features or network objects
          that are
          tagged with the specified categories will not be processed, while
          other network features and network objects will be processed. This is
          the default.INCLUDE_CATEGORIES-The network features or network objects
          that are
          tagged with the specified categories will be processed.
      category (String):
          The network categories that will be excluded or included depending on
          the inverse_category_selection parameter value.If the
          inverse_category_selection parameter is set to
          INCLUDE_CATEGORIES, one or more network categories must be specified.
          The specified capability will be assigned to any diagram features that
          are related to network features and network objects that are tagged
          with the specified network categories.If the
          inverse_category_selection parameter is set to
          EXCLUDE_CATEGORIES, the specified capability will be assigned to any
          diagram features that are related to network features and network
          objects that are not tagged with the specified network categories.
      capability (String):
          Specifies the capability that will be assigned to the diagram features
          filtered out by categories at the end of the rule operation. The
          specified capability will be used by other rules that run later in the
          rule sequence.PREVENT_TO_COLLAPSE_CONTAINER-All features filtered out
          by categories
          will be flagged to prevent their related container from being
          collapsed by Collapse Container rules that run later in the rule
          sequence. This is the default.ALLOW_TO_COLLAPSE_CONTAINER-All
          features filtered out by categories
          will be flagged to allow their related container to be collapsed by
          Collapse Container rules that run later in the rule
          sequence.PREVENT_TO_REDUCE_JUNCTION-All junctions filtered out by
          categories
          will be flagged to prevent reduction by Reduce Junction rules that run
          later in the rule sequence.ALLOW_TO_REDUCE_JUNCTION-All junctions
          filtered out by categories
          will be flagged to allow reduction by Reduce Junction rules that run
          later in the rule sequence.
      description {String}:
          The description of the rule.

        """