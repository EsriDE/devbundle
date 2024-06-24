# Generated documentation for module arcpy.ba


class GenerateCustomerProfile(object):
    """
    Creates a segmentation profile with an existing customer layer.
    """

    @property
    def description(self) -> str:
        return """

        GenerateCustomerProfile_ba(in_customers_layer, in_segmentation_base, out_profile, {in_volume_field})

        Creates a segmentation profile with an existing customer layer.

     INPUTS:
      in_customers_layer (Feature Layer):
          The input point feature class that represents existing customers.
      in_segmentation_base (String):
          The segmentation base for the profile being created. Available options
          are provided by the segmentation dataset in use.
      in_volume_field {Field}:
          The field containing volume information from which the profile can
          optionally be created. For example, you can create a profile using the
          sales for each customer.

     OUTPUTS:
      out_profile (File):
          The name of the segmentation profile file to be created.

        """