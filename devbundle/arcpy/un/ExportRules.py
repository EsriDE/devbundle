# Generated documentation for module arcpy.un


class ExportRules(object):
    """
    Exports connectivity, structural attachment, and containment rules from a utility network into a comma-separated values file.
    """

    @property
    def description(self) -> str:
        return """

        ExportRules_un(in_utility_network, rule_type, out_csv_file)

        Exports connectivity, structural attachment, and containment rules
        from a utility network into a comma-separated values file.

     INPUTS:
      in_utility_network (Utility Network / Utility Network Layer):
          The utility network to export the rules from.
      rule_type (String):
          The type of rule to export.ALL-All the rules in the utility network
          will be
          exported.JUNCTION_JUNCTION_CONNECTIVITY-Junction-junction connectivity
          association rules will be
          exported.JUNCTION_EDGE_CONNECTIVITY-Junction-edge connectivity rules
          will be
          exported.CONTAINMENT-Containment association rules will be
          exported.STRUCTURAL_ATTACHMENT-Structural attachment association rules
          will be
          exported.EDGE_JUNCTION_EDGE_CONNECTIVITY-Edge-junction-edge
          connectivity
          association rules will be exported.

     OUTPUTS:
      out_csv_file (File):
          The folder location and name of the .csv file to be created.

        """