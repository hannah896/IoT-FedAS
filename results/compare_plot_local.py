import h5py
import matplotlib.pyplot as plt

fedas = h5py.File('Cifar100_FedAS_test_0.h5','r')
fedper = h5py.File('Cifar100_FedPer_test_0.h5','r')

acc_fedas = fedas['rs_test_acc'][:]
acc_fedper = fedper['rs_test_acc'][:]

plt.figure(figsize=(9,5))
plt.plot(acc_fedas, label='FedAS (Proposed)')
plt.plot(acc_fedper, label='FedPer (Baseline)')
plt.title('Local Personalized Test Accuracy (CIFAR100)')
plt.xlabel('Round')
plt.ylabel('Accuracy')
plt.legend()
plt.grid(True)
plt.savefig('fedas_vs_fedper_local.png', dpi=200)
plt.show()
