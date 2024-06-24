# Generated documentation for module arcpy.server


class UploadServiceDefinition(object):
    """
    Uploads and shares a web layer, locator, web tool, or service to ArcGIS Online, ArcGIS Enterprise, or ArcGIS Server.
    """

    @property
    def description(self) -> str:
        return """

        UploadServiceDefinition_server(in_sd_file, in_server, {in_service_name}, {in_cluster}, {in_folder_type}, {in_folder}, {in_startupType}, {in_override}, {in_my_contents}, {in_public}, {in_organization}, {in_groups;in_groups...})

        Uploads and shares a web layer, locator, web tool, or service to
        ArcGIS Online, ArcGIS Enterprise, or ArcGIS Server.

     INPUTS:
      in_sd_file (File):
          The service definition file (.sd) that contains all the information
          needed to share a web layer, web tool, or service.
      in_server (ServerConnection):
          The server type. The following server types are supported:
          My Hosted Services-Use when sharing a hosted web layer to ArcGIS
          Online or ArcGIS Enterprise. Enter My Hosted Services for the server
          connection. Capitalize the first letter of each word and include a
          space between each word.HOSTING_SERVER-Use when sharing a hosted web
          layer to ArcGIS Online or
          ArcGIS Enterprise.URL to the ArcGIS Enterprise portal federated
          server-Use when sharing
          a web tool or map image layer to an ArcGIS Enterprise portal federated
          server. ArcGIS Server connection-Use when sharing a map or
          geoprocessing service to ArcGIS Server. You can use ArcGIS Server
          connections listed under thenode in thewindow, or you can browse to a
          folder where server connection files are stored.
          ServersProjectURL to ArcGIS Server-Use when sharing a map or
          geoprocessing service
          to ArcGIS Server. You can specify the URL to ArcGIS Server provided a
          publisher connection to ArcGIS Server has been added to the ArcGIS Pro
          project, and you're opening the project in the script or you're
          running the tool in ArcGIS Pro.
      in_service_name {String}:
          The service name that will override the current service name specified
          in the service definition.
      in_cluster {String}:
          The cluster name that will override the current cluster to which the
          service has been assigned. You must choose from clusters on the
          specified server.
      in_folder_type {String}:
          Specifies the folder type that will be used to determine the source
          for the folder. The default is to get a folder from the service
          definition. You can also get a list of existing folders on the
          specified online server, or you can specify that a new folder be
          created once you share the web layer or service.NEW-A new folder will
          be created.EXISTING-An existing folder on the
          server will be used.FROM_SERVICE_DEFINITION-The folder in the service
          definition will be
          used. This is the default.
      in_folder {String}:
          The folder that will be used for the web layer or service. If no
          folder is provided, the folder specified in the service definition
          will be used. If you specified NEW for in_folder_type, use this
          parameter to provide a folder name. If you specified EXISTING for
          in_folder_type, you can choose from the existing folders on the
          server.
      in_startupType {Boolean}:
          Specifies whether the service will be started after
          sharing.STARTED-The service will be started after sharing. This is the
          default.STOPPED-The service will not be started after sharing.
      in_override {Boolean}:
          Specifies whether the sharing properties set in the service definition
          will be overridden. These properties define if, and how, you are
          sharing the web layer or web tool with ArcGIS Online or ArcGIS
          Enterprise. Sharing the web layer or web tool exposes it for others to
          use.OVERRIDE_DEFINITION-The sharing properties set in the service
          definition will be overridden.USE_DEFINITION-The sharing properties
          set in the service definition
          will not be overridden; they will be used. This is the default.You
          must be signed in to ArcGIS Online or ArcGIS Enterprise to
          override sharing properties.This parameter is not honored when sharing
          to ArcGIS Server.
      in_my_contents {Boolean}:
          Specifies whether web layers and web tools will be shared. All
          shared web layers and web tools are available through.
          Even if you only want to share with a specific group in your
          organization, the web layer or web tool will also be shared through.
          My ContentMy Content         SHARE_ONLINE-The web layer or web tool
          will be shared on
          ArcGIS Online or ArcGIS Enterprise. The web layer or web tool will be
          listed under. My ContentNO_SHARE_ONLINE-The web layer or web
          tool will not be shared on ArcGIS
          Online or ArcGIS Enterprise and will be inaccessible to other ArcGIS
          Online or ArcGIS Enterprise users and clients on the web. This is the
          default.You must be signed in to a portal to override sharing
          properties.This parameter is not honored when sharing to ArcGIS
          Server.
      in_public {Boolean}:
          Specifies whether the web layer or web tool will be available to the
          public.PUBLIC-The web layer or web tool will be available to the
          public.PRIVATE-The web layer or web tool will not be available to the
          public.
          This is the default.You must be signed in to ArcGIS Online or ArcGIS
          Enterprise to
          override sharing properties.This parameter is not honored when sharing
          to ArcGIS Server.
      in_organization {Boolean}:
          Specifies whether the web layer or web tool will be shared with your
          organization.SHARE_ORGANIZATION-The web layer or web tool will be
          shared with your
          organization.NO_SHARE_ORGANIZATION-The web layer or web tool will not
          be shared
          with your organization. This is the default.You must be signed in to
          ArcGIS Online or ArcGIS Enterprise to
          override sharing properties.This parameter is not honored when sharing
          to ArcGIS Server.
      in_groups {String}:
          A list of group names with which the web layer or web tool will be
          shared.You must be signed in to ArcGIS Online or ArcGIS Enterprise to
          override sharing properties.This parameter is not honored when sharing
          to ArcGIS Server.

        """