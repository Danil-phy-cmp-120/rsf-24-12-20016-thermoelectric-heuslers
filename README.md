## Repository Contents

This repository contains the datasets, trained models, notebooks, and uncertainty-analysis files used in the high-throughput screening of aliovalent double half-Heusler thermoelectrics.

---

## 1. Transport and Screening Data

### Electronic Transport Dataset  
`ZT_e_max_by_T_all.csv`

Contains the electronic figure of merit \(Z_T^{(e)}\) as a function of temperature for all considered double half-Heusler compounds. The dataset includes electronic transport descriptors such as Seebeck coefficient, electrical conductivity, power factor, and optimal carrier concentration for both n-type and p-type doping.

### MACE-Derived Elastic and Thermal Descriptor Dataset  
`elastic_gruneisen_results_final_mace.json`

Main dataset containing structural, elastic, and thermodynamic properties for the screened compounds. It includes total energies, formation energies, energy above hull, MACE-derived elastic tensors, bulk and shear moduli, Poisson ratio, Debye temperature, Grüneisen parameter, and Slack-model lattice thermal conductivity.

---

## 2. Elastic Validation and Uncertainty Analysis

### Propagated Error and Uncertainty Table  
`all_errors.csv`

Contains the numerical uncertainty estimates used in the error-propagation analysis. The file includes direct and linearized errors, confidence intervals where applicable, and propagated uncertainties for elastic constants, Reuss bulk and shear moduli, sound velocities, Debye temperature, Grüneisen parameter, and Slack lattice thermal conductivity.

### Pareto-Front Elastic Validation Dataset  
`dataset_dhh_pareto_elastic.json`

Additional strain-stress dataset generated for compounds located on or near the Pareto front. This dataset was used to validate the elastic-property workflow for the most relevant candidate materials and to support the uncertainty analysis of MACE-derived elastic descriptors.

### Error-Propagation Calculation Notebook  
`errors_calculations.ipynb`

Notebook used to calculate and propagate the uncertainty estimates reported in the Supplementary Materials. It includes processing of elastic-tensor errors, propagation to sound velocities and Debye temperature, EOS-based Grüneisen uncertainty analysis, and final Slack lattice-thermal-conductivity uncertainty estimates.

---

## 3. CHGNet Fine-Tuning Data

### CHGNet Training Dataset for I-42d Structures  
`chgnet_dataset_dhh_I-42d.json`

Dataset for CHGNet fine-tuning based on ordered I-42d double half-Heusler structures. It contains structures, total energies, atomic forces, and stress tensors where available.

### CHGNet Training Dataset for Pmn2₁ Structures  
`chgnet_dataset_dhh_Pmn21.json`

Dataset for CHGNet fine-tuning based on ordered Pmn2₁ double half-Heusler structures. It contains structures, total energies, atomic forces, and stress tensors where available.

### Stress-Augmented CHGNet Training Dataset  
`chgnet_dataset_dhh_with_stresses.json`

Extended CHGNet fine-tuning dataset including stress tensors. This file was prepared for elasticity-aware training and validation of machine-learning interatomic potentials.

### Dataset Split Indices  
`dhh_split_indices.npz`

Train, validation, and test split indices used for model training and evaluation.

---

## 4. Trained Models and Notebooks

### Fine-Tuned CHGNet Model Checkpoint  
`epoch49_e140_f26_s290_mNA.pth.tar`

Fine-tuned CHGNet model checkpoint used in the validation workflow.

### CHGNet Fine-Tuning Notebook  
`fine_tuning_dhh.ipynb`

Notebook used for CHGNet fine-tuning on the double half-Heusler dataset.

### Model Evaluation Notebook  
`evaluate_models.ipynb`

Notebook used to evaluate model accuracy and generate comparison plots for energies, forces, stresses, and derived quantities.