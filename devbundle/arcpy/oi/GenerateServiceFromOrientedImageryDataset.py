# Generated documentation for module arcpy.oi


class GenerateServiceFromOrientedImageryDataset(object):
    """
    Generates a hosted feature service with an oriented imagery layer from an input oriented imagery dataset.
    """

    @property
    def description(self) -> str:
        return """

        GenerateServiceFromOrientedImageryDataset_oi(in_oriented_imagery_dataset, service_name, {portal_folder}, {share_with}, {add_footprint}, {attach_images}, {tags}, {summary})

        Generates a hosted feature service with an oriented imagery layer from
        an input oriented imagery dataset.

     INPUTS:
      in_oriented_imagery_dataset (Oriented Imagery Layer):
          The input oriented imagery dataset from which the hosted feature
          service will be created.
      service_name (String):
          The name of the output feature service that will be created.
      portal_folder {String}:
          The folder in the ArcGIS Online or ArcGIS Enterprise portal where the
          service will be added.
      share_with {String}:
          Specifies the sharing level of the output service item.PRIVATE-Only
          the owner of the item will have access. This is the
          default.ORGANIZATION-All members of your organization will have
          accessPUBLIC-People outside your organization will have access
      add_footprint {Boolean}:
          Specifies whether the footprint layer will be added to the output
          service. FOOTPRINT-The feature class defined in theproperty of
          the
          dataset will be added to the service as a sublayer. This is the
          default. Footprint ItemNO_FOOTPRINT-The footprint layer will
          not be added to the service.
      attach_images {Boolean}:
          Specifies whether images will be added as attachments to the output
          service. Images can only be added as attachments when the images are
          on local disk or network storage. ATTACH-The images referenced
          in thefield of the oriented
          imagery dataset will be added to the service as attachments.
          ImagePathNO_ATTACH-The images will not be added to the service as
          attachments.
          This is the default.
      tags {String}:
          The service item tags separated by commas.
      summary {String}:
          A summary of the service item

        """