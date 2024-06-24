# Generated documentation for module arcpy.conversion


class ExtractBIMFileFloorplan(object):
    """
    Extracts 2.5D floor plan data from a BIM file workspace into a geodatabase dataset.
    """

    @property
    def description(self) -> str:
        return """

        ExtractBIMFileFloorplan_conversion(in_bim_file_workspace, output_workspace, out_feature_dataset_name, out_polyline_featureclass_name, out_polygon_featureclass_name, out_poi_featureclass_name, out_footprint_featureclass_name, {additional_polyline_categories;additional_polyline_categories...}, {additional_polygon_categories;additional_polygon_categories...}, {included_levels;included_levels...})

        Extracts 2.5D floor plan data from a BIM file workspace into a
        geodatabase dataset.

     INPUTS:
      in_bim_file_workspace (BIM File Workspace):
          The BIM file workspace that contains the building information to be
          extracted.
      output_workspace (Workspace):
          The geodatabase where the output feature dataset will be created. This
          must be an existing geodatabase.
      out_feature_dataset_name (String):
          The name of the dataset where the output feature classes will be
          created. If the feature dataset does not exist, it will be created
          with the spatial reference of the input BIM file workspace.
      out_polyline_featureclass_name (String):
          The name of the output polyline feature class. Polyline features will
          be extracted into this feature class.
      out_polygon_featureclass_name (String):
          The name of the output polygon feature class. Polygon features will be
          extracted into this feature class.
      out_poi_featureclass_name (String):
          The name of the output points of interest feature class. Points of
          interest features will be extracted into this feature class.
      out_footprint_featureclass_name (String):
          The name of the output footprint feature class. Footprint polygons
          from the BIM file workspace will be created in this feature class.The
          feature class will include the following categories:Merge Slabs
          (IFC)Merge Floor (Revit)
      additional_polyline_categories {String}:
          The additional polyline features that will be included in the
          floor plan polyline feature class. Features from the following
          categories can be included:        FurnitureFurniture
          systemWindows(All)
      additional_polygon_categories {String}:
          Specifies the additional polygon features that will be
          included in the floor plan polygon feature class. Features from the
          following categories can be included from Revit data:
          AreasRoomsRoofs        Features from the following categories can be
          included from
          IFC data:        SpacesRoofs
      included_levels {String}:
          The building level or levels of features that will be included in the
          output feature classes. If no building levels are provided, features
          from all levels will be included by default.

        """