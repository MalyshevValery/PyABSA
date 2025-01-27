# -*- coding: utf-8 -*-
# file: train_apc_multilingual.py
# time: 2021/5/26 0026
# author: yangheng <hy345@exeter.ac.uk>
# github: https://github.com/yangheng95
# Copyright (C) 2021. All Rights Reserved.

########################################################################################################################
#                    train and evaluate on your own apc_datasets (need train and test apc_datasets)                    #
########################################################################################################################


from pyabsa.functional import Trainer
from pyabsa.functional import APCConfigManager
from pyabsa.functional import ABSADatasetList
from pyabsa.functional import APCModelList

apc_config_multilingual = APCConfigManager.get_apc_config_multilingual()
apc_config_multilingual.model = APCModelList.FAST_LSA_T_V2

datasets_path = ABSADatasetList.Multilingual
sent_classifier = Trainer(config=apc_config_multilingual,
                          dataset=datasets_path,
                          checkpoint_save_mode=1,  # save state_dict instead of model
                          auto_device=True,  # auto-select cuda device
                          load_aug=True,  # training using augmentation data
                          ).load_trained_model()
