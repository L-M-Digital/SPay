.PHONY: apply delete get

.DEFAULT_GOAL := apply

NAMESPACE := tcc

apply:
	minikube kubectl -- apply -f deploy/Deployment.yaml -n $(NAMESPACE)
	minikube kubectl -- apply -f deploy/Service.yaml -n $(NAMESPACE)
	minikube kubectl -- apply -f deploy/PersistentVolumeClaim.yaml -n $(NAMESPACE)
	minikube kubectl -- apply -f deploy/postgres-deployment.yaml -n $(NAMESPACE)
	minikube kubectl -- apply -f deploy/postgres-service.yaml -n $(NAMESPACE)

delete:
	minikube kubectl -- delete -f deploy/Deployment.yaml -n $(NAMESPACE)
	minikube kubectl -- delete -f deploy/Service.yaml -n $(NAMESPACE)
	minikube kubectl -- delete -f deploy/PersistentVolumeClaim.yaml -n $(NAMESPACE)
	minikube kubectl -- delete -f deploy/postgres-deployment.yaml -n $(NAMESPACE)
	minikube kubectl -- delete -f deploy/postgres-service.yaml -n $(NAMESPACE)

get:
	minikube kubectl -- get deployment,service,pvc -n $(NAMESPACE)
