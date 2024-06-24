# Generated documentation for module arcpy.management


class MakeWCSLayer(object):
    """
    Creates a temporary raster layer from a WCS service.
    """

    @property
    def description(self) -> str:
        return """

        MakeWCSLayer_management(in_wcs_coverage, out_wcs_layer, {template}, {band_index;band_index...})

        Creates a temporary raster layer from a WCS service.

     INPUTS:
      in_wcs_coverage (WCS Coverage / String):
          The name of the input WCS service, or the URL that references the WCS
          service.If a WCS server URL is used, the URL should include the
          coverage name
          and version information. If only the URL is entered, the tool will
          automatically take the first coverage and use the default version
          (1.0.0) to create the WCS layer.An example of a URL that includes the
          coverage name and version is htt
          p://ServerName/arcgis/services/serviceName/ImageServer/WCSServer?cover
          age=rasterDRGs&version=1.1.1.In this example,
          http://ServerName/arcgis/services/serviceName/ImageServer/WCSServer?
          is the URL. The coverage specified is coverage=rasterDRGs, and the
          version is &version=1.1.1.To get the coverage names on a WCS server,
          use the WCS GetCapabilities
          request. An example of WCS request is http://ServerName/arcgis/service
          s/serviceName/ImageServer/WCSServer?request=getcapabilities&service=wc
          s.
      template {Extent}:
          The output extent of the WCS layer.MAXOF-The maximum extent of all
          inputs will be used.MINOF-The minimum
          area common to all inputs will be used.DISPLAY-The extent is equal to
          the visible display.Layer name-The extent of the specified layer will
          be used.Extent object-The extent of the specified object will be
          used.Space delimited string of coordinates-The extent of the specified
          string will be used. Coordinates are expressed in the order of x-min,
          y-min, x-max, y-max.
      band_index {Value Table}:
          The bands that will be exported for the layer. If no bands are
          specified, all the bands will be used in the output.

     OUTPUTS:
      out_wcs_layer (Raster Layer):
          The name of the output WCS layer.

        """