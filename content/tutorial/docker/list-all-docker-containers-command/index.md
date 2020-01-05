+++
title="List all containers in Docker command"
summary="We can get a list of all containers in  docker using docker container list or docker ps commands."
keywords="docker,list all container,command to show all containers"
type='post'
date='2020-01-03T18:03:40+0000'
lastmod='2020-01-03T18:03:40+0000'
draft='false'
authors=['admin']
[image]
caption='List all containers in Docker command'
focal_point=''
preview_only=false
+++

We can get a list of all containers in  docker using `docker container list` or `docker ps` commands.

{{%toc%}}

## **List Docker Containers**

To list down docker containers we can use below two commands

1. docker container list
2. docker ps

`docker container ls` command introduced in docker 1.13 version. In older versions we have to use `docker ps` command.


## **List all Containers in docker, using docker ls command**


The below command returns a list of all containers in docker.

```
docker container list -all
```

or

```
docker container ls -all
```

## **List all containers in docker, using docker ps command**

In older version of docker we can use `docker ps` command to list all containers in docker.

```
$ docker ps -all
```
or 
```
$ docker ps -a
```

## **List all Running docker containers**

The default `docker container ls` command shows all running docker containers.

```
$ docker container list
```
or 

```
$ docker container ls
```
or

To get list of all running docker containers use the below command

```
$ docker ps
```

## **List all stopped docker containers command**

To get list of all stopped containers in docker use the below commands

```
$ docker container list -f "status=exited"
```

or 

```
$ docker container ls -f "status=exited"

```
or you can use `docker ps` command

```
$ docker ps -f "status=exited"

```

## **List all latest created docker containers**

To list out all latest created containers in docker use the below command.

```
$ docker container list --latest 
```

## **Show n last created docker containers**

To display n last created containers in docker use the below command.

```
$ docker container list --last=n
```