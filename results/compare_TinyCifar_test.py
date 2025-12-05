import h5py
import matplotlib.pyplot as plt
import numpy as np

# ============================
# 1) 실제 TinyCifar 결과 파일 경로 입력
# ============================
files = {
    "FedAvg": "/home/hannah/FedAS/results/TinyCifar_FedAvg_test_0.h5",
    "FedAS": "/home/hannah/FedAS/results/TinyCifar_FedAS_test_0.h5"
}

# ============================
# 2) H5 데이터 로드 함수
# ============================
def load_results(path):
    with h5py.File(path, "r") as f:
        acc = np.array(f["rs_test_acc"])
        auc = np.array(f["rs_test_auc"])
        loss = np.array(f["rs_train_loss"])
    return acc, auc, loss

# ============================
# 3) 그래프 생성
# ============================
plt.figure(figsize=(10, 6))

for name, path in files.items():
    acc, _, _ = load_results(path)
    plt.plot(acc, label=name)

plt.title("TinyCifar: FedAvg vs FedAS (Test Accuracy)")
plt.xlabel("Round")
plt.ylabel("Accuracy")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("tinycifar_fedavg_vs_fedas.png", dpi=200)
plt.show()
