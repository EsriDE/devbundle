# Generated documentation for module arcpy.management


class SharePackage(object):
    """
    Shares a package by uploading it to ArcGIS Online or ArcGIS Enterprise.
    """

    @property
    def description(self) -> str:
        return """

        SharePackage_management(in_package, username, password, {summary}, {tags}, {credits}, {public}, {groups;groups...}, {organization}, {publish_web_layer}, {portal_folder})

        Shares a package by uploading it to ArcGIS Online or ArcGIS
        Enterprise.

     INPUTS:
      in_package (File):
          The input layer (.lpk or .lpkx), scene layer (.slpk), map (.mpk or
          .mpkx), geoprocessing (.gpk, .gpkx), tile (.tpk or .tpkx), mobile map
          (.mmpk), vector tile (.vtpk), address locator (.gcpk), or project
          (.ppkx or .aptx) package file.
      username (String):
          The ArcGIS Online or ArcGIS Enterprise username. This parameter has
          been deprecated and should consist of an empty string. Before running
          the Python script, you must sign in to the active portal from the
          application. Alternatively, you can sign in using the SignInToPortal
          function.
      password (Encrypted String):
          The ArcGIS Online or ArcGIS Enterprise password. This parameter has
          been deprecated and should consist of an empty string. Before running
          the Python script, you must sign in to the active portal from the
          application. Alternatively, you can sign in using the SignInToPortal
          function.
      summary {String}:
          The summary of the package. The summary is displayed in the item
          information of the package on ArcGIS Online or ArcGIS Enterprise.
      tags {String}:
          The tags used to describe and identify the package. Individual tags
          are separated using either a comma or a semicolon.
      credits {String}:
          The credits for the package. This is generally the name of the
          organization that is given credit for authoring and providing the
          content for the package.
      public {Boolean}:
          Specifies whether the input package will be shared with and available
          to everybody.EVERYBODY-The input package will be shared with
          everybody.MYGROUPS-
          The input package will be shared with the package owner and
          any selected groups. This is the default.
      groups {String}:
          The groups the package will be shared with.
      organization {Boolean}:
          Specifies whether the input package will be available within your
          organization only or shared publicly with everyone.EVERYBODY-The
          package will be shared with everybody. This is the
          default.MYORGANIZATION-The package will be shared within your
          organization
          only.
      publish_web_layer {Boolean}:
          Specifies whether the package will be published as a web layer to your
          portal. Only tile packages, vector tile packages, and scene layer
          packages are supported.FALSE-The package will be uploaded without
          publishing. This is the
          default.TRUE-The package will be uploaded and published as a web layer
          with
          the same name.
      portal_folder {String}:
          An existing folder or the name of a new folder on the portal for the
          package. If a web layer is published, it is stored in the same folder.

        """