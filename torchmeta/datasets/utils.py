import os
import json


def get_asset_path(*args):
    basedir = os.path.dirname(__file__)
    return os.path.join(basedir, "assets", *args)


def get_asset(*args, dtype=None):
    filename = get_asset_path(*args)
    if not os.path.isfile(filename):
        raise IOError("{} not found".format(filename))

    if dtype is None:
        _, dtype = os.path.splitext(filename)
        dtype = dtype[1:]

    if dtype == "json":
        with open(filename, "r") as f:
            data = json.load(f)
    else:
        raise NotImplementedError()
    return data


# QKFIX: The current version of `download_file_from_google_drive` (as of torchvision==0.8.1)
# is inconsistent, and a temporary fix has been added to the bleeding-edge version of
# Torchvision. The temporary fix removes the behaviour of `_quota_exceeded`, whenever the
# quota has exceeded for the file to be downloaded. As a consequence, this means that there
# is currently no protection against exceeded quotas. If you get an integrity error in Torchmeta
# (e.g. "MiniImagenet integrity check failed" for MiniImagenet), then this means that the quota
# has exceeded for this dataset. See also: https://github.com/tristandeleu/pytorch-meta/issues/54
#
# See also: https://github.com/pytorch/vision/issues/2992
#
# The following functions are taken from
# https://github.com/pytorch/vision/blob/cd0268cd408d19d91f870e36fdffd031085abe13/torchvision/datasets/utils.py

from torchvision.datasets.utils import download_file_from_google_drive
