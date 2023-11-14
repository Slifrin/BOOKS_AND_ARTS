FROM scrapinghub/scrapinghub-stack-scrapy:2.0

ENV PYHTONUNBUFFERED=1
RUN apt-get update \
  && apt-get -y install tesseract-ocr 

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /app
WORKDIR /app

# COPY ./main.py /app

ENV TESSDATA_PREFIX="/usr/share/tesseract-ocr/4.00/tessdata/"

CMD [ "python3", "main.py" ]