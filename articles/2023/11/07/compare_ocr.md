# OCR

## Considered tooles

Information included are relevant for scrapy project

 1. [tesseract](https://github.com/tesseract-ocr/tesseract)
     - Apache-2.0 license
     - Oldest tool used for benchamrking other tools
     - Works good on CPU
     - Requires installation of tesseract and additional python library which enables access to its functionality.
     - `tesserocr` integrates directly with Tesseract's C++ API using Cython, whic allows more refined access to tesseract functionality.
     - Has a large number of configuration parameters
     - Can be trained for given data
 2. [doctr](https://github.com/mindee/doctr)
     - Apache-2.0 license
     - Uses `TensorFlow 2` or `PyTorch`
     - Works good on CPU
     - Requires installtion of `TensorFlow 2` or `PyTorch`
     - Alows using different models
 3. [EasyOCR](https://github.com/JaidedAI/EasyOCR)
     - Apache-2.0 license
     - Uses `PyTorch`
     - Works best on GPU

## Other tools

 1. [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) - [english README](https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.7/README_en.md) - worth of further investigation
 2. [TrOCR](https://huggingface.co/docs/transformers/model_doc/trocr) - worth of further investigation
 3. [donut](https://github.com/clovaai/donut)
 4. [keras-ocr](https://github.com/faustomorales/keras-ocr)
 5. [OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF)
 6. [mmocr](https://github.com/open-mmlab/mmocr)

## Comparison between tesseract and doctr

### Tesseract

PROS:

- Finds nearly all places with characters
- Is less inclined to modify structured data like names
- Keeps distance between characters, is less eager in adding single character to a nearby word
- Has more configuration options without a need to add new model

CONS:

- Sometimes duplicates characters or inject similar characters for example in warrant_number like CR01234 CR`O`01234 (injects capital `o` before 0)
- Adds more noise (compared to docTR) but it is not so common
- Have more difficulties with identifying standalone characters like `B` or `I`
- It is slower compared to `doctr`

### doctr

PROS:

- Have less problems with identifying single characters
- Is less eager to inject characters in the middle of word
- Adds less noise compared to tesseract
- Is a little faster
- Comes with tool which allows easy visual inspection of results
- Easier to install in development environment

CONS:

- Is more eager to add a letter to the end of a word for example duplicate of a letter which is at the begining of next word
- Have more difficulties with preserving distance between words and single characters

## Conclusions

Combining capabilities of both tools can improve accuracy of findings, but if only one could be used it would be better to choose `doctr` as it adds less noise and in case of given PDF is better in identifying individual characters.
