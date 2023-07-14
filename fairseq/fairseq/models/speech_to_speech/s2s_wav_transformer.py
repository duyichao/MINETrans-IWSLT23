#!/usr/bin/env python3
# Copyright    2023/4/1 17:04              (authors: Yichao Du)
# IDE: PyCharm file: s2s_wav_transformer.py
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
from typing import Any, Dict, List, Optional

import torch
from torch import Tensor

from fairseq import checkpoint_utils, utils
from fairseq.models import (
    FairseqEncoderDecoderModel,
    FairseqEncoderModel,
    FairseqLanguageModel,
    register_model,
    register_model_architecture,
)
from fairseq.models.speech_to_speech.modules.ctc_decoder import CTCDecoder
from fairseq.models.speech_to_speech.modules.stacked_embedding import StackedEmbedding
from fairseq.models.speech_to_text import S2TTransformerEncoder
from fairseq.models.text_to_speech import TTSTransformerDecoder
from fairseq.models.transformer import Linear, TransformerDecoder, TransformerModelBase

logger = logging.getLogger(__name__)
