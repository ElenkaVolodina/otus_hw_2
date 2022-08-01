## Основы работы с Kubernetes

### Домашняя работа № 2

### Используемый Docker образ
```shell
docker pull elenkavolodina/otus_hw2:latest
```

### Миграции
```shell
Команда alembic upgrade head вызывается в initContainers в hw_2_chart/templates/deployment.yaml
```

### Запуск приложения
```shell
kubectl create namespace otus-hw-2-volodina
helm upgrade --install -n otus-hw-2-volodina otus-hw-2-volodina ./hw_2_chart
```

### Удаление приложения
```shell
helm uninstall otus-hw-2-volodina -n otus-hw-2-volodina
```

### Postman коллекция
```shell
newman run postman_collection/otus_hw_2.postman_collection.json
```
