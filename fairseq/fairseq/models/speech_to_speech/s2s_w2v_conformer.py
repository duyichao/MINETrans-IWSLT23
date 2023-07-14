#!/usr/bin/env python3
# Copyright    2023/3/31 12:33              (authors: Yichao Du)
# IDE: PyCharm file: s2s_w2v_conformer.py.py
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
from pathlib import Path

import torch

import torch
import torch.nn as nn

from fairseq.data.data_utils import compute_mask_indices
from fairseq.models.wav2vec import ConvFeatureExtractionModel

from fairseq.modules import GradMultiply, LayerNorm, SamePad, TransformerEncoderLayer

from fairseq import checkpoint_utils
from fairseq.models import register_model, register_model_architecture, FairseqEncoder
from fairseq.models.speech_to_speech.s2s_transformer import (
    S2SpecTTransformerModel,
    S2UTTransformerModel,
    s2spect_architecture_base,
    s2ut_architecture_base,
)
from fairseq.models.speech_to_text import S2TConformerEncoder, SpeechWavTransformerEncoder
from fairseq.models.transformer import Linear

logger = logging.getLogger(__name__)


#   Conformer encoder with wave input, it is adopted from wav2vec 2.0 Encoder.
#       use wav input
#       use trained position embedding so it is easier to match with text input
class SpeechWavConformerEncoder(SpeechWavTransformerEncoder):

    def __init__(self, args, alway_mask=False):
        super(SpeechWavConformerEncoder, self).__init__(args)
        self.layers = nn.ModuleList(
            [S2TConformerEncoder(args) for _ in range(args.encoder_layers)]
        )


    def forward(
        self,
        src_tokens,
        src_lengths,
        return_all_hiddens=False,
        padding_mask=None,
        features_only=True,
    ):
        pass