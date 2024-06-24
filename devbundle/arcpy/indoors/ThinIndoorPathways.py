# Generated documentation for module arcpy.indoors


class ThinIndoorPathways(object):
    """
    Removes preliminary network pathways that are not needed for routing between selected locations on each level, reducing the network dataset size and improving its route-solving performance.
    """

    @property
    def description(self) -> str:
        return """

        ThinIndoorPathways_indoors(in_level_features, in_pathway_features, in_transition_features, routable_locations;routable_locations..., target_pathways, target_transitions, {search_tolerance}, {neighbor_solve_count})

        Removes preliminary network pathways that are not needed for routing
        between selected locations on each level, reducing the network dataset
        size and improving its route-solving performance.

     INPUTS:
      in_level_features (Feature Layer):
          The input polygon features representing a level or levels in one or
          more facilities. In the ArcGIS Indoors Information Model, this is the
          Levels layer. Only the levels represented by these features will be
          processed.
      in_pathway_features (Feature Layer):
          The input polyline features representing the preliminary pathways to
          be thinned. In the Indoors model, this is the PrelimPathways layer.
      in_transition_features (Feature Layer):
          The input polyline features representing the preliminary transitions
          to be thinned. In the Indoors model, this is the PrelimTransitions
          layer.
      routable_locations (Feature Layer):
          The input point or polygon features representing the locations used to
          calculate routes. This can be any point or polygon features that
          conform to the Indoors model or are configured as floor aware.
      target_pathways (Feature Layer):
          The existing feature class or feature layer to which the thinned
          pathways will be added. In the Indoors model, this is the Pathways
          layer.
      target_transitions (Feature Layer):
          The existing feature class or feature to which thinned transitions
          will be added. In the Indoors model, this is the Transitions layer.
      search_tolerance {Long}:
          The distance, in meters, the tool will search forfeatures near
          the input pathways. Thefeatures that are farther away than this value
          will not be used for thinning. The default value is 5. Routable
          LocationsRoutable LocationsThe value must be 0 or greater.
      neighbor_solve_count {Long}:
          The number of closest neighboring locations that will be
          solved when calculating routes between a specified location and other
          routable locations in the facility. The default value is 50.
          The value must be 1 or greater.

        """