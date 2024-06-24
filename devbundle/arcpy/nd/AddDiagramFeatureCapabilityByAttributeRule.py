# Generated documentation for module arcpy.nd


class AddDiagramFeatureCapabilityByAttributeRule(object):
    """
    Adds a diagram rule to the rule sequence specified on a diagram template to assign a particular capability on diagram features currently represented in the diagram during diagram buildings. This capability is used by other rules run later in the rule sequence. The diagram features that will be processed are queried from a network source class or object table by attributes.
    """

    @property
    def description(self) -> str:
        return """

        AddDiagramFeatureCapabilityByAttributeRule_nd(in_utility_network, template_name, is_active, network_source, where_clause, capability, {description})

        Adds a diagram rule to the rule sequence specified on a diagram
        template to assign a particular capability on diagram features
        currently represented in the diagram during diagram buildings. This
        capability is used by other rules run later in the rule sequence. The
        diagram features that will be processed are queried from a network
        source class or object table by attributes.

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
      network_source (Table / Feature Class):
          The network source class or object table that references the features
          or objects associated with the diagram features to which the
          particular capability will be assigned.
      where_clause (SQL Expression):
          An SQL expression that will be used to filter out the features or
          objects of interest among the specified network source feature class
          or objet table. For more information about SQL syntax, see SQL
          reference for query expressions used in ArcGIS.
      capability (String):
          Specifies the capability that will be assigned to the queried diagram
          features at the end of the rule operation. This capability will be
          used by other rules run later in the rule
          sequence.PREVENT_TO_COLLAPSE_CONTAINER-All queried features will be
          flagged to
          prevent their related container from being collapsed by Collapse
          Container rules run later in the rule sequence. This is the
          default.ALLOW_TO_COLLAPSE_CONTAINER-All queried features will be
          flagged to
          allow their related container to be collapsed by Collapse Container
          rules run later in the rule sequence.PREVENT_TO_REDUCE_JUNCTION-All
          queried junctions will be flagged to
          prevent reduction by Reduce Junction rules run later in the rule
          sequence.ALLOW_TO_REDUCE_JUNCTION-All queried junctions will be
          flagged to
          allow reduction by Reduce Junction rules run later in the rule
          sequence.
      description {String}:
          The description of the rule.

        """