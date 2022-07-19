## Основы работы с Kubernetes

### Домашняя работа № 2

### Используемый Docker образ
```shell
docker pull 
```

### Миграции
```shell
alembic upgrade head
```

### Запуск приложения
```shell
cd k8s
kubectl create namespace otus-hw-1-volodina
kubectl apply -f .
```
### Удаление приложения
```shell
kubectl delete namespaces otus-hw-1-volodina
```

### Postman коллекция
```shell
newman run postman_collection/otus_hw_1.postman_collection.json
```
          
```shell

```

