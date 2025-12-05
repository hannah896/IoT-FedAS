import h5py
import matplotlib.pyplot as plt

# FedAS
f1 = h5py.File("Cifar100_FedAS_test_0.h5","r")
acc_as = f1['rs_test_acc'][:]

# FedAvg
f2 = h5py.File("Cifar100_FedAvg_test_0.h5","r")
acc_avg = f2['rs_test_acc'][:]

plt.figure(figsize=(10,6))
plt.plot(acc_as, label="FedAS")
plt.plot(acc_avg, label="FedAvg")

plt.title("FedAS vs FedAvg Test Accuracy")
plt.xlabel("Round")
plt.ylabel("Accuracy")
plt.legend()
plt.grid(True)
plt.savefig("fed_compare.png", dpi=300)
print("saved as fed_compare.png")
