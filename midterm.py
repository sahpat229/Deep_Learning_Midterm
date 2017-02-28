import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from cifar import Cifar
from model import Model

cifar_data = Cifar('../hw3/cifar10')
cifar_data.convert_to_lab

sess = tf.Session()
model = Model(
	sess=sess,
	data=cifar_data.data,
	val_data = cifar_data.val_data,
	num_iter=2000,
	sup_learning_rate=None,
	uns_learning_rate_1=1e-2,
	uns_learning_rate_2=1e-2,
	batch_size=64,
	is_supervised=False,
	)

model.train_init()
model.train()