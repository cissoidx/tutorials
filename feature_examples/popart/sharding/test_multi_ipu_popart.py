# Copyright (c) 2020 Graphcore Ltd. All rights reserved.
import os
import subprocess
import sys
import unittest

import pytest


def run_multi_ipu(shards, batch_size, batches_per_step):
    py_version = "python" + str(sys.version_info[0])
    cmd = [py_version, "multi_ipu.py",
           "--shards", str(shards),
           "--batch-size", str(batch_size),
           "--batches-per-step", str(batches_per_step)]
    cwd = os.path.dirname(__file__)
    try:
        out = subprocess.check_output(
            cmd, cwd=cwd, stderr=subprocess.PIPE).decode("utf-8")
    except subprocess.CalledProcessError as e:
        print(f"TEST FAILED")
        print(f"stdout={e.stdout.decode('utf-8',errors='ignore')}")
        print(f"stderr={e.stderr.decode('utf-8',errors='ignore')}")
        raise
    return out


class TestMultiIPUPopART(unittest.TestCase):
    """Tests for multi-IPU popART code example"""

    @classmethod
    def setUpClass(cls):
        pass

    # Multi-IPU tests

    @pytest.mark.ipus(2)
    @pytest.mark.category1
    def test_multi_ipu_2_10(self):
        out = run_multi_ipu(shards=2, batch_size=10, batches_per_step=100000)
