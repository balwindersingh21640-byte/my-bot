from freqtrade.strategy import IStrategy
import talib.abstract as ta
import pandas_ta as pta

class SampleStrategy(IStrategy):
    timeframe = '5m'
    minimal_roi = {"0": 0.02}
    stoploss = -0.10
    process_only_new_candles = True
    use_exit_signal = True
    startup_candle_count: int = 30

    def populate_indicators(self, dataframe, metadata):
        dataframe['rsi'] = ta.RSI(dataframe, timeperiod=14)
        return dataframe

    def populate_entry_trend(self, dataframe, metadata):
        dataframe.loc[
            (dataframe['rsi'] < 30),
            'enter_long'] = 1
        return dataframe

    def populate_exit_trend(self, dataframe, metadata):
        dataframe.loc[
            (dataframe['rsi'] > 70),
            'exit_long'] = 1
        return dataframe
