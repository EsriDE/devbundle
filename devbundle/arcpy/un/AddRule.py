# Generated documentation for module arcpy.un


class AddRule(object):
    """
    Adds a network rule to a utility network.
    """

    @property
    def description(self) -> str:
        return """

        AddRule_un(in_utility_network, rule_type, from_class, from_assetgroup, from_assettype, to_class, to_assetgroup, to_assettype, {from_terminal}, {to_terminal}, {via_class}, {via_assetgroup}, {via_assettype}, {via_terminal})

        Adds a network rule to a utility network.

     INPUTS:
      in_utility_network (Utility Network / Utility Network Layer):
          The utility network for which the rule will be added.
      rule_type (String):
          Specifies the type of rule that will be
          created.JUNCTION_JUNCTION_CONNECTIVITY-A junction-junction
          connectivity rule
          will be created to allow point features or junction objects to connect
          through a connectivity association.CONTAINMENT-A containment rule will
          be created in which the from
          parameters are the container and the to parameters are the contents in
          a containment association.STRUCTURAL_ATTACHMENT-A structural
          attachment rule will be created in
          which the from parameters are the structure features or objects and
          the to parameters are the attachment features or objects in a
          structural attachment association.JUNCTION_EDGE_CONNECTIVITY-A
          junction-edge connectivity rule will be
          created to allow point and line features to connect through geometric
          coincidence (features are at the same x,y,z location), or allow an
          edge object to connect with point features or junction objects through
          a connectivity association.EDGE_JUNCTION_EDGE_CONNECTIVITY-An edge-
          junction-edge connectivity
          rule will be created to allow a line to connect to either side of a
          point feature, or allow an edge object to connect with another line or
          edge object through a point feature or junction object.
      from_class (String):
          The from utility network feature class or nonspatial object that will
          be included in the rule.Structural attachment and containment
          association rules require that
          the container or structure network feature be in this parameter.When
          creating junction-edge and edge-junction-edge connectivity rules,
          this parameter must reference the junction or junction object.
      from_assetgroup (String):
          An asset group for the from_class parameter value to which the rule
          will apply.
      from_assettype (String):
          An asset type for the from_class parameter value to which the rule
          will apply.
      to_class (String):
          The to utility network feature class or nonspatial object that will be
          included in the rule.Structural attachment and containment
          associations rules require that
          the content or attachment network feature be in this parameter.When
          creating junction-edge and edge-junction-edge connectivity rules,
          the from_class parameter must reference the junction or junction
          object..
      to_assetgroup (String):
          An asset group for the to_class parameter value to which the rule will
          apply.
      to_assettype (String):
          An asset type for the to_class parameter value to which the rule will
          apply.
      from_terminal {String}:
          The from terminal to which the rule will apply. This will be a
          terminal in the from_class parameter value. When creating a
          connectivity rule for a device or junction object with terminals to
          connect to another network feature, the terminal side to connect from
          must be specified, for example, the high-side terminal on a
          transformer.This parameter is required if the asset type has
          terminals. It is
          ignored for structural attachment or containment rule types.
      to_terminal {String}:
          The to terminal to which the rule will apply. This will be a terminal
          in the to_class parameter value. When creating a connectivity rule for
          a device or junction object to connect to another network feature with
          terminals, the terminal side to connect to must be specified, for
          example, the low-side terminal on a transformer.This parameter is
          required if the asset type has terminals. It is
          ignored for structural attachment or containment rule types.
      via_class {String}:
          The junction utility network feature class or table to which the rule
          will apply. This parameter can only be specified when the rule_type
          parameter is set to EDGE_JUNCTION_EDGE_CONNECTIVITY, since three
          classes are required to participate in edge-junction-edge
          connectivity.
      via_assetgroup {String}:
          An asset group of the via_class parameter value to which the rule will
          apply. This parameter can only be specified when the rule_type
          parameter is set to EDGE_JUNCTION_EDGE_CONNECTIVITY.
      via_assettype {String}:
          An asset type of the via_class parameter value to which the rule will
          apply. This parameter can only be specified when the rule_type
          parameter is set to EDGE_JUNCTION_EDGE_CONNECTIVITY.
      via_terminal {String}:
          The terminal from the via_class parameter value to which the rule will
          apply. This parameter can only be specified when the rule_type
          parameter is set to EDGE_JUNCTION_EDGE_CONNECTIVITY.

        """