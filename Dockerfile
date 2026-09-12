FROM freqtradeorg/freqtrade:stable
COPY . /freqtrade/
WORKDIR /freqtrade
USER root
RUN mkdir -p /freqtrade/user_data/backtest_results /freqtrade/user_data/data /freqtrade/user_data/logs && chmod -R 777 /freqtrade/user_data
USER ftuser
CMD ["trade", "--config", "user_data/config.json", "--strategy", "SampleStrategy"]
