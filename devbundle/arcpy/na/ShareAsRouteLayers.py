# Generated documentation for module arcpy.na


class ShareAsRouteLayers(object):
    """
    Shares the results of network analyses as route layer items in a portal. A route layer includes all the information for a route such as the stops assigned to the route or the orders serviced by a route, as well as the travel directions.
    """

    @property
    def description(self) -> str:
        return """

        ShareAsRouteLayers_na(in_network_analysis_layer, {summary}, {tags}, {route_name_prefix}, {portal_folder_name}, {share_with}, {groups;groups...})

        Shares the results of network analyses as route layer items in a
        portal. A route layer includes all the information for a route such as
        the stops assigned to the route or the orders serviced by a route, as
        well as the travel directions.

     INPUTS:
      in_network_analysis_layer (File / Network Analyst Layer):
          The network analysis layer from which the route layer items will be
          created. The network analysis layer should already be solved.Route,
          Closest facility, Vehicle routing problem, and Last mile
          delivery network analysis layers are supported as valid inputs to this
          parameter.The input can also be a .zip file containing route data
          created by the
          saveRouteData() method of the arcpy.nax solver result objects or the
          service parameter in the REST API that return a zipped geodatabase of
          route data with the correct schema.
      summary {String}:
          The summary that will be used by the route layer items. The summary is
          displayed as part of the item information for the route layer item. If
          no value is provided, default summary text-Route and directions for
          <route name>-is used in which <route name> is replaced with the name
          of the route represented by the route layer.
      tags {String}:
          The tags that will be used to describe and identify the route layer
          items. Individual tags are separated with commas. The route name is
          always included as a tag even when no other value is provided.
      route_name_prefix {String}:
          A qualifier that will be added to the title of every route layer item.
          For example, a route name prefix of Monday morning deliveries can be
          used to group all route layer items created from a route analysis
          performed by deliveries that will be run on Monday morning. If no
          value is specified, the title of the route layer item will be created
          using only the route name.
      portal_folder_name {String}:
          The folder in your personal online workspace where the route layer
          items will be created. If a folder with the provided name does not
          exist, a folder will be created. If a folder with the provided name
          exists, the items will be created in the existing folder. If no value
          is provided, the route layer items will be created in the root folder
          of your online workspace.
      share_with {String}:
          Specifies who can access the route layer items.EVERYBODY-The route
          layer items will be public and can be accessed by
          anyone with the URL to the items.MYCONTENT-The route layer items will
          only be shared with the owner of
          the item (the user connected to the portal when the tool is run). As a
          result, only the item owner can access the route layers. This is the
          default.MYGROUPS-The route layer items will be shared with groups the
          connected user belongs to and its members. The groups are specified
          using the groups parameter.MYORGANIZATION-The route layer items will
          be shared with all
          authenticated users in your organization.
      groups {String}:
          The list of groups with which the route layer items will be shared.
          This parameter is applicable only when the share_with parameter is set
          to MYGROUPS.

        """