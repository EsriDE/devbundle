# Generated documentation for module arcpy.management


class AddFeatureClassToTopology(object):
    """
    Adds a feature class to a topology.
    """

    @property
    def description(self) -> str:
        return """

        AddFeatureClassToTopology_management(in_topology, in_featureclass, xy_rank, z_rank)

        Adds a feature class to a topology.

     INPUTS:
      in_topology (Topology Layer):
          The topology to which the feature class will be added.
      in_featureclass (Feature Layer):
          The feature class that will be added to the topology. The feature
          class must be in the same feature dataset as the topology.
      xy_rank (Long):
          The relative degree of positional accuracy associated with vertices of
          features in the feature class versus those in other feature classes in
          the topology. The feature class with the highest accuracy receives a
          higher rank (lower number, for example, 1) than a feature class that
          is known to be less accurate.
      z_rank (Long):
          Feature classes that are z-aware have elevation values embedded in
          their geometry for each vertex. By setting a z rank, you can influence
          how vertices with accurate z-values are snapped or clustered with
          vertices that contain less accurate z measurements.

        """