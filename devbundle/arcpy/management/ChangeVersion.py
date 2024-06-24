# Generated documentation for module arcpy.management


class ChangeVersion(object):
    """
    Modifies the workspace of a layer or table view to connect to the specified version.
    """

    @property
    def description(self) -> str:
        return """

        ChangeVersion_management(in_features, version_type, {version_name}, {date}, {include_participating})

        Modifies the workspace of a layer or table view to connect to the
        specified version.

     INPUTS:
      in_features (Feature Layer / Table View / Topology Layer / Parcel Layer / Utility Network Layer / Trace Network Layer):
          The layer or table view that will connect to the specified version.The
          sublayers of a topology layer, parcel layer, utility network
          layer, or trace network layer are not valid inputs.
      version_type (String):
          Specifies the type of version to which the input feature layer will
          connect.TRANSACTIONAL-Connect to a defined state of the database
          (traditional
          version).HISTORICAL-Connect to a version representing a defined moment
          in time,
          often specified by a time or historical marker.BRANCH-Connect to a
          branch version.
      version_name {String}:
          The name of the version to which the input feature layer will connect.
          This parameter is optional if you're using a historical version.
      date {Date}:
          The date of the historical version to which the input feature layer
          will connect.
      include_participating {Boolean}:
          Specifies whether the workspace of participating classes will also
          change.The parameter is only applicable when the input layer is a
          topology
          layer, parcel layer, utility network layer, or trace network
          layer.INCLUDE-The version of the participating classes of the
          controller
          dataset will change if they are from the same workspace as the
          controller dataset.EXCLUDE-Only the version of the controller dataset
          will change.

        """