# custom_h5_dataset.py
import h5py
import numpy as np

class CustomH5Dataset():
    def __init__(self, filename, batch_size, npoints=4096, shuffle=True):
        self.f = h5py.File(filename, 'r')
        self.data = self.f['data'][:]  # shape (N, 4096, 8)
        self.label = self.f['label'][:]  # shape (N,)
        self.batch_size = batch_size
        self.npoints = npoints
        self.shuffle = shuffle
        self.num_examples = self.data.shape[0]
        self.reset()

    def reset(self):
        self.idx = 0
        if self.shuffle:
            perm = np.arange(self.num_examples)
            np.random.shuffle(perm)
            self.data = self.data[perm]
            self.label = self.label[perm]

    def has_next_batch(self):
        return self.idx < self.num_examples

    def next_batch(self, augment=False):
        start = self.idx
        end = min(start + self.batch_size, self.num_examples)
        self.idx = end
        return self.data[start:end], self.label[start:end]

    def num_channel(self):
        return self.data.shape[2]
