# Generated documentation for module arcpy.indoors


class ImportCADToIndoorDataset(object):
    """
    Imports features from CAD files to an indoor dataset that conforms to the ArcGIS Indoors Information Model. The output of this tool can be used to create floor-aware maps and scenes, as well as to generate an indoor network for routing.
    """

    @property
    def description(self) -> str:
        return """

        ImportCADToIndoorDataset_indoors(input_cad_datasets;input_cad_datasets..., target_level_features, level_name, vertical_order, level_elevation, target_facility_features, facility_name, target_unit_features, target_detail_features, {allow_layers_from_cad}, {input_unit_layers_cad;input_unit_layers_cad...}, {input_unit_feature_layers;input_unit_feature_layers...}, {input_level_layers_cad;input_level_layers_cad...}, {input_level_feature_layers;input_level_feature_layers...}, {input_door_layers_cad;input_door_layers_cad...}, {input_door_feature_layers;input_door_feature_layers...}, {input_detail_layers_cad;input_detail_layers_cad...}, {input_detail_feature_layers;input_detail_feature_layers...}, {input_facility_layers_cad;input_facility_layers_cad...}, {input_facility_feature_layers;input_facility_feature_layers...}, {cad_annotation_mapping;cad_annotation_mapping...}, {door_close_buffer}, {input_unit_minimum_width}, {input_unit_minimum_area})

        Imports features from CAD files to an indoor dataset that conforms to
        the ArcGIS Indoors Information Model. The output of this tool can be
        used to create floor-aware maps and scenes, as well as to generate an
        indoor network for routing.

     INPUTS:
      input_cad_datasets (CAD Drawing Dataset):
          The .dwg or .dgn files that contain floor plan information to be
          imported to the Indoors model.
      target_level_features (Feature Layer):
          The target Levels feature layer, feature class, or feature service
          that conforms to the Indoors model and resides in the same workspace
          as the target Facilities, Units, and Details features.
      level_name (String):
          The unique level name of the level on which the source CAD data is
          located.
      vertical_order (Long):
          An ordinal integer representing the vertical order of each floor. The
          vertical order of the ground floor is zero (0). Floors above the
          ground floor have positive vertical order values, and floors below the
          ground floor have negative values.
      level_elevation (Linear Unit):
          The elevation of the level relative to a flat terrain. This value will
          be used to populate the z-value for levels, units, and details.
      target_facility_features (Feature Layer):
          The target Facilities feature layer, feature class, or feature service
          that conforms to the Indoors model and resides in the same workspace
          as the target Levels, Units, and Details features.
      facility_name (String):
          The unique facility name of the building where the source CAD data is
          located.
      target_unit_features (Feature Layer):
          The target Units feature layer, feature class, or feature service that
          conforms to the Indoors model and resides in the same workspace as the
          target Facilities, Levels, and Details features.
      target_detail_features (Feature Layer):
          The target Details feature layer, feature class, or feature service
          that conforms to the Indoors model and resides in the same workspace
          as the target Facilities, Levels, and Units features.
      allow_layers_from_cad {Boolean}:
          Specifies whether polylines that represent unit boundaries will be
          sourced from CAD files or from map feature layers. If you specify to
          select based on map feature layers, you can make a selection on the
          layer to import a subset of features.ALLOW_LAYERS_FROM_CAD-Polylines
          that represent unit boundaries will be
          sourced directly from the CAD data. This is the
          default.NO_ALLOW_LAYERS_FROM_CAD-Polylines that represent unit
          boundaries will
          be sourced from map feature layers.
      input_unit_layers_cad {String}:
          The CAD layers that contain polyline entities that define the edges
          and extent of the usable spaces within a facility. These polylines
          will be used to create unit polygon features in the target Units
          layer.
      input_unit_feature_layers {Feature Layer}:
          The feature layers that contain polyline entities that define the
          edges and extent of the usable spaces within a facility. These
          polylines will be used to create unit polygon features in the target
          Units layer.
      input_level_layers_cad {String}:
          The CAD layers that contain polyline entities that define the edges
          and extent of the level. These polylines will be used to create unit
          polygon features in the target Levels layer.
      input_level_feature_layers {Feature Layer}:
          The feature layers that contain polyline entities that define the
          edges and extent of the level. These polylines will be used to create
          unit polygon features in the target Levels layer.
      input_door_layers_cad {String}:
          The CAD layers that contain polyline entities that define the doors
          that are part of a unit boundary. These polylines will be closed to
          create unit polygon features in the target Units layer.
      input_door_feature_layers {Feature Layer}:
          The feature layers that contain polyline entities that define the
          doors that are part of a unit boundary. These polylines will be closed
          to create unit polygon features in the target Units layer.
      input_detail_layers_cad {String}:
          The CAD layers that contain polyline entities that represent floor
          plan details-such as walls, windows, and doors-that will be included
          as polyline features in the target Details layer.
      input_detail_feature_layers {Feature Layer}:
          The feature layers that contain polyline entities that represent floor
          plan details-such as walls, windows, and doors-that will be included
          as polyline features in the target Details layer.
      input_facility_layers_cad {String}:
          The CAD layers that contain polyline entities that define the edges
          and extent of the facility footprint. If no value is provided, the
          facility footprint will be created or updated based on the extent of
          all levels within the facility.
      input_facility_feature_layers {Feature Layer}:
          The feature layers that contain polyline entities that define the
          edges and extent of the facility footprint. If no value is provided,
          the facility footprint will be created or updated based on the extent
          of all levels within the facility.
      cad_annotation_mapping {Value Table}:
          Specifies the field mapping for CAD annotation features to
          populate a field of a layer in the Indoors workspace. Target
          Indoor Layer-The layer in the Indoors workspace to which you
          want to map annotation. The tool supports mapping to the layer
          provided for the Target Facilities, Target Levels, and Target Units
          parameters.Target Field-The field in the target layer to which you
          want to map
          annotation. The field must already exist.Entity Type-The entity type
          of the annotation you want to map. Text
          and Block types are supported.Source CAD Layer-The CAD layer that
          contains the annotation that will
          be mapped.Block Attribute-For annotation that has the block entity
          type, provide
          the block attribute that contains the information to map.Delimiter-For
          annotation stored in a delimited string, provide the
          delimiting character.Position-For annotation stored in a delimited
          string, provide the
          position of the value to map.
      door_close_buffer {Linear Unit}:
          The distance the tool will search from a door feature for a unit
          boundary in international inches or millimeters. The parameter value
          must include a numeric value and a unit of measure. The default is 0.3
          international inches.
      input_unit_minimum_width {Linear Unit}:
          The minimum width in international feet or meters that a space must be
          to be considered a unit feature. Features with a width that falls
          below this threshold will be written to a nonunit polygons feature
          class and are not included in the target Units layer. The parameter
          value must include a numeric value and a unit of measure. The default
          is 3 international feet.
      input_unit_minimum_area {Areal Unit}:
          The minimum area in square international feet or square meters a space
          must be to be considered a unit feature. Features with an area that
          falls below this threshold will be written to a nonunit polygons
          feature class and are not included in the target Units layer. The
          parameter value must include a numeric value and a unit of measure.
          The default is 9 square international feet.

        """