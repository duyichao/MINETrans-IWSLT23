<div align="center">
  <img src="https://raw.githubusercontent.com/duyichao/MINETrans-IWSLT23/main/assest/MineTrans-logo.bmp" alt="Logo" width="200">
</div>

# The MineTrans Systems for IWSLT 2023 Offline Speech Translation and Speech-to-Speech Translation Tasks

This project is the official implementation of the MineTrans English-to-Chinese speech transaltion system for the IWSLT2023 speech-to-speech translation (S2ST) track and the offline speech translation (S2T) track.

<p align="left">
  🌐 <a href="https://duyichao.github.io/MINETrans-IWSLT23/demo/index.html" target="_blank">Demo Page</a> • 🤗 <a href="" target="_blank">HuggingFace Page(Coming soon)</a> • 📃 <a href="https://aclanthology.org/2023.iwslt-1.3" target="_blank">Paper</a> • 📽️ <a href="https://drive.google.com/file/d/1F-IFVHkzPQk0Q1jCQiCBql6fTrWq8gfH/view" target="_blank">Slide</a> •  ⏬ <a href="https://github.com/duyichao/MINETrans-IWSLT23/blob/main/README.md" target="_blank">Data</a> • 🤖 <a href="https://github.com/duyichao/MINETrans-IWSLT23/blob/main/README.md#pre-trained-models" target="_blank">Model</a> 
   <!-- • 📹 <a href="" target="_blank">Video</a>  -->
</p>

