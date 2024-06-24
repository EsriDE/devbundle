# Generated documentation for module arcpy.management


class CreateMobileMapPackage(object):
    """
    Packages maps and basemaps along with all referenced data sources into a single .mmpk file.
    """

    @property
    def description(self) -> str:
        return """

        CreateMobileMapPackage_management(in_map;in_map..., output_file, {in_locator;in_locator...}, {area_of_interest}, {extent}, {clip_features}, {title}, {summary}, {description}, {tags}, {credits}, {use_limitations}, {anonymous_use}, {enable_map_expiration}, {map_expiration_type}, {expiration_date}, {expiration_message}, {select_related_rows}, {reference_online_content})

        Packages maps and basemaps along with all referenced data sources into
        a single .mmpk file.

     INPUTS:
      in_map (Map):
          One or more maps or basemaps that will be packaged into a single .mmpk
          file.
      in_locator {Address Locator}:
          Locators have the following restrictions:       One or more
          locators (.loc) to include in the mobile map package.The locator
          cannot have an unknown coordinate system.The locator or
          any participating locator in a composite locator cannot
          be a geocoding service, including services from ArcGIS Enterprise or
          ArcGIS Online.
      area_of_interest {Feature Layer}:
          Polygon layer that defines the area of interest. Only those features
          that intersect the area_of_interest value will be included in the
          mobile map package.
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
          area of interest or extent.CLIP-The geometry of the features will be
          clipped to the given
          area_of_interest value or extent value.SELECT-Features in the map
          will be selected and their geometry will
          remain unaltered. This is the default.
      title {String}:
          Adds title information to the properties of the package.
      summary {String}:
          The summary information that will be added to the properties of the
          package.
      description {String}:
          Adds description information to the properties of the package.
      tags {String}:
          The tag information that will be added to the properties of the
          package. Multiple tags can be added or separated by a comma or
          semicolon.
      credits {String}:
          Adds credit information to the properties of the package.
      use_limitations {String}:
          Adds use limitations to the properties of the package.
      anonymous_use {Boolean}:
          Specifies whether the mobile map can be used by
          anyone.ANONYMOUS_USE-Anyone with access to the package can use the
          mobile map
          without signing in with an Esri Named User account.STANDARD-Anyone
          with access to the package must be signed in with a
          Named User account to use the mobile map. This is the default.This
          optional parameter is only available with the Publisher
          extension.
      enable_map_expiration {Boolean}:
          Specifies whether a time-out will be enabled on the mobile map
          package.ENABLE_MAP_EXPIRATION-Time-out will be enabled on the mobile
          map
          package.DISABLE_MAP_EXPIRATION-Time-out will not be enabled on the
          mobile map
          package. This is the default.This optional parameter is only available
          with the Publisher
          extension.
      map_expiration_type {String}:
          Specifies the type of access a user will have to the expired mobile
          map package.ALLOW_TO_OPEN-A user of the package will be warned that
          the map has
          expired, but will be allowed to open it. This is the
          default.DONOT_ALLOW_TO_OPEN-A user of the package will be warned that
          the map
          has expired, and will not be allowed to open it.This optional
          parameter is only available with the Publisher
          extension.
      expiration_date {Date}:
          Specifies the date the mobile map package will expire.This optional
          parameter is only available with the Publisher
          extension.
      expiration_message {String}:
          A text message that will display when an expired map is accessed.This
          optional parameter is only available with the Publisher
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
          The output mobile map package (.mmpk).

        """