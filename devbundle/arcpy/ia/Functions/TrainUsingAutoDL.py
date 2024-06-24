# Generated documentation for module arcpy.ia.Functions


class TrainUsingAutoDL(object):
    """
    Trains a deep learning model by building training pipelines and automating much of the training process. This includes data augmentation, model selection, hyperparameter tuning, and batch size deduction. Its outputs include performance metrics of the best model on the training data, as well as the trained deep learning model package (.dlpk file) that can be used as input for the Extract Features Using AI Models tool to predict on new imagery.
    """

    @property
    def description(self) -> str:
        return """

        TrainUsingAutoDL_ia(in_data, out_model, {pretrained_model}, {total_time_limit}, {autodl_mode}, {networks;networks...}, {save_evaluated_models})

        Trains a deep learning model by building training pipelines and
        automating much of the training process. This includes data
        augmentation, model selection, hyperparameter tuning, and batch size
        deduction. Its outputs include performance metrics of the best model
        on the training data, as well as the trained deep learning model
        package (.dlpk file) that can be used as input for the Extract
        Features Using AI Models tool to predict on new imagery.

     INPUTS:
      in_data (Folder):
          The folders containing the image chips, labels, and statistics
          required to train the model. This is the output from the Export
          Training Data For Deep Learning tool. The metadata format of the
          exported data must be Classified_Tiles, PASCAL_VOC_rectangles, or
          KITTI_rectangles.
      pretrained_model {File}:
          A pretrained model that will be used to fine-tune the new model. The
          input is an Esri model definition file (.emd) or a deep learning
          package file (.dlpk).A pretrained model with similar classes can be
          fine-tuned to fit the
          new model. The pretrained model must have been trained with the same
          model type and backbone model that will be used to train the new
          model.
      total_time_limit {Double}:
          The total time limit in hours it will take for AutoDL model training.
          The default is 2 hours.
      autodl_mode {String}:
          Specifies the AutoDL mode that will be used and how intensive the
          AutoDL search will be.BASIC-The basic mode will be used. This mode is
          used to train all
          selected networks without hyperparameter tuning.ADVANCED-The advanced
          mode will be used. This mode is used to perform
          hyperparameter tuning on the top two performing models.
      networks {String}:
          Specifies the architectures that will be used to train the
          model.SingleShotDetector-The SingleShotDetector architecture will be
          used to
          train the model. SingleShotDetector is used for object
          detection.RetinaNet-The RetinaNet architecture will be used to train
          the model.
          RetinaNet is used for object detection.FasterRCNN-The FasterRCNN
          architecture will be used to train the
          model. FasterRCNN is used for object detection.YOLOv3-The YOLOv3
          architecture will be used to train the model. YOLOv3
          is used for object detection.HRNet-The HRNet architecture will be used
          to train the model. HRNet is
          used for pixel classification.ATSS-The ATSS architecture will be used
          to train the model. ATSS is
          used for object detection.CARAFE-The CARAFE architecture will be used
          to train the model. CARAFE
          is used for object detection.CascadeRCNN-The CascadeRCNN architecture
          will be used to train the
          model. CascadeRCNN is used for object detection.CascadeRPN-The
          CascadeRPN architecture will be used to train the
          model. CascadeRPN is used for object detection.DCN-The DCN
          architecture will be used to train the model. DCN is used
          for object detection.DeepLab-The DeepLab architecture will be used to
          train the model.
          DeepLab is used for pixel classification.UnetClassifier-The
          UnetClassifier architecture will be used to train
          the model. UnetClassifier is used for pixel
          classification.DeepLabV3Plus-The DeepLabV3Plus architecture will be
          used to train the
          model. DeepLabV3Plus is used for pixel
          classification.PSPNetClassifier-The PSPNetClassifier architecture will
          be used to
          train the model. PSPNetClassifier is used for pixel
          classification.ANN-The ANN architecture will be used to train the
          model. ANN is used
          for pixel classification.APCNet-The APCNet architecture will be used
          to train the model. APCNet
          is used for pixel classification.CCNet-The CCNet architecture will be
          used to train the model. CCNet is
          used for pixel classification.CGNet-The CGNet architecture will be
          used to train the model. CGNet is
          used for pixel classification.DETReg-The DETReg architecture will be
          used to train the model. DETReg
          is used for object detection.DynamicRCNN-The DynamicRCNN architecture
          will be used to train the
          model. DynamicRCNN is used for object detection.EmpiricalAttention-The
          EmpiricalAttention architecture will be used to
          train the model. EmpiricalAttention is used for object
          detection.FCOS-The FCOS architecture will be used to train the model.
          FCOS is
          used for object detection.FoveaBox-The FoveaBox architecture will be
          used to train the model.
          FoveaBox is used for object detection.FSAF-The FSAF architecture will
          be used to train the model. FSAF is
          used for object detection.GHM-The GHM architecture will be used to
          train the model. GHM is used
          for object detection.LibraRCNN-The LibraRCNN architecture will be used
          to train the model.
          LibraRCNN is used for object detection.PaFPN-The PaFPN architecture
          will be used to train the model. PaFPN is
          used for object detection.Res2Net-The Res2Net architecture will be
          used to train the model.
          Res2Net is used for object detection.SABL-The SABL architecture will
          be used to train the model. SABL is
          used for object detection.VFNet-The VFNet architecture will be used to
          train the model. VFNet is
          used for object detection.DMNet-The DMNet architecture will be used to
          train the model. DMNet is
          used for pixel classification.DNLNet-The DNLNet architecture will be
          used to train the model. DNLNet
          is used for pixel classification.FastSCNN-The FastSCNN architecture
          will be used to train the model.
          FastSCNN is used for pixel classification.FCN-The FCN architecture
          will be used to train the model. FCN is used
          for pixel classification.GCNet-The GCNet architecture will be used to
          train the model. GCNet is
          used for pixel classification.MobileNetV2-The MobileNetV2 architecture
          will be used to train the
          model. MobileNetV2 is used for pixel classification.NonLocalNet-The
          NonLocalNet architecture will be used to train the
          model. NonLocalNet is used for pixel classification.OCRNet-The OCRNet
          architecture will be used to train the model. OCRNet
          is used for pixel classification.PSANet-The PSANet architecture will
          be used to train the model. PSANet
          is used for pixel classification.SemFPN-The SemFPN architecture will
          be used to train the model. SemFPN
          is used for pixel classification.UperNet-The UperNet architecture will
          be used to train the model.
          UperNet is used for pixel classification.MaskRCNN-The MaskRCNN
          architecture will be used to train the model.
          MaskRCNN is used for object detection.By default, all the networks
          will be used.
      save_evaluated_models {Boolean}:
          Specifies whether all evaluated models will be saved.SAVE_ALL_MODELS-
          All evaluated models will be
          saved.SAVE_BEST_MODEL-Only the best performing model will be saved.
          This is
          the default.

     OUTPUTS:
      out_model (File):
          The output trained model that will be saved as a deep learning package
          (.dlpk file).

        """