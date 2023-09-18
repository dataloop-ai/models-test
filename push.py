import dtlpy as dl
import os

from model_evaluate.main import ModelAdapter

project = dl.projects.get(project_id='603dcf02-fc5f-4b63-bfa0-1bca18bc8c80')
dataset = project.datasets.get(dataset_id='608ea66ec98640e0f454a05b')

metadata = dl.Package.get_ml_metadata(cls=ModelAdapter,
                                      default_configuration={},
                                      output_type=dl.AnnotationType.CLASSIFICATION
                                      )
metadata['system']['ml']['supportedMethods'][2]['evaluate'] = True
module = dl.PackageModule.from_entry_point(entry_point='main.py')
package = project.packages.push(package_name='test-predict',
                                src_path=os.getcwd(),
                                package_type='ml',
                                # codebase=codebase,
                                requirements=[
                                    dl.PackageRequirement(
                                        name='https://storage.googleapis.com/dtlpy/dtlpy-metrics/dtlpymetrics-latest-py3-none-any.whl'),
                                    dl.PackageRequirement(name='matplotlib')],
                                modules=[module],
                                is_global=True,
                                service_config={
                                    'runtime': dl.KubernetesRuntime(pod_type=dl.INSTANCE_CATALOG_REGULAR_XS,
                                                                    runner_image='jjanzic/docker-python3-opencv',
                                                                    autoscaler=dl.KubernetesRabbitmqAutoscaler(
                                                                        min_replicas=0,
                                                                        max_replicas=1),
                                                                    concurrency=1).to_json()},
                                metadata=metadata)


# model = package.models.update(model_name='test-predict',
#                               description='test-predict',
#                               tags=['pretrained'],
#                               dataset_id=None,
#                               configuration={},
#                               status='trained',
#                               project_id=package.project.id,
#                               labels=['test']
#                               )
