# Generated documentation for module arcpy.un


class DeleteRule(object):
    """
    Permanently deletes a rule from a utility network.
    """

    @property
    def description(self) -> str:
        return """

        DeleteRule_un(in_utility_network, rule_type, {rule_desc})

        Permanently deletes a rule from a utility network.

     INPUTS:
      in_utility_network (Utility Network / Utility Network Layer):
          The utility network for which the rule will be removed.
      rule_type (String):
          Specifies the type of rule that will be deleted.ALL-All rules will be
          deleted.JUNCTION_JUNCTION_CONNECTIVITY-A
          junction-junction connectivity
          association rule will be deleted.CONTAINMENT-A containment association
          rule will be deleted.STRUCTURAL_ATTACHMENT-A structural attachment
          association rule will be
          deleted.JUNCTION_EDGE_CONNECTIVITY-A junction-edge connectivity rule
          will be
          deleted.EDGE_JUNCTION_EDGE_CONNECTIVITY-An edge-junction-edge
          connectivity
          rule will be deleted.
      rule_desc {String}:
          Specifies the rule that will be removed, including the rule ID
          and the description of the rule. To find the rule ID,
          browse thesection on thetab on thedialog
          box. For more information, see View network rules.
          RulesNetwork PropertiesLayer Properties

        """