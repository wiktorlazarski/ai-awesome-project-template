import typing as t

import pytorch_lightning as pl
import torch


class DataModule(pl.LightningDataModule):
    def __init__(
        self,
        *,
        batch_size: int,
        num_workers: int,
    ):
        self.batch_size = batch_size
        self.num_workers = num_workers

    def setup(self, stage: t.Optional[str] = None) -> None:
        self.train_dataset = None
        self.validation_dataset = None
        self.test_dataset = None

    def train_dataloader(self) -> torch.utils.data.DataLoader:
        return torch.utils.data.DataLoader(
            self.train_dataset,
            batch_size=self.batch_size,
            num_workers=self.num_workers,
            shuffle=True,
            drop_last=True,
            pin_memory=True,
        )

    def val_dataloader(self) -> torch.utils.data.DataLoader:
        return torch.utils.data.DataLoader(
            self.validation_dataset,
            batch_size=self.batch_size,
            num_workers=self.num_workers,
            shuffle=False,
            drop_last=False,
            pin_memory=True,
        )

    def test_dataloader(self) -> torch.utils.data.DataLoader:
        return torch.utils.data.DataLoader(
            self.test_dataset,
            batch_size=self.batch_size,
            num_workers=self.num_workers,
            shuffle=False,
            drop_last=False,
            pin_memory=True,
        )


class ModelModule(pl.LightningModule):
    def __init__(
        self,
        *,
        lr: float,
    ):
        super().__init__()
        self.save_hyperparameters()

        self.learning_rate = lr
        self.criterion = None
        self.neural_net = None

    def configure_optimizers(self) -> torch.optim.Optimizer:
        return torch.optim.Adam(self.neural_net.parameters(), lr=self.learning_rate)

    def training_step(
        self, batch: t.Tuple[torch.Tensor, torch.Tensor], batch_idx: int
    ) -> pl.utilities.types.STEP_OUTPUT:
        pass

    def validation_step(
        self, batch: t.Tuple[torch.Tensor, torch.Tensor], batch_idx: int
    ) -> pl.utilities.types.STEP_OUTPUT:
        pass

    def test_step(
        self, batch: t.Tuple[torch.Tensor, torch.Tensor], batch_idx: int
    ) -> pl.utilities.types.STEP_OUTPUT:
        pass

    def training_epoch_end(self, outputs: pl.utilities.types.EPOCH_OUTPUT) -> None:
        pass

    def validation_epoch_end(self, outputs: pl.utilities.types.EPOCH_OUTPUT) -> None:
        pass

    def test_epoch_end(self, outputs: pl.utilities.types.EPOCH_OUTPUT) -> None:
        pass
