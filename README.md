# FedAS: 개인화 연합 학습의 불일치 문제 해결
### 사물인터넷 Lab2 논문 구현 수행


------------------------------------------------------------------------------------------------------
# [CVPR24] FedAS: Bridging Inconsistency in Personalized Fedearated Learning
개인화 연합 학습(PFL)에서 발생하는 불일치 문제 해결 프레임워크

> Xiyuan Yang, Wenke Huang, Mang Ye  
> *CVPR 2024*, [Paper Link](https://openaccess.thecvf.com/content/CVPR2024/html/Yang_FedAS_Bridging_Inconsistency_in_Personalized_Federated_Learning_CVPR_2024_paper.html)

Code Implementation and Informations about FedAS

## Citation
```
@inproceedings{cvpr24_xiyuan_fedas,
    author    = {Yang, Xiyuan and Huang, Wenke and Ye, Mang},
    title     = {FedAS: Bridging Inconsistency in Personalized Fedearated Learning},
    booktitle = {CVPR},
    year      = {2024}
}
```
------------------------------------------------------------------------------------------------------
## 핵심 문제 정의
### 1. 클라이언트 내부 불일치 (Intra-client Inconsistency)
- 개인화 파라미터(Local)와 공유 파라미터(Global) 간 학습 방향이 충돌
- 중앙에서 받은 전역 모델이 로컬 지식을 덮어쓰는 문제
→ 개인화 모델의 일반화 능력 저하

### 2. 클라이언트 간 불일치 (Inter-client Inconsistency)
- 데이터가 부족하거나 참여하지 않는 낙오자(Stragglers)
- 미학습 모델이 집계에 참여 → 전체 수렴 성능 저하
→ 전체 시스템 성능 하락 및 불안정한 학습


## 제안 기법: FedAS Framework
PA(Parameter-Alignment) + CS(Client-Synchronization)
두 가지 기법을 결합해 불일치 문제를 동시에 해

### 1. Parameter Alignment (PA)
- 로컬 파라미터를 전역 파라미터에 정렬(Alignment)
- 클라이언트 내부 지식의 보존과 공유를 균형 있게 유지
→ 일관된 데이터 처리 & 로컬 적응력 증가

### 2. Client Synchronization (CS)
- 참여하지 않은 클라이언트 영향을 최소화
- Fisher Information Matrix(FIM) 기반 중요도 추정
- 중요도 높은 업데이트에 집계 가중치 부여
→ 낙오자 문제 해결 → 안정 수렴


## 알고리즘 개요 흐름
1. 로컬 모델 학습 진행
2. PA를 통해 전역 파라미터와 정렬
3. 각 파라미터 중요도를 FIM으로 계산
4. CS 기반 파라미터 동기화
5. α-가중치를 반영하여 서버에서 전역 모델 집계
6. 반복 수행


## 실험 환경
항목	        내용
데이터셋	    CIFAR-10, CIFAR-100, TinyCIFAR
데이터 분할 	Dirichlet 분포 기반 Non-IID
백본 모델	    CNN 기반 네트워크
비교 방식    	FedAvg, pFedMe, FedALA, FedProto 등 최신 PFL 기법


## 실험 결과

### CIFAR-100 결과
- 모든 조건에서 기존 방법 대비 일관된 성능 향상
- 데이터 이질성 강화 시에도 정확도 우수 유지
- 13개 실험 조합 중 5개 이상에서 최고 성능 달성

### Ablation Study
PA 제거:	내부 불일치 증가 → 성능 하락
CS 제거:	낙오자 영향 확대 → 수렴 저하
둘 다 유지:	최고 성능


## 추가 실험
### FedAS-vs-FedAvg-on-TinyImageNet
FedAS,
FedAvg,
FedPer 의 결과물을 담고 있음.

추가 데이터 셋으로 학습했을 때의 FedAS, FedAvg의 Global 환경에서의 결과 비교 실험으로 추가실험 진행
32*32로 이미지 파일 변형후 실험 진행.

- 글로벌 환경 및 다양한 데이터셋에서도 안정적 성능 확인
- FedAvg보다 더 높은 Robustness 확보
