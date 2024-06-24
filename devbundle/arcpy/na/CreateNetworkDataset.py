# Generated documentation for module arcpy.na


class CreateNetworkDataset(object):
    """
    Creates a network dataset in an existing feature dataset. The network dataset can be used to perform network analysis on the data in the feature dataset.
    """

    @property
    def description(self) -> str:
        return """

        CreateNetworkDataset_na(feature_dataset, out_name, source_feature_class_names;source_feature_class_names..., elevation_model)

        Creates a network dataset in an existing feature dataset. The network
        dataset can be used to perform network analysis on the data in the
        feature dataset.

     INPUTS:
      feature_dataset (Feature Dataset):
          The feature dataset where the network dataset will be created. The
          feature dataset should contain the source feature classes that will
          participate in the network dataset.If the feature dataset is in an
          enterprise geodatabase, the feature
          dataset and all source feature classes cannot be versioned.
      out_name (String):
          The name of the network dataset to be created. The feature_dataset
          parameter value and its parent geodatabase must not already contain a
          network dataset with this name.
      source_feature_class_names (String):
          The names of the feature classes to be included in the network dataset
          as network source features. Specify this parameter as a list of
          strings.You must choose at least one line feature class that is not a
          turn
          feature class. This line feature class will act as an edge source in
          the network dataset. You can optionally choose point feature classes
          to act as junction sources in the network dataset and turn feature
          classes to act as turn sources.All source feature classes must reside
          in the feature_dataset
          parameter value and must not already participate in a geometric
          network, a utility network, or another network dataset. Source feature
          classes cannot have 64-bit object identifier (OID) fields.
      elevation_model (String):
          Specifies the model that will be used to control vertical connectivity
          in the network dataset.ELEVATION_FIELDS-Coincident endpoints with the
          same elevation field
          values will be considered connected in the network dataset. This is
          the default.Z_COORDINATES-The z-coordinate values in the line feature
          geometry
          will be used to determine vertical connectivity. Coincident points are
          considered connected only if they have matching z-coordinate
          values.NO_ELEVATION-Network dataset connectivity will be determined
          only by
          horizontal coincidence.

        """