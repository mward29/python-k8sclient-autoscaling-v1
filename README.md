# Python API client generated through Codegen for Kubernetes v1.2 Autoscaling v1

## Requirements.
Python 2.7 and later.
swagger-codegen (if you intend to generate your own client)


## v1.json

Pulled from https://raw.githubusercontent.com/kubernetes/kubernetes/master/api/swagger-spec/v1.json for Kubernetes v1.2.2

## Setuptools
You can install the bindings via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install
```

Or you can install from Github via pip:

```sh
pip install git+https://github.com/geekerzp/swagger_client.git
```

To use the bindings, import the pacakge:

```python
import swagger_client
```

## Manual Installation
If you do not wish to use setuptools, you can download the latest release.
Then, to use the bindings, import the package:

```python
import path.to.swagger_client
```

## To Generate your own swagger_client
`swagger-codegen generate -i v1.json -l python -o swagger_client`


## Documentation

`delete_namespaced_horizontal_pod_autoscaler(self,body,namespace,name)`

deleteaHorizontalPodAutoscaler

--

`deletecollection_namespaced_horizontal_pod_autoscaler(self,namespace)`

deletecollectionofHorizontalPodAutoscaler

--

`get_api_resources(self)`

getavailableresources

--

`list_namespaced_horizontal_pod_autoscaler(self)`

listorwatchobjectsofkindHorizontalPodAutoscaler

--

`list_namespaced_horizontal_pod_autoscaler_1(self,namespace)`

listorwatchobjectsofkindHorizontalPodAutoscaler

--

`patch_namespaced_horizontal_pod_autoscaler(self,body,namespace,name)`

partiallyupdatethespecifiedHorizontalPodAutoscaler

--

`read_namespaced_horizontal_pod_autoscaler(self,namespace,name)`

readthespecifiedHorizontalPodAutoscaler

--

`replace_namespaced_horizontal_pod_autoscaler(self,body,namespace,name)`

replacethespecifiedHorizontalPodAutoscaler

--

`replace_namespaced_horizontal_pod_autoscaler_status(self,body,namespace,name)`

replacestatusofthespecifiedHorizontalPodAutoscaler

--

`watch_namespaced_horizontal_pod_autoscaler(self,namespace,name)`

watchchangestoanobjectofkindHorizontalPodAutoscaler

--

`watch_namespaced_horizontal_pod_autoscaler_list(self)`

watchindividualchangestoalistofHorizontalPodAutoscaler

--

`watch_namespaced_horizontal_pod_autoscaler_list_2(self,namespace)`

watchindividualchangestoalistofHorizontalPodAutoscaler

## Tests

(Please make sure you have [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) installed)

 Execute the following command to run the tests in the current Python (v2 or v3) environment:

```sh
$ make test
[... magically installs dependencies and runs tests on your virtualenv]
Ran 7 tests in 19.289s

OK
```
or

```
$ mvn integration-test -rf :PythonPetstoreClientTests
Using 2195432783 as seed
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 37.594 s
[INFO] Finished at: 2015-05-16T18:00:35+08:00
[INFO] Final Memory: 11M/156M
[INFO] ------------------------------------------------------------------------
```
If you want to run the tests in all the python platforms:

```sh
$ make test-all
[... tox creates a virtualenv for every platform and runs tests inside of each]
  py27: commands succeeded
  py34: commands succeeded
  congratulations :)
```
