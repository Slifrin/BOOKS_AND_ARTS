FROM cpp-build-base:0.1.0 AS build

WORKDIR /src

COPY CMakeLists.txt cpp_in_docker.cpp ./

RUN cmake . && make

FROM ubuntu:bionic

WORKDIR /opt/hello-world

COPY --from=build /src/helloCPPInDocker ./

CMD ["./helloCPPInDocker"]