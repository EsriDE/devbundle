# Generated documentation for module arcpy.locref


class ConfigureAddressFeatureClasses(object):
    """
    Configures the Address Range and Site Address feature classes from the Address Data Management solution for use with a linear referencing system (LRS) with the ArcGIS Roads and Highways extension.
    """

    @property
    def description(self) -> str:
        return """

        ConfigureAddressFeatureClasses_locref(in_address_range_features, left_from_address_field, left_to_address_field, right_from_address_field, right_to_address_field, in_site_address_features, address_number_field)

        Configures the Address Range and Site Address feature classes from the
        Address Data Management solution for use with a linear referencing
        system (LRS) with the ArcGIS Roads and Highways extension.

     INPUTS:
      in_address_range_features (Feature Layer):
          The input LRS centerline or LRS line event feature class that is the
          Address Management Address Range feature class.
      left_from_address_field (Field):
          The field in the Address Range feature class that contains information
          for the first address on the left side of a roadway.
      left_to_address_field (Field):
          The field in the Address Range feature class that contains information
          for the last address on the left side of a roadway.
      right_from_address_field (Field):
          The field in the Address Range feature class that contains information
          for the first address on the right side of a roadway.
      right_to_address_field (Field):
          The field in the Address Range feature class that contains information
          for the last address on the right side of a roadway.
      in_site_address_features (Feature Layer):
          The input point feature class that is the Address Management Site
          Address feature class.
      address_number_field (Field):
          The field in the Site Address feature class that contains information
          for the site address number.

        """