FROM freqtradeorg/freqtrade:stable
COPY . /freqtrade/
WORKDIR /freqtrade
CMD ["trade", "--config", "user_data/config.json", "--strategy", "SampleStrategy"]
