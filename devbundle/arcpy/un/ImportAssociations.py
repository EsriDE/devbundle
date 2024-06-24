# Generated documentation for module arcpy.un


class ImportAssociations(object):
    """
    Imports associations from a comma-separated values file (.csv) into an existing utility network. This tool can be used in conjunction with the Export Associations tool.
    """

    @property
    def description(self) -> str:
        return """

        ImportAssociations_un(in_utility_network, association_type, csv_file)

        Imports associations from a comma-separated values file (.csv) into an
        existing utility network. This tool can be used in conjunction with
        the Export Associations tool.

     INPUTS:
      in_utility_network (Utility Network / Utility Network Layer):
          The utility network to which the associations will be imported.
      association_type (String):
          Specifies the type of association that will be imported.ALL-All
          association types will be
          imported.JUNCTION_JUNCTION_CONNECTIVITY-The junction-junction
          connectivity
          association type will be imported.CONTAINMENT-The containment
          association type will be imported.STRUCTURAL_ATTACHMENT-The structural
          attachment association type will
          be imported.JUNCTION_EDGE_FROM_CONNECTIVITY-The junction-edge
          connectivity (from
          side of edge) association type will be
          imported.JUNCTION_EDGE_MIDSPAN_CONNECTIVITY-The junction-edge
          connectivity
          (midspan) association type will be
          imported.JUNCTION_EDGE_TO_CONNECTIVITY-The junction-edge connectivity
          (to side
          of edge) association type will be imported.
      csv_file (File):
          The .csv file from which the associations will be imported.

        """