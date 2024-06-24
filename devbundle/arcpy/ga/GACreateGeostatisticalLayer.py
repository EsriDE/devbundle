# Generated documentation for module arcpy.ga


class GACreateGeostatisticalLayer(object):
    """
    Creates a new geostatistical layer. An existing geostatistical layer is required to populate the initial values for the new layer.
    """

    @property
    def description(self) -> str:
        return """

        GACreateGeostatisticalLayer_ga(in_ga_model_source, in_datasets;in_datasets..., out_layer)

        Creates a new geostatistical layer. An existing geostatistical layer
        is required to populate the initial values for the new layer.

     INPUTS:
      in_ga_model_source (Geostatistical Layer / File):
          The geostatistical model source to be analyzed.
      in_datasets (Geostatistical Value Table):
          A GeostatisticalDatasets object.Alternatively, it can be a semicolon-
          delimited string of elements.
          Each element is comprised of the following components:The catalog path
          and name to a dataset or the name of a layer in the
          current table of contents, followed by a space.A sequence of field
          names, each field name separated by a space. In
          the case of a raster, the cell values will be used.

     OUTPUTS:
      out_layer (Geostatistical Layer):
          The geostatistical layer produced by the tool.

        """