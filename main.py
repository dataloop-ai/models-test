import typing

import dtlpy as dl
import logging
import os
import random

logger = logging.getLogger('dummy-adapter')


@dl.Package.decorators.module(name='model-adapter',
                              description='Model Adapter for Dummy Model',
                              init_inputs={'model_entity': dl.Model})
class ModelAdapter(dl.BaseModelAdapter):
    """
    Dummy Model adapter using pytorch.
    The class bind Dataloop model and model entities with model code implementation
    """

    def __init__(self, model_entity=None):
        super(ModelAdapter, self).__init__(model_entity=model_entity)

    def load(self, local_path, **kwargs):
        logger.info("Loaded model")

    def save(self, local_path, **kwargs):
        logger.info("Saved model")

    def train(self, data_path, output_path, **kwargs):
        logger.info("model training")

    def predict(self, batch, **kwargs):
        logger.info("model prediction")
        batch_annotations = list()

        return batch_annotations

    def convert_from_dtlpy(self, data_path, **kwargs):
        logger.info("convert_from_dtlpy")
