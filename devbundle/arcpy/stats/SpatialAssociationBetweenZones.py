# Generated documentation for module arcpy.stats


class SpatialAssociationBetweenZones(object):
    """
    Measures the degree of spatial association between two regionalizations of the same study area in which each regionalization is composed of a set of categories, called zones. The association between the regionalizations is determined by the area overlap between zones of each regionalization. The association is highest when each zone of one regionalization closely corresponds to a zone of the other regionalization. Similarly, spatial association is lowest when the zones of one regionalization have large overlap with many different zones of the other regionalization. The primary output of the tool is a global measure of spatial association between the categorical variables: a single number ranging from 0 (no correspondence) to 1 (perfect spatial alignment of zones). Optionally, this global association can be calculated and visualized for specific zones of either regionalization or for specific combinations of zones between regionalizations.
    """

    @property
    def description(self) -> str:
        return """

        SpatialAssociationBetweenZones_stats(input_feature_or_raster, categorical_zone_field, overlay_feature_or_raster, categorical_overlay_zone_field, {output_features}, {output_raster}, {correspondence_overlay_to_input}, {correspondence_input_to_overlay})

        Measures the degree of spatial association between two
        regionalizations of the same study area in which each regionalization
        is composed of a set of categories, called zones. The association
        between the regionalizations is determined by the area overlap between
        zones of each regionalization. The association is highest when each
        zone of one regionalization closely corresponds to a zone of the other
        regionalization. Similarly, spatial association is lowest when the
        zones of one regionalization have large overlap with many different
        zones of the other regionalization. The primary output of the tool is
        a global measure of spatial association between the categorical
        variables: a single number ranging from 0 (no correspondence) to 1
        (perfect spatial alignment of zones). Optionally, this global
        association can be calculated and visualized for specific zones of
        either regionalization or for specific combinations of zones between
        regionalizations.

     INPUTS:
      input_feature_or_raster (Feature Layer / Raster Layer / Image Service):
          The dataset representing the zones of the first regionalization. The
          zones can be defined using polygon features or a raster.
      categorical_zone_field (Field):
          The field representing the zone category of the input zones.
          Each unique value of this field defines an individual zone. For
          features, the field must be integer or text. For rasters, thefield is
          also supported. VALUE
      overlay_feature_or_raster (Feature Layer / Raster Layer / Image Service):
          The dataset representing the zones of the second regionalization. The
          zones can be polygon features or a raster.
      categorical_overlay_zone_field (Field):
          The field representing the zone category of the overlay zones.
          Each unique value of this field defines an individual zone. For
          features, the field must be integer or text. For rasters, thefield is
          also supported. VALUE

     OUTPUTS:
      output_features {Feature Class}:
          The output polygon features containing spatial association measures at
          all intersections of the input and overlay zones.The output features
          can be used to measure the association between
          specific combinations of input and overlay zones, such as the
          association between areas of corn production (crop type) and areas of
          well-drained soil (soil drainage class). This parameter is only
          enabled if the input and overlay zones are both polygon features.
      output_raster {Raster Dataset}:
          The output raster containing spatial association measures between the
          input and overlay zones.The output raster will have three fields to
          indicate the spatial
          association measures for intersections of the input and overlay zones,
          correspondence of overlay zones within input zones, and correspondence
          of input zones within overlay zones. This parameter is only enabled if
          at least one of the input and overlay zones is a raster.
      correspondence_overlay_to_input {Feature Class}:
          The output polygon features containing the correspondence measures of
          the overlay zones within the input zones.This output will have the
          same geometry as the input zones and can be
          used to identify which input zones closely correspond overall to the
          overlay zones. Specific zone combinations can then be investigated
          with the output features. This parameter is only enabled if the input
          and overlay zones are both polygon features.
      correspondence_input_to_overlay {Feature Class}:
          The output polygon features containing the correspondence measures of
          the input zones within the overlay zones.This output will have the
          same geometry as the overlay zones and can
          be used to identify which overlay zones closely correspond overall to
          the input zones. Specific zone combinations can then be investigated
          with the output features. This parameter is only enabled if the input
          and overlay zones are both polygon features.

        """