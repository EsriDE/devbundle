# Generated documentation for module arcpy.un


class ExportAssociations(object):
    """
    Exports associations from a utility network to a comma-separated- values file (.csv). This tool can be used in conjunction with the Import Associations tool.
    """

    @property
    def description(self) -> str:
        return """

        ExportAssociations_un(in_utility_network, association_type, out_csv_file)

        Exports associations from a utility network to a comma-separated-
        values file (.csv). This tool can be used in conjunction with the
        Import Associations tool.

     INPUTS:
      in_utility_network (Utility Network / Utility Network Layer):
          The utility network containing the associations to export.
      association_type (String):
          Specifies the type of association to export.ALL-All association types
          in the utility network will be exported to a
          .csv file.JUNCTION_JUNCTION_CONNECTIVITY-Connectivity associations
          allowing two
          junction subtypes to connect via a connectivity association (features
          are offset geometrically) will be exported to a .csv
          file.CONTAINMENT-The containment association type will be exported to
          a
          .csv file.STRUCTURAL_ATTACHMENT-The structural attachment association
          type will
          be exported to a .csv file.JUNCTION_EDGE_FROM_CONNECTIVITY-The
          junction-edge (from side of edge)
          connectivity association type will be exported to a .csv
          file.JUNCTION_EDGE_MIDSPAN_CONNECTIVITY-The junction-edge (midspan)
          connectivity association type will be exported to a .csv
          file.JUNCTION_EDGE_TO_CONNECTIVITY-The junction-edge (to side of edge)
          connectivity association type will be exported to a .csv file.

     OUTPUTS:
      out_csv_file (File):
          The name and location of the .csv file that will be generated.

        """