import torch
import torchmetrics as tm

import tml.core.metrics as core_metrics

# create metrics function to update the dictionary

def create_metrics(
  device: torch.device,
):
  metrics = dict()
  metrics.update(
    {
      "AUC": core_metrics.Auc(128),
    }
  )
  metrics = tm.MetricCollection(metrics).to(device)
  return metrics
