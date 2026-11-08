# Cows vs Horses — CNN Classification & CycleGAN Image Translation

An experimental Jupyter notebook exploring binary cow/horse image classification and **unpaired image-to-image translation** with CycleGAN.

## What's implemented

1. **Baseline CNN:** a four-layer convolutional classifier with batch normalization, dropout, global average pooling and data augmentation.
2. **Training evaluation:** train/test loss curves, accuracy plots and a confusion matrix.
3. **CycleGAN:** two ResNet-based generators (cow → horse and horse → cow), two PatchGAN discriminators, replay buffer, cycle-consistency loss and identity loss.
4. **Visual experiments:** translated examples and reconstructed images for both directions.
5. **Additional CNN experiment:** a second CNN training run using a separate dataset setup.

## Recorded experimental results

- **164** baseline training images; **82** test images.
- Baseline CNN: **50.0% final test accuracy** after **40 epochs**, despite high training accuracy (a sign of poor generalization on this test).
- CycleGAN: **160** training epochs recorded, with sample translations and cycle reconstructions visible in the original notebook.
- Additional CNN run: **122** training images; **82** test images; **50.0% final test accuracy** after 40 epochs.

These are observations from the supplied notebook, not evidence that the model is ready for reliable real-world classification or high-fidelity translation. The notebook does not establish a controlled improvement from CycleGAN.

## Files

- [Source-only Jupyter notebook](cows_horses_complete.ipynb)
- [Cow to horse gallery](images/cow-to-horse.svg)
- [Horse to cow gallery](images/horse-to-cow.svg)
- [CNN training curves](images/cnn-training.svg)
- [Baseline confusion matrix](images/confusion-matrix.svg)

The uploaded original notebook contained inline outputs. This public copy **removes execution outputs** to keep the repository smaller; selected original output figures were preserved separately in the `images/` folder. Computer-specific paths were changed to relative `data/` paths. No training images or model checkpoints are included.

## Requirements

Python, Jupyter, PyTorch, torchvision, NumPy, Matplotlib, scikit-learn and Pillow, plus local cow/horse image folders. Run the notebook from a working directory with the required datasets organized under `data/` according to its path constants. Training is computationally intensive.

[View the portfolio project](../index.html#cow-horse-ml).
