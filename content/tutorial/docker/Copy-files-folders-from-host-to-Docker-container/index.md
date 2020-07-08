+++
title="Copying files/folders from host to Docker container & docker container to host"
summary="To copy files or folders from host to docker container or docker container to host use docker cp command"
keywords=["cp from host to container,cp from container to host"]
type='post'
date='2020-01-02T18:08:51+0000'
lastmod='2020-01-02T18:08:51+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

To copy files or folders from host to docker container or docker container to host we can use `docker cp` command. 

{{%toc%}}

## **docker cp**

docker copy command `docker cp` is used to Copy files or folders between a docker container and the local host filesystem

We have to pass docker container id, source and destination path arguments to `docker cp` command.
 
```
docker cp CONTAINER_ID:SOURCE_PATH DESTINATION_PATH
docker cp SOURCE_PATH CONTAINER_ID:DESTINATION_PATH
```

In Docker versions prior to 1.8 it was only possible to copy files from a docker container to the host. Not from the host to a docker container.


## **Copy files from host to docker container**

To copy a file from host to docker container the below steps.

1. Get the docker container id by using `docker ps` command.
2. Copy file from host to container by using `docker cp` command.

```
$ docker ps

CONTAINER ID  IMAGE         COMMAND CREATED         STATUS           PORTS  NAMES
74789744g489  docker_image          9 seconds ago  Up 9 seconds    0.0.0.0:8080->8080/tcp   myblog_container

```
Now copy the file from host to container.

```
$ docker cp copytocontainer.html 74789744g489:/copytocontainer.html
```

## **Copy files from docker container to host**

Similarly by using docker container id,we can copy files from docker container to host as well. 

```
$ docker cp 74789744g489:/copytohost.html copytohost.html

```

## **Copy a folder from host to docker container**

`docker cp` command can be used to copy an entire folder from host to docker container and vice versa.

```
$ docker cp Desktop/images 74789744g489:/root/img_files/car_photos/images

```

## **Copy a folder from docker container to host**

To copy a folder from docker container to host use the below `docker cp` command.

```
$ docker cp 74789744g489:/root/img_files/car_photos/images Desktop/images 

```

