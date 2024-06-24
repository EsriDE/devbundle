# Generated documentation for module arcpy.transit


class ConnectPublicTransitDataModelToStreets(object):
    """
    Connects transit stops to street features for use in a transit-enabled network dataset. This tool creates the StopsOnStreets and StopConnectors feature classes defined by the Network Analyst public transit data model and is intended to be run as part of a larger workflow for creating a transit-network dataset described in Create and use a network dataset with public transit data.
    """

    @property
    def description(self) -> str:
        return """

        ConnectPublicTransitDataModelToStreets_transit(target_feature_dataset, in_streets_features, search_distance, {expression})

        Connects transit stops to street features for use in a transit-enabled
        network dataset. This tool creates the StopsOnStreets and
        StopConnectors feature classes defined by the Network Analyst public
        transit data model and is intended to be run as part of a larger
        workflow for creating a transit-network dataset described in Create
        and use a network dataset with public transit data.

     INPUTS:
      target_feature_dataset (Feature Dataset):
          The feature dataset where the transit-enabled network dataset will be
          created. This feature dataset must already exist and contain a point
          feature class called Stops with the schema described by the Network
          Analyst public transit data model. A valid Stops feature class can be
          created with the GTFS To Network Dataset Transit Sources tool.
          The Stops feature class may be altered after running the tool.
          Stop features with avalue of 2, representing station entrances, may be
          deleted. These stop features will instead be included in the output
          StopsOnStreets feature class to model correct connections from the
          streets, through the station entrances, and to the stops. Parent
          stations that are spatially coincident with stops may also be deleted.
          GStopType
      in_streets_features (Feature Layer):
          A polyline feature class of streets to which transit stops and lines
          will connect. This streets feature class should be the same feature
          class you intend to use in the transit-enabled network dataset for
          modeling pedestrians walking along streets. The feature class does not
          need to be in the target feature dataset to run this tool; however,
          the feature class must be in the target feature dataset at the time
          you create the network dataset.The input streets features will be
          altered after running the tool.
          Vertices will be added at the locations where StopsOnStreets features
          intersect the streets. If you do not want the street data altered,
          make a copy of it before running this tool.
      search_distance (Linear Unit):
          The search distance for snapping transit stops to the input street
          features. Stops that are outside the search distance will not be
          snapped and will not be connected to the streets. A small search
          distance will ensure that stops do not snap to streets that are far
          away, but it increases the likelihood of stops failing to snap when
          they should. A large search distance increases the number of stops
          likely to snap but may lead to errors that should instead be corrected
          by editing the street data. If no street features are found within the
          search distance of a particular stop, the output StopsOnStreets
          feature will not be snapped to a street and will be coincident with
          its corresponding feature in Stops, which could lead to poor
          connectivity in the network dataset at that location.The default is
          100 meters.
      expression {SQL Expression}:
          An SQL expression used to select a subset of input street feature
          records. Transit stops will be snapped only to street features
          matching this expression. For example, the expression can be used to
          prevent stops from snapping to streets where pedestrian travel is
          prohibited.

        """