**Team:** [Yichao Du](https://github.com/duyichao), [Zhengsheng Guo](), [Jinchuan Tian](https://scholar.google.com/citations?user=KE5I4R0AAAAJ), [Zhirui
Zhang](https://zrustc.github.io/), [Xing Wang](http://www.xingwang4nlp.com/), [Jianwei Yu](https://scholar.google.com/citations?user=fY1IJ4wAAAAJ&hl=en), [Zhaopeng Tu](http://www.zptu.net/), [Tong Xu](http://staff.ustc.edu.cn/~tongxu/), and [Enhong Chen](https://scholar.google.com/citations?user=Q9h02J0AAAAJ&hl)

<hr>

## Overview
- [Setup](#setup)
- [Speech-to-Speech Translation](#speech-to-speech-translation)
- [Offline Speech Translation](#offline-speech-translation)

<hr>

## Setup
```bash
git clone https://github.com/duyichao/MineTrans-IWSLT23.git
cd MineTrans-IWSLT23
pip install -e ./fairseq
pip install -r requirements.txt
```


## Speech-to-Speech Translation
### Pre-trained Models

#### Speech Encoder & K-means Model

Language | Speech Encoder | Block type | Model size | Dataset  | KM-Model |
--- | --- | --- | --- | --- | --- |
En | [Wav2vec 2.0](https://drive.google.com/drive/folders/1ROowmSkoFHsWXOORgJDg3lNmVoi9HD-W) | Conformer   | Large | Voxpopuli & GigaSS | × |
Zh | [HuBert](https://drive.google.com/drive/folders/1HD8dz9EqdzoUa_rRATJCugROCIjEAl94)      | Transformer | Base  | GigaSS & AISHELL3  | [layer6.km250](https://drive.google.com/drive/folders/1HD8dz9EqdzoUa_rRATJCugROCIjEAl94) |
<!-- En | [Wav2vec 2.0](https://drive.google.com/drive/folders/1ROowmSkoFHsWXOORgJDg3lNmVoi9HD-W) | Transformer | Large | Voxpopuli & GigaSS | × |
En | [HuBert](https://drive.google.com/drive/folders/1HD8dz9EqdzoUa_rRATJCugROCIjEAl94)      | Transformer | Large | Voxpopuli & GigaSS | × | -->

#### S2UT Model
Models | ASR-BLEU | ASR-charF | Checkpoint |
--- | --- | --- | --- | 
W2V2-CONF-LARGE         | 27.7 | 23.4 | [download](https://drive.google.com/drive/folders/1hpVdVlg2o7SLoDHM0FeuJrXBC4WXhzLy) |
W2V2-CONF-LARGE+T2U     | 27.8 | 23.7 | [download](https://drive.google.com/drive/folders/1hpVdVlg2o7SLoDHM0FeuJrXBC4WXhzLy) |
HUBERT-TRANS-LARGE+T2U  | 26.2 | 23.2 | [download](https://drive.google.com/drive/folders/1hpVdVlg2o7SLoDHM0FeuJrXBC4WXhzLy) |
HUBERT-TRANS-LARGE+T2U* | 25.7 | 22.6 | [download](https://drive.google.com/drive/folders/1hpVdVlg2o7SLoDHM0FeuJrXBC4WXhzLy) |

#### Unit HiFi-GAN Vocoder
Unit config | Unit size | Language | Dataset | Model
|---|---|---|---|---
HuBERT Base, layer 6 | 250 | Zh | GigaSS-S (200h) | [d_500000](https://drive.google.com/drive/folders/14Cdnn_dKf7sM7KiEeHamccFWMINSHjEg)

### Data Preparation
<!-- #### Data for HuBert/Wav2vec2 Pretraining
Please follow the steps of data preparation for HuBERT in [here](https://github.com/facebookresearch/fairseq/tree/main/examples/hubert#data-preparation).

#### Target Unit Extraction
To prepare data for S2UT training, follow the steps from Direct S2ST with Discrete Units and format the data in the S2UT format. Note that we use 250 units from the sixth layer (--layer 6) of the hubert model linked above instead. -->

#### Formatting Data
Dataset should be prepared into the following format.
```
id	audio	n_frames	tgt_text	tgt_n_frames
YOU0000010267_S0001707	/path/to/YOU0000010267_S0001707.wav	49600	44 127 27 66 46	100
YOU0000016336_S0001298	/path/to/YOU0000016336_S0001298.wav	83200	44 239 222 46	202
```

### Inference
1. Follow the same inference process as in [fairseq-S2T](https://github.com/pytorch/fairseq/tree/main/examples/speech_to_text) to generate units (`${RESULTS_PATH}/generate-${GEN_SUBSET}.txt`).
``` bash
CFG=config_u250_s2ut_audio.yaml
CKPT_S2UT=/path/to/checkpoint
RESULTS_PATH=/path/to/results
EVAL_DATA_PATH=/path/to/eval_data
GEN_SUBSET=/path/to/test_data


mkdir ${RESULTS_PATH} -p
CUDA_VISIBLE_DEVICES=1 \
  fairseq-generate ${EVAL_DATA_PATH} \
  --config-yaml ${CFG} \
  --task speech_to_text \
  --path ${CKPT_S2UT} --gen-subset ${GEN_SUBSET} \
  --max-tokens 2000000 --max-source-positions 2000000 --max-target-positions 10000 \
  --beam 10 --max-len-a 1 --max-len-b 200 --lenpen 1 \
  --scoring sacrebleu \
  --required-batch-size-multiple 1 \
  --results-path ${RESULTS_PATH}
```
2. Convert unit sequences to waveform through unit-based HiFi-GAN vocoder.
``` bash
VOCODER_CFG=/path/to/vocoder_cfg
VOCODER_CKPT=/path/to/vocoder_ckpt
  grep "^D\-" ${RESULTS_PATH}/generate-${GEN_SUBSET}.txt |
    sed 's/^D-//ig' | sort -nk1 | cut -f3 \
      >${RESULTS_PATH}/generate-${GEN_SUBSET}.hyp.unit
  grep "^T\-" ${RESULTS_PATH}/generate-${GEN_SUBSET}.txt |
    sed 's/^D-//ig' | sort -nk1 | cut -f2 \
      >${RESULTS_PATH}/generate-${GEN_SUBSET}.ref.unit

  mkdir ${RESULTS_PATH}/audio_gen -p
  python3 ./minetrans/scripts/generate_waveform_from_code.py \
    --in-code-file ${RESULTS_PATH}/generate-${GEN_SUBSET}.hyp.unit \
    --vocoder ${VOCODER_CKPT} --vocoder-cfg ${VOCODER_CFG} \
    --results-path ${RESULTS_PATH}/audio_gen --dur-prediction
```
<hr>

## Offline Speech Translation

Coming soon.

<hr>

## Citation
Please cite our paper if you find this repository helpful in your research:
```bibtex
@inproceedings{du2023minetrans,
    title = {The {M}ine{T}rans Systems for {IWSLT} 2023 Offline Speech Translation and Speech-to-Speech Translation Tasks},
    author = {Du, Yichao and Zhengsheng, Guo and Tian, Jinchuan and Zhang, Zhirui and Wang, Xing and Yu, Jianwei and Tu, Zhaopeng  and Xu, Tong  and Chen, Enhong},
    booktitle = {Proceedings of the 20th International Conference on Spoken Language Translation (IWSLT 2023)},
    year = {2023},
    publisher = {Association for Computational Linguistics},
    url = {https://aclanthology.org/2023.iwslt-1.3},
    pages = {79--88},

}
```