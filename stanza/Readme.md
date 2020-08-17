## Bio-medical-clinical-NER-stanza
This repo contains utilities for using bio medical ner models from [stanza](https://stanfordnlp.github.io/stanza/)

Stanza is the current SOTA framework for NER and especially for Bio-medical. Here are some comparisons of bio-ner model benchmarks:
![](https://github.com/MageshDominator/bio-medical-clinical-ner/blob/master/stanza/images/ner_benchmark.png)

It outperfoms BioBERT in 3 out of 6 tasks and outperfoms sciSpacy in all the tasks

## Utils:
### [biomed_ner_download_all.py](https://github.com/MageshDominator/bio-medical-clinical-ner/blob/master/stanza/biomed_ner_download_all.py)
* Downloads all stanza bio-med models at one shot
* Download 2 universal dependencies (CRAFT for biomedical, MIMIC for clinical)
* Downloads 8 bio medical ner models and 2 clinical ner models
* Explanation and entities of each model is added in comments

### [saveAsSpacyModel.py](https://github.com/MageshDominator/bio-medical-clinical-ner/blob/master/stanza/saveAsSpacyModel.py)
* Utility to load and save Stanza models using stanza and spacy stanza
Note that this will not save any model data by default. The Stanza models are very large, so for now, this package expects that you load them separately.

### [NER_inference.py](https://github.com/MageshDominator/bio-medical-clinical-ner/blob/master/stanza/NER_inference.py)
* Inference on biomedical and clinical NER models using stanza
* Code used to benchmark my documents collection
* Models can be dropped out based on need and text stream pipeline should be modified as per your need
* For each model, a report will be generated on all documents(all page)

## Reference
@article{zhang2020biomedical,
  title={Biomedical and Clinical English Model Packages in the Stanza Python NLP Library},
  author={Zhang, Yuhao and Zhang, Yuhui and Qi, Peng and Manning, Christopher D. and Langlotz, Curtis P.},
  journal={arXiv preprint arXiv:2007.14640},
  year={2020}
}