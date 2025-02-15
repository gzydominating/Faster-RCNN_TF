# --------------------------------------------------------
# SubCNN_TF
# Copyright (c) 2016 CVGL Stanford
# Licensed under The MIT License [see LICENSE for details]
# Written by Yu Xiang
# --------------------------------------------------------

"""Factory method for easily getting imdbs by name."""

__sets = {}

from .VGGnet_test import VGGnet_test
from .VGGnet_train import VGGnet_train
from .Resnet50_test import Resnet50_test
from .Resnet50_train import Resnet50_train
from .Resnet101_test import Resnet101_test
from .Resnet101_train import Resnet101_train
import pdb
import tensorflow as tf

#__sets['VGGnet_train'] = networks.VGGnet_train()

#__sets['VGGnet_test'] = networks.VGGnet_test()


def get_network(name):
    """Get a network by name."""
    if name.split('_')[0] == 'VGGnet':
        if name.split('_')[1] == 'test':
            return VGGnet_test()
        elif name.split('_')[1] == 'train':
            return VGGnet_train()
        else:
            raise KeyError('Unknown dataset: {}'.format(name))
    elif name.split('_')[0] == 'Resnet50':
        if name.split('_')[1] == 'test':
            return Resnet50_test()
        elif name.split('_')[1] == 'train':
            return Resnet50_train()
        else:
            raise KeyError('Unknown dataset: {}'.format(name))
    elif name.split('_')[0] == 'Resnet101':
        if name.split('_')[1] == 'test':
            return Resnet50_test()
        elif name.split('_')[1] == 'train':
            return Resnet50_train()
        else:
            raise KeyError('Unknown dataset: {}'.format(name))
    else:
        raise KeyError('Unknown dataset: {}'.format(name))
    

def list_networks():
    """List all registered imdbs."""
    return __sets.keys()
