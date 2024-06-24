# Generated documentation for module arcpy.nd


class AddExpandContainerByAttributeRule(object):
    """
    Adds a diagram rule to the rule sequence specified on a diagram template to automatically expand container contents during diagram buildings. The containers to expand are filtered by attributes from a given container source class or object table.
    """

    @property
    def description(self) -> str:
        return """

        AddExpandContainerByAttributeRule_nd(in_utility_network, template_name, is_active, containers_visibility, container_source, {where_clause}, {description})

        Adds a diagram rule to the rule sequence specified on a diagram
        template to automatically expand container contents during diagram
        buildings. The containers to expand are filtered by attributes from a
        given container source class or object table.

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
      containers_visibility (Boolean):
          Specifies whether the containers stay visible after they are
          expanded.KEEP_VISIBLE-The containers will stay visible after they are
          expanded. This is the default.HIDE-The containers will be hidden
          after they are expanded.
      container_source (Table / Feature Class):
          The container source class or object table that references the
          containers to be expanded.
      where_clause {SQL Expression}:
          An SQL expression that will be used to select the subset of containers
          in the container source class or object table that will be expanded in
          the generated diagrams. For more information about SQL syntax, see SQL
          reference for query expressions used in ArcGIS.
      description {String}:
          The description of the rule.

        """