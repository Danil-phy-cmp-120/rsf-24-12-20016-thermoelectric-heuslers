## Repository Contents

### `ZT_e_max_by_T_all.csv`
Electronic figure of merit \(Z_T^{(e)}\) vs temperature for all considered double half-Heuslers.

### `chgnet_dataset_dhh_I-42d.json`
Dataset for CHGNet fine-tuning (I-42d structures, energies, forces, stresses).

### `chgnet_dataset_dhh_Pmn21.json`
Same as above, but for Pmn2₁ structures.

### `chgnet_dataset_dhh_with_stresses.json`
Extended dataset including stress tensors for elasticity-aware training.

### `dhh_split_indices.npz`
Train/val/test split indices.

### `epoch49_e140_f26_s290_mNA.pth.tar`
Fine-tuned CHGNet checkpoint.

### `fine_tuning_dhh.ipynb`
Notebook performing CHGNet fine-tuning.

### `evaluate_models.ipynb`
Notebook evaluating model accuracy and generating comparison plots.
