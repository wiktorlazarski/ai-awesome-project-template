import os
import warnings

import hydra
import omegaconf
import pytorch_lightning as pl

import scripts.training.lightning_modules as lm


@hydra.main(
    config_path=os.path.join(os.getcwd(), "configs"), config_name="train_experiment"
)
def main(configs: omegaconf.DictConfig) -> None:
    dataset_module = lm.DataModule(
        batch_size=configs.dataset_module.batch_size,
        num_workers=configs.dataset_module.num_workers,
    )

    nn_module = lm.ModelModule(
        lr=configs.nn_module.lr,
    )

    nn_trainer = pl.Trainer(
        max_epochs=configs.training.max_epochs,
    )

    nn_trainer.fit(nn_module, dataset_module)
    nn_trainer.test()


if __name__ == "__main__":
    warnings.filterwarnings("ignore", category=UserWarning)

    main()
