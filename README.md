# The MineTrans Systems for IWSLT 2023 Offline Speech Translation and Speech-to-Speech Translation Tasks

This project is the official implementation of the MineTrans English-to-Chinese speech transaltion system for the IWSLT2023 speech-to-speech translation (S2ST) track and the offline speech translation (S2T) track.

<p align="left">
  🌐 <a href="https://duyichao.github.io/MINETrans-IWSLT23/demo/index.html" target="_blank">Demo Page</a> • 🤗 <a href="" target="_blank">HuggingFace Page(Coming soon)</a> • 📃 <a href="https://aclanthology.org/2023.iwslt-1.3" target="_blank">Paper</a> • 📽️ <a href="https://drive.google.com/file/d/1F-IFVHkzPQk0Q1jCQiCBql6fTrWq8gfH/view" target="_blank">Slide</a> •  ⏬ <a href="https://github.com/duyichao/MINETrans-IWSLT23/blob/main/README.md" target="_blank">Data</a> • 🤖 <a href="https://github.com/duyichao/MINETrans-IWSLT23/blob/main/README.md#pre-trained-models" target="_blank">Model</a> 
   <!-- • 📹 <a href="" target="_blank">Video</a>  -->
</p>

**Team:** [Yichao Du](https://github.com/duyichao), ZHengsheng Guo, [Jinchuan Tian](https://scholar.google.com/citations?user=KE5I4R0AAAAJ), [Zhirui
Zhang](https://zrustc.github.io/), [Xing Wang](http://www.xingwang4nlp.com/), [Jianwei Yu](https://scholar.google.com/citations?user=fY1IJ4wAAAAJ&hl=en), [Zhaopeng Tu](http://www.zptu.net/), [Tong Xu](http://staff.ustc.edu.cn/~tongxu/), and [Enhong Chen](https://scholar.google.com/citations?user=Q9h02J0AAAAJ&hl)

<hr>

## Overview
- [Pre-trained Models](#pre-trained-models)
- [Speech-to-Speech Translation](#speech-to-speech-translation)
- [Offline Speech Translation](#offline-speech-translation)

<hr>

## Pre-trained Models

### Speech Encoder & K-means Model

Language | Speech Encoder | Block type | Model size | Dataset  | KM-Model |
--- | --- | --- | --- | --- | --- |
En | [Wav2vec 2.0]() | Conformer   | Large | Voxpopuli & GigaSS | × |
En | [Wav2vec 2.0]() | Transformer | Large | Voxpopuli & GigaSS | × |
En | [HuBert]()      | Transformer | Large | Voxpopuli & GigaSS | × |
Zh | [HuBert]()      | Transformer | Base  | GigaSS & AISHELL3  | [layer6.km250]() |

### Unit-based HiFi-GAN vocoder
Unit config | Unit size | Language | Dataset | Model
|---|---|---|---|---
HuBERT Base, layer 6 | 250 | Zh | GigaSS-S (200h) | [g_500000]()


### E2E-S2ST Model
Models | ASR-BLEU | ASR-charF | Checkpoint |
--- | --- | --- | --- | 
W2V2-CONF-LARGE         | 27.7 | 23.4 | [download]() |
W2V2-CONF-LARGE+T2U     | 27.8 | 23.7 | [download]() |
HUBERT-TRANS-LARGE+T2U  | 26.2 | 23.2 | [download]() |
HUBERT-TRANS-LARGE+T2U* | 25.7 | 22.6 | [download]() |


## Speech-to-Speech Translation
Coming soon.

<!-- ### Data Preparation

#### Target Unit Extraction
To prepare data for S2UT training, follow the steps from Direct S2ST with Discrete Units and format the data in the S2UT format. Note that we use 250 units from the sixth layer (--layer 6) of the hubert model linked above instead.

### Inference
```

``` -->

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