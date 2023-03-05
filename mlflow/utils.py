import mlflow
from mlflow.tracking import MlflowClient

def yield_artifacts(run_id, path=None):
    client = MlflowClient()
    for item in client.list_artifacts(run_id, path):
        if item.is_dir:
            yield from yield_artifacts(run_id, item.path)
        else:
            yield item.path

def fetch_logged_data(run_id: str) -> dict:
    client = MlflowClient()
    data = client.get_run(run_id).data

    tags = {k: v for k, v in data.tags.items() if not k.startswith("mlflow.")}
    artifacts = list(yield_artifacts(run_id))

    return {
        "params": data.params,
        "metrics": data.metrics,
        "tags": tags,
        "artifacts": artifacts
    }

# run_id = 'aeb895f254f64f04a26a666bd5070693'
# print(fetch_logged_data(run_id))