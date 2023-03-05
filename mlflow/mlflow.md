
# Mlflow

모델 서빙을 편하게 해주는 오픈소스 라이브러리. 

- Python > 3.7 ?  
    - mlflow.sklearn.autolog() : 안됨. 오류남. --> version upgrade 필요. 

> mlflow ui : mlflow ui 띄어줌. 

log 추가는 아래와 같이 하면됨. 

```
mlflow.log_param("l1_ratio", l1_ratio)
mlflow.log_metric("rmse", rmse)
mlflow.log_artifact("ElasticNet-paths.png")

--  mlflow에서 logging을 지원하는 라이브러리인 경우 -- 
--  sagemaker, pyspark, pytorch, sklearn, .. 지원 -- 

mlflow.sklearn.log_model(lr, "model")

```



## Mlflow Serving

> mlflow models serve -m ./mlruns/0/<run_id>/artifacts/model -p 1234

```
(shell)

curl -X POST -H "Content-Type:application/json" \
--data '{"columns":["age", "sex", "bmi", "bp", "s1", "s2", "s3", "s4", "s5", "s6"] \
"data": [[0.038076,  0.050680,  0.061696,  0.021872, -0.044223, -0.034821, -0.043401, -0.002592,  0.019908, -0.017646]]}' \
http://127.0.0.1:1234/invocations


```

OUTPUT 
> [157.3774842648259]


위와 같이 custom으로 log 지표를 넘겨줄수 있지만, 대부분의 유명한 모델, 라이브러리들은 아래와 같은 
코드에서 대부분의 지표를 자동으로 넣어줌. 

```
import mlflow
mlflow.sklearn.autolog()

<model training>
    ...
    ...


```