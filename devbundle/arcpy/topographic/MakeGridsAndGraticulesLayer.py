# Generated documentation for module arcpy.topographic


class MakeGridsAndGraticulesLayer(object):
    """
    Creates a grouped layer of feature classes depicting grid, graticule, and border features using predefined cartographic specifications. Grid layers are ideal for advanced grid definitions that are scale and extent specific.
    """

    @property
    def description(self) -> str:
        return """

        MakeGridsAndGraticulesLayer_topographic(in_grid_xml, area_of_interest, target_feature_dataset, out_layer_name, {grid_name}, {configure_layout}, {layout}, {map_frame}, {reference_scale}, {rotation}, {mask_size}, {xy_tolerance}, {primary_coordinate_system}, {ancillary_coordinate_system_1}, {ancillary_coordinate_system_2}, {ancillary_coordinate_system_3}, {ancillary_coordinate_system_4})

        Creates a grouped layer of feature classes depicting grid, graticule,
        and border features using predefined cartographic specifications. Grid
        layers are ideal for advanced grid definitions that are scale and
        extent specific.

     INPUTS:
      in_grid_xml (File):
          The XML grid definition template that stores the specification's
          graphic properties for each grid layer. In addition to the graphic
          properties, which cannot be altered before execution, the definition
          has specific default values, exposed as parameters, that can be
          modified before execution.
      area_of_interest (Feature Layer / Extent):
          The polygon feature layer or geographic extent used to determine the
          area over which the grid features are created.
      target_feature_dataset (Feature Dataset):
          The feature dataset that will store the grid features. Grid-specific
          feature classes will be created if they do not already exist. If they
          already exist, and a grid with the same name and type as the one being
          created also exists, it will be overwritten.
      grid_name {String / Field}:
          The name used to uniquely identify the grid. You can use a unique name
          for the grid or choose a field from the input area of interest feature
          layer.
      configure_layout {Boolean}:
          Adjusts the map, map frame, and layout settings to ensure they match
          the grid layer. The map's coordinate system as well as the map frame's
          scale, rotation, size, and extent can be altered to enforce
          consistency. This setting requires that a map frame is chosen from the
          map_frame parameter.CONFIGURE_LAYOUT-The data frame and layout are
          configured using grid
          settings.NO_CONFIGURE_LAYOUT-The data frame and layout are not
          configured. This
          is the default.
      layout {Layout}:
          The layout that contains the map frame to which the grid will be added
          when the configure_layout parameter is enabled. The layout can be in
          the active project or from an existing layout file.
      map_frame {String}:
          The map frame that will be updated. The map associated with the map
          frame can also be updated.
      reference_scale {Double}:
          The scale at which the grid is created and should be viewed.
          When the reference scale from the XML grid definition file is defined
          as Use Environment, the reference scale is derived in the following
          order:        The geoprocessing Reference Scale environment settingThe
          active data
          frame's reference scaleThe active data frame's scaleThe value from the
          XML grid definition file
      rotation {Double}:
          The rotation angle for the grid components. Rotation is used
          to create annotation features that are aligned with the page. Unless
          otherwise specified, rotation is calculated using the area of interest
          feature. When the rotation type from the XML grid definition file is
          defined as Use Environment, the rotation is derived in the following
          order:        The active data frame's rotationThe value from the XML
          grid definition
          file
      mask_size {Linear Unit}:
          The mask is a polygon feature that forms an outer ring around the
          extent of the neatline and is used to mask data that falls in the area
          reserved for coordinate labels. Mask size defines the width of the
          polygon mask feature in map or page units. The data frame may need to
          be resized to fit around the edge of the mask while including the
          coordinate labels.
      xy_tolerance {Linear Unit}:
          The minimum distance between geodatabase features, expressed in linear
          units. This value defaults to the value set in the grid XML. You can
          set higher values for data with less coordinate accuracy and lower
          values for data with extremely high accuracy. Features that fall
          within the set x,y tolerance will be considered coincident.
      primary_coordinate_system {Spatial Reference}:
          The primary coordinate system used to create grid features. The final
          product or data frame should use the same coordinate system. This
          coordinate system must be a projected coordinate system. When
          the primary coordinate system in the XML grid definition
          file is defined as Use Environment, the default primary coordinate
          system is derived in the following order:        The geoprocessing
          Cartographic Coordinate System environment
          settingThe active data frame's coordinate system if it is a projected
          coordinate systemThe Fixed value from the XML grid definition file
      ancillary_coordinate_system_1 {Spatial Reference}:
          The first of up to four ancillary coordinate systems used to create
          grid features. The grid template XML file specifies the number of
          ancillary grids.
      ancillary_coordinate_system_2 {Spatial Reference}:
          The second of up to four ancillary coordinate systems used to create
          grid features. The grid template XML file specifies the number of
          ancillary grids.
      ancillary_coordinate_system_3 {Spatial Reference}:
          The third of up to four ancillary coordinate systems used to create
          grid features. The grid template XML file specifies the number of
          ancillary grids.
      ancillary_coordinate_system_4 {Spatial Reference}:
          The fourth of up to four ancillary coordinate systems used to create
          grid features. The grid template XML file specifies the number of
          ancillary grids.

     OUTPUTS:
      out_layer_name (Group Layer):
          The name of the group layer that will be created to contain
          the symbolized grid and graticule feature classes. The group layer can
          be composed of the following layers for grid elements:        Mask
          (polygon)Clip (polygon)Segments (line)Gridlines (line)Ticks
          (line)Endpoints (point)Points (point)AnnotationThis is a temporary
          layer that you must save in the project or as a
          layer file.

        """