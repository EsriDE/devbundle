# Generated documentation for module arcpy.management


class CreateMobileScenePackage(object):
    """
    Creates a mobile scene package file (.mspk) from one or more scenes for use across the ArcGIS system.
    """

    @property
    def description(self) -> str:
        return """

        CreateMobileScenePackage_management(in_scene;in_scene..., output_file, {in_locator;in_locator...}, {area_of_interest}, {extent}, {clip_features}, {title}, {summary}, {description}, {tags}, {credits}, {use_limitations}, {anonymous_use}, {texture_optimization}, {enable_scene_expiration}, {scene_expiration_type}, {expiration_date}, {expiration_message}, {select_related_rows}, {reference_online_content})

        Creates a mobile scene package file (.mspk) from one or more scenes
        for use across the ArcGIS system.

     INPUTS:
      in_scene (Map):
          One or more local or global scenes that will be packaged into a single
          .mspk file. Active scenes and .mapx files can be added as input.
      in_locator {Address Locator}:
          Locators have the following restrictions:       One or more
          locators (.loc file) that will be included in the mobile
          scene package.The locator cannot have an unknown coordinate system.The
          locator or
          any participating locator in a composite locator cannot
          be a geocoding service, including services from ArcGIS Enterprise or
          ArcGIS Online.
      area_of_interest {Feature Layer}:
          A polygon layer that defines the area of interest. Only those features
          that intersect the area of interest will be included in the mobile
          scene package.
      extent {Extent}:
          Specifies the extent that will be used to select or clip
          features.MAXOF-The maximum extent of all inputs will be used.MINOF-The
          minimum
          area common to all inputs will be used.DISPLAY-The extent is equal to
          the visible display.Layer name-The extent of the specified layer will
          be used.Extent object-The extent of the specified object will be
          used.Space delimited string of coordinates-The extent of the specified
          string will be used. Coordinates are expressed in the order of x-min,
          y-min, x-max, y-max.
      clip_features {Boolean}:
          Specifies whether the output features will be clipped to the given
          area of interest or extent.Checked-The geometry of the features will
          be clipped to the given area
          of interest or extent.Unchecked-Features in the scene will be selected
          and their geometry
          will remain unaltered. This is the default.Multipatch feature layers,
          3D point feature layers, LAS dataset
          layers, service layers, and tile packages cannot be clipped and will
          be completely copied to the mobile scene package.Specifies whether the
          output features will be clipped to the given
          area of interest or extent.CLIP-The geometry of the features will be
          clipped to the given area of
          interest or extent.SELECT-Features in the map will be selected and
          their geometry will
          remain unaltered. This is the default.Multipatch feature layers, 3D
          point feature layers, LAS dataset
          layers, and tile packages cannot be clipped and will be completely
          copied to the mobile scene package.
      title {String}:
          Title information that will be added to the properties of the package.
      summary {String}:
          Summary information that will be added to the properties of the
          package.
      description {String}:
          Description information that will be added to the properties of the
          package.
      tags {String}:
          Tag information that will be added to the properties of the package.
          Multiple tags can be added, separated by a comma or semicolon.
      credits {String}:
          Credit information that will be added to the properties of the
          package.
      use_limitations {String}:
          Use limitations that will be added to the properties of the package.
      anonymous_use {Boolean}:
          Specifies whether the mobile scenes can be used by anyone or only
          those with an ArcGIS account.ANONYMOUS_USE-Anyone with access to the
          package can use the mobile
          scene without signing in with an Esri named user
          account.STANDARD-Anyone with access to the package must be signed in
          with a
          named user account to use the mobile scene. This is the default.This
          optional parameter is only available with the Publisher
          extension.
      texture_optimization {String}:
          Specifies the textures that will be optimized according to the
          target platform where the scene layer package is used.
          Optimizations that include KTX2 may take significant time to process.
          For fastest results, use the DESKTOP or NONE options.ALL-All texture
          formats will be optimized including JPEG, DXT, and
          KTX2 for use in desktop, web, and mobile platforms.DESKTOP-Windows,
          Linux, and Mac supported textures will be optimized
          including JPEG and DXT for use in ArcGIS Pro clients on Windows and
          ArcGIS Maps SDKs desktop clients on Windows, Linux, and Mac. This is
          the default.MOBILE-Android and iOS supported textures will be
          optimized including
          JPEG and KTX2 for use in ArcGIS Maps SDKs mobile
          applications.NONE-JPEG textures will be optimized for use in desktop
          and web
          platforms.
      enable_scene_expiration {Boolean}:
          Specifies whether the mobile scene package will time
          out.ENABLE_SCENE_EXPIRATION-Time-out functionality will be enabled on
          the
          mobile scene package.DISABLE_SCENE_EXPIRATION-Time-out functionality
          will not be enabled on
          the mobile scene package. This is the default.This optional parameter
          is only available with the Publisher
          extension.
      scene_expiration_type {String}:
          Specifies the type of scene access that will be used for the expired
          mobile scene package.ALLOW_TO_OPEN-The user of the package will be
          warned that the scene
          has expired and allowed to open the scene. This is the
          default.DONOT_ALLOW_TO_OPEN-The user of the package will be warned
          that the
          scene has expired and will not be allowed to open the package.This
          optional parameter is only available with the Publisher
          extension.
      expiration_date {Date}:
          The date the mobile scene package will expire.This optional parameter
          is only available with the Publisher
          extension.
      expiration_message {String}:
          The text message that will appear when an expired scene is
          accessed.This optional parameter is only available with the Publisher
          extension.
      select_related_rows {Boolean}:
          Specifies whether the specified extent will be applied to related data
          sources.KEEP_ONLY_RELATED_ROWS-Only related data corresponding to
          records
          within the specified extent will be
          consolidated.KEEP_ALL_RELATED_ROWS-Related data sources will be
          consolidated in
          their entirety. This is the default.
      reference_online_content {Boolean}:
          Specifies whether service layers will be referenced in the
          package.INCLUDE_SERVICE_LAYERS-Service layers will be referenced in
          the mobile
          package.EXCLUDE_SERVICE_LAYERS-Service layers will not be referenced
          in the
          mobile package. This is the default.

     OUTPUTS:
      output_file (File):
          The output mobile scene package .mspk file.

        """