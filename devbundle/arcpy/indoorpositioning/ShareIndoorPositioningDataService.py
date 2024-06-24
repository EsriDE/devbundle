# Generated documentation for module arcpy.indoorpositioning


class ShareIndoorPositioningDataService(object):
    """
    Publishes an Indoor Positioning Data Service to ArcGIS Enterprise or ArcGIS Online. An Indoor Positioning Data Service contains the data required for enabling indoor positioning. It is used by the IndoorsLocationDataSource objects of the ArcGIS Maps SDKs to compute an estimated position.
    """

    @property
    def description(self) -> str:
        return """

        ShareIndoorPositioningDataService_indoorpositioning(in_ips_datasets, ips_dataset_name, title, {summary}, {tags}, {folder}, {sharing_level}, {group_sharing;group_sharing...})

        Publishes an Indoor Positioning Data Service to ArcGIS Enterprise or
        ArcGIS Online. An Indoor Positioning Data Service contains the data
        required for enabling indoor positioning. It is used by the
        IndoorsLocationDataSource objects of the ArcGIS Maps SDKs to compute
        an estimated position.

     INPUTS:
      in_ips_datasets (Feature Layer):
          The feature class from the ArcGIS IPS Data Model containing one
          feature per Indoor Positioning Dataset.
      ips_dataset_name (String):
          The name of the Indoor Positioning Dataset. Options will be a list of
          dataset names derived from the in_ips_datasets parameter value.
      title (String):
          The title of the Indoor Positioning Data Service.
      summary {String}:
          A short description for the Indoor Positioning Data Service.
      tags {String}:
          The keywords or terms that describe the Indoor Positioning Data
          Service. Separate multiple tags with a comma.
      folder {String}:
          The name of an existing folder on the portal to store the Indoor
          Positioning Data Service.
      sharing_level {String}:
          Specifies the sharing permissions that will be used for the
          service.OWNER-Only the owner of the Indoor Positioning Data Service
          will have
          access. This is the default.ORGANIZATION-All members of the
          organization will have access.EVERYONE-Everyone, including people
          outside the organization, will
          have access.
      group_sharing {String}:
          The groups with which the Indoor Positioning Data Service will be
          shared. You can select multiple values from the groups to which you
          belong.

        """