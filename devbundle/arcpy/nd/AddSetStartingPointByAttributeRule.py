# Generated documentation for module arcpy.nd


class AddSetStartingPointByAttributeRule(object):
    """
    Adds a diagram rule to a diagram template to set diagram features currently represented in the diagram as starting points for tracing rules. The diagram features are queried from a given network source class or object table and can be filtered by their attributes.
    """

    @property
    def description(self) -> str:
        return """

        AddSetStartingPointByAttributeRule_nd(in_utility_network, template_name, is_active, network_source, {where_clause}, {junction_terminals;junction_terminals...}, {description})

        Adds a diagram rule to a diagram template to set diagram features
        currently represented in the diagram as starting points for tracing
        rules. The diagram features are queried from a given network source
        class or object table and can be filtered by their attributes.

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
          or objects that will be set as starting points.
      where_clause {SQL Expression}:
          An SQL expression to select the subset of features or objects in the
          specified source class or object table that will be set as starting
          points. For more information on SQL syntax, see SQL reference for
          query expressions used in ArcGIS.
      junction_terminals {Long}:
          The terminal IDs that will start tracing if the network source class
          or object table references junctions with terminals. The
          terminal IDs are all listed in thesection on thetab.
          Terminal ConfigurationsNetwork PropertiesWhen both the where_clause
          and junction_terminals parameters are
          configured, the specified terminals must correspond to queried
          features or objects; otherwise, no starting points will be set.
      description {String}:
          The description of the rule.

        """