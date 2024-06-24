# Generated documentation for module arcpy.un


class ImportRules(object):
    """
    Import connectivity, structural attachment, and containment rules from a comma-separated values file into an existing utility network.
    """

    @property
    def description(self) -> str:
        return """

        ImportRules_un(in_utility_network, rule_type, csv_file)

        Import connectivity, structural attachment, and containment rules from
        a comma-separated values file into an existing utility network.

     INPUTS:
      in_utility_network (Utility Network / Utility Network Layer):
          Specifies the utility network to import the rules to.
      rule_type (String):
          Specifies the type of rules to import.ALL-One or more types of
          rulesJUNCTION_JUNCTION_CONNECTIVITY-Junction-
          junction connectivity
          association rulesJUNCTION_EDGE_CONNECTIVITY-Junction-edge connectivity
          rulesCONTAINMENT-Containment association
          rulesSTRUCTURAL_ATTACHMENT-Structural attachment association
          rulesEDGE_JUNCTION_EDGE_CONNECTIVITY-Edge-junction-edge association
          rules
      csv_file (File):
          Specifies the .csv file containing the rules to import.

        """