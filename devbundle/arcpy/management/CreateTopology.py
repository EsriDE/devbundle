# Generated documentation for module arcpy.management


class CreateTopology(object):
    """
    Creates a topology. The topology will not contain any feature classes or rules.
    """

    @property
    def description(self) -> str:
        return """

        CreateTopology_management(in_dataset, out_name, {in_cluster_tolerance})

        Creates a topology. The topology will not contain any feature classes
        or rules.

     INPUTS:
      in_dataset (Feature Dataset):
          The feature dataset in which the topology will be created.
      out_name (String):
          The name of the topology to be created. This name must be unique
          across the entire geodatabase.
      in_cluster_tolerance {Double}:
          The cluster tolerance to be set on the topology. The larger the value,
          the more likely vertices will be to cluster together.

        """