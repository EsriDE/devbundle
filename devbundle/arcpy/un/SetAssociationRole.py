# Generated documentation for module arcpy.un


class SetAssociationRole(object):
    """
    Alters the association role assigned to a network feature class or table at the asset type level.
    """

    @property
    def description(self) -> str:
        return """

        SetAssociationRole_un(in_utility_network, domain_network, featureclass, assetgroup, assettype, association_role_type, association_deletion_semantics, {view_scale}, {split_content})

        Alters the association role assigned to a network feature class or
        table at the asset type level.

     INPUTS:
      in_utility_network (Utility Network / Utility Network Layer):
          The utility network that contains the asset type with an association
          role to set.
      domain_network (String):
          The domain network that contains the asset type with an association
          role to set.
      featureclass (String):
          The utility network feature class or table where the association role
          will be set.
      assetgroup (String):
          The asset group that contains the asset type.
      assettype (String):
          The asset type that the association role will be set for.
      association_role_type (String):
          Specifies the type of association role that will be assigned to the
          asset type.CONTAINER-The container association role type will be
          assigned.
          Features or objects of this role type can contain other features and
          objects as content.STRUCTURE-The structure association role type will
          be assigned.
          Features or objects of this role type can have other features and
          objects attached to them.NONE-No role type will be assigned. These are
          features or objects that
          are neither a container nor a structure but do connect to other
          structures.
      association_deletion_semantics (String):
          Specifies the deletion semantics for the network features, which
          defines how content or attachment network features will be managed
          when the container or structure is deleted. This applies to both
          container and structure association roles.CASCADE-When the container
          or structure is deleted, all content or
          attachment network features will be deleted.SET_TO_NONE-When a
          container or structure is deleted, its content or
          attachment network features are not deleted, but are removed from the
          containment or structural attachment association.RESTRICTED-If
          content or attachment network features exist, an error
          will be returned when attempting to delete the container or structure.
          The content or attachment network features must be removed before
          deleting the container or structure.
      view_scale {Double}:
          The scale at which containment mode will be entered to edit
          features participating in the container. For example, setting the view
          scale to 5 means that when you enter containment mode of the container
          feature, the scale will be 1:5. Units are based on the utility network
          units, which are located on thetab of the utility network layer
          properties pane. This parameter does not apply to junction and edge
          objects. Source
      split_content {Boolean}:
          Specifies whether the associated content of a container will be split
          if the container feature is split. This parameter is only enabled if
          the association role is container and is only applicable for line
          features.SPLIT-The container's content will be split if the container
          feature
          is split. If a parallel content line feature is found, the content is
          also split and each section will be contained by the closest container
          feature. If the content line is not parallel, the content will be
          contained by the container feature that is closest to it. When the
          content is a nonspatial junction object, the content is duplicated so
          that each container feature has a junction object as content. When the
          content is a nonspatial edge object, the content is split so that each
          container feature has an edge object as content.DO_NOT_SPLIT-The
          container's content will not be split if the
          container feature is split. If a parallel content line feature is
          found, the content will be contained by both sections of the container
          feature. If the content line is not parallel, the content will be
          contained by the container feature that is closest to it. When working
          with nonspatial junction object content, the content will be contained
          by the larger container. When working with nonspatial edge object
          content, the content is maintained as content to both parent
          containers. This is the default.

        """