apply:
    kubectl apply -f deploy/Deployment.yaml
    kubectl apply -f deploy/Service.yaml
    kubectl apply -f deploy/PersistentVolumeClaim.yaml
    kubectl apply -f deploy/postgres-deployment.yaml
    kubectl apply -f deploy/postgres-service.yaml

delete:
    kubectl delete -f deploy/Deployment.yaml
    kubectl delete -f deploy/Service.yaml
    kubectl delete -f deploy/PersistentVolumeClaim.yaml
    kubectl delete -f deploy/postgres-deployment.yaml
    kubectl delete -f deploy/postgres-service.yaml

get:
    kubectl get deployment -n TCC
    kubectl get service -n TCC
    kubectl get pvc -n TCC
    kubectl get deployment -n TCC
    kubectl get service -n TCC
