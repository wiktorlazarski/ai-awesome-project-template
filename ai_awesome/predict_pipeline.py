import typing as t

import ai_awesome.model as mdl


class InferencePipeline:
    def __init__(self):
        self.nn_model = mdl.NeuralNet()

    def __call__(self, X: t.Any) -> t.Any:
        return self.predict(X)

    def predict(self, X: t.Any) -> t.Any:
        preprocessed_in = self._preprocess(X)

        model_out = self.nn_model(preprocessed_in)

        return self._postprocess(model_out)

    def _preprocess(self, X: t.Any) -> t.Any:
        pass

    def _postprocess(self, model_out: t.Any) -> t.Any:
        pass